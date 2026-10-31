"""Markdown migration tests; these do not execute or evaluate an AI host."""
from __future__ import annotations

import html
import json
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src/S03_Scripts"))
from papertrace_validation.documents import document_path, load_document
from papertrace_validation.model import Reporter
from papertrace_validation.methods import validate_method_design
from papertrace_validation.project import validate_paper_state, validate_required_layout
from papertrace_validation.gates import validate_stage_gates
from test_validator_semantics import ValidatorFixture


def record(data: dict) -> str:
    """Fixture serializer: plain Markdown tables, no production write-back path."""
    rows = ["# Test\n", "| Field | Value | Type |", "|---|---|---|"]

    def append(key, value):
        if isinstance(value, dict) and value:
            for child, item in value.items():
                append(f"{key}.{child}" if key else child, item)
        else:
            kind = "text" if isinstance(value, str) else "json"
            text = value if kind == "text" else json.dumps(value, ensure_ascii=False)
            text = html.escape(text, quote=False).replace("|", "&#124;").replace("\n", "<br>")
            rows.append(f"| {key} | {text} | {kind} |")

    for key, value in data.items():
        append(key, value)
    return "\n".join(rows) + "\n"


class MarkdownCoreTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.fixture = ValidatorFixture(self.root)
        legacy = self.root / "paper/paper.yaml"
        self.paper = yaml.safe_load(legacy.read_text())
        self.path = self.root / "paper/core/02_RESEARCH.md"
        self.path.parent.mkdir()
        self.path.write_text(record(self.paper), encoding="utf-8")
        legacy.unlink()

    def read(self, text=None):
        if text is not None:
            self.path.write_text(text, encoding="utf-8")
        reporter = Reporter(self.root)
        return load_document(self.path, reporter), reporter

    def test_markdown_replaces_yaml_without_changing_record(self):
        value, report = self.read()
        self.assertEqual(self.paper, value)
        self.assertFalse(report.errors)
        self.assertEqual(set(), self.fixture.error_codes())

    def test_missing_active_source_still_fails(self):
        (self.root / "paper/draft/main.md").unlink()
        self.assertIn("E-ACTIVE-SOURCE-FILE", self.fixture.error_codes())

    def test_dual_project_authority_is_rejected(self):
        self.fixture.write("paper/paper.yaml", yaml.safe_dump(self.paper))
        self.assertIn("E-DOCUMENT-AUTHORITY", self.fixture.error_codes())

    def test_legacy_only_project_is_still_readable(self):
        self.path.unlink()
        self.fixture.write("paper/paper.yaml", yaml.safe_dump(self.paper))
        self.assertEqual(set(), self.fixture.error_codes())

    def test_duplicate_and_parent_child_fields_are_rejected(self):
        for extra in ["| paper_stage | submitted | text |", "| research_state | {} | json |"]:
            with self.subTest(extra=extra):
                _, report = self.read(record(self.paper) + extra + "\n")
                self.assertIn("E-DOCUMENT-DUPLICATE", {e.code for e in report.errors})

    def test_collection_does_not_overwrite_nested_scalar_record(self):
        paper = dict(self.paper)
        paper["main_claims"] = {"text": "must not be silently discarded"}
        table = "\n## main_claims\n| claim_id | text |\n|---|---|\n| C1 | different claim |\n"
        _, report = self.read(record(paper) + table)
        self.assertIn("E-DOCUMENT-DUPLICATE", {e.code for e in report.errors})

    def test_invalid_json_does_not_become_approval(self):
        text = record(self.paper).replace("| false | json |", "| yes | json |", 1)
        _, report = self.read(text)
        self.assertIn("E-DOCUMENT-VALUE", {e.code for e in report.errors})

    def test_text_false_is_not_a_boolean_confirmation(self):
        text = record(self.paper).replace("| false | json |", "| false | text |")
        self.read(text)
        self.assertIn("E-HUMAN-GATE-TYPE", self.fixture.error_codes())

    def test_markdown_does_not_remove_tex_confirmation(self):
        self.paper.update(paper_stage="tex_formalization", active_source="tex", freeze={"frozen": True})
        self.paper["research_state"]["central_question"] = "A real question"
        self.fixture.write("paper/tex/main.tex", "\\documentclass{article}")
        self.read(record(self.paper))
        self.assertIn("E-STAGE-CONFIRMATION", self.fixture.error_codes())

    def test_fenced_examples_do_not_overwrite_real_fields(self):
        value, report = self.read(record(self.paper) + "\n```markdown\n" + record({"paper_stage": "submitted"}) + "```\n")
        self.assertEqual("idea", value["paper_stage"])
        self.assertFalse(report.errors)

    def test_unicode_pipes_and_multiline_text_round_trip(self):
        self.paper["research_state"]["central_question"] = "问题: P(y|x) & x < y\n第二行"
        value, report = self.read(record(self.paper))
        self.assertEqual(self.paper, value)
        self.assertFalse(report.errors)

    def test_claim_collection_retains_foreign_key_checks(self):
        paper = dict(self.paper)
        paper.pop("main_claims")
        text = record(paper) + "\n## main_claims · 主张\n\n| claim_id | text | boundary |\n|---|---|---|\n| C1 | Claim | bounded |\n"
        value, report = self.read(text)
        self.assertEqual("C1", value["main_claims"][0]["claim_id"])
        self.assertFalse(report.errors)
        self.paper["main_contributions"] = [{"supporting_claims": ["C404"]}]
        self.read(record(self.paper))
        self.assertIn("E-CONTRIBUTION-FK", self.fixture.error_codes())

    def test_malformed_record_table_is_not_silently_ignored(self):
        _, report = self.read(record(self.paper).replace("| Type |", "| Typo |", 1))
        self.assertIn("E-DOCUMENT-TABLE", {e.code for e in report.errors})

    def test_malformed_claim_header_is_rejected(self):
        text = record(self.paper) + "\n## main_claims\n| claim_typo | text |\n|---|---|\n| C1 | claim |\n"
        _, report = self.read(text)
        self.assertIn("E-DOCUMENT-TABLE", {e.code for e in report.errors})

    def test_dual_method_and_literature_authorities_are_rejected(self):
        for name, new, old in [
            ("method", "paper/core/03_METHOD.md", "paper/method/method_spec.yaml"),
            ("literature", "paper/core/06_LITERATURE.md", "paper/refs/reading_matrix.md"),
        ]:
            with self.subTest(name=name):
                self.fixture.write(new, "# new")
                self.fixture.write(old, "old")
                reporter = Reporter(self.root)
                document_path(self.root, name, reporter)
                self.assertIn("E-DOCUMENT-AUTHORITY", {e.code for e in reporter.errors})

    def test_ready_method_is_not_approved_by_format_conversion(self):
        reporter = Reporter(ROOT)
        method = load_document(ROOT / "paper/core/03_METHOD.md", reporter)
        self.assertFalse(reporter.errors)
        method["status"] = "ready"
        self.fixture.write("paper/core/03_METHOD.md", record(method))
        reporter = Reporter(self.root)
        validate_method_design(self.root, reporter, self.paper, set())
        self.assertIn("E-METHOD-READY", {e.code for e in reporter.errors})

    def test_new_literature_still_requires_verified_full_text(self):
        self.paper["main_claims"] = [{"claim_id": "C1", "text": "Claim"}]
        self.read(record(self.paper))
        self.fixture.write("paper/core/06_LITERATURE.md", """# Reading
| Ref ID | Bib key | Verified source | Main evidence | Limitation | Supports/refutes claim | Full text checked | Status |
|---|---|---|---|---|---|---|---|
| R1 | key | doi | result | limit | C1 | no | screened |
""")
        self.fixture.write("paper/experiments/evidence_matrix.md", """# Evidence
| Claim ID | Strength | Evidence ID | Run/ref/artifact | Boundary | Status |
|---|---|---|---|---|---|
| C1 | weak | E1 | R1 | bounded | supported |
""")
        self.assertIn("E-NON-VERIFIED-REF", self.fixture.error_codes())


if __name__ == "__main__":
    unittest.main()
