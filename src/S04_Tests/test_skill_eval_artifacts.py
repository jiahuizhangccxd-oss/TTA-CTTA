"""Test the evaluator with synthetic snapshots, not simulated host successes."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "artifact_eval_under_test", ROOT / ".agent/scripts/validate_skill_evals.py"
)
assert SPEC is not None and SPEC.loader is not None
EVAL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EVAL)


class ArtifactEvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.before = self.root / "before"
        self.after = self.root / "after"
        for root in (self.before, self.after):
            (root / "CODE/src").mkdir(parents=True)
            (root / "CODE/src/model.py").write_text("old\n", encoding="utf-8")
        self.case = {
            "case_id": "CODE", "language": "en", "prompt": "Fix the specified behavior.",
            "expected_primary": "code-change", "expected_primary_surface": "code",
            "must_change_product": True, "audit_allowed": False,
            "artifact_paths": ["src/model.py"],
        }
        self.result = {
            "case_id": "CODE", "selected_primary": "code-change", "primary_surface": "code",
            "product_changed": True, "audit_used": False, "user_visible_summary": "Changed source.",
        }

    def score(self):
        return EVAL.score_artifacts({"CODE": self.case}, self.before, self.after)

    def change(self):
        (self.after / "CODE/src/model.py").write_text("new\n", encoding="utf-8")

    def cli(self, *extra, results=True):
        routing = self.root / "routing.yaml"
        products = self.root / "products.yaml"
        skills = self.root / "skills"
        skills.mkdir(exist_ok=True)
        routing.write_text(yaml.safe_dump({
            "schema_version": 1, "suite": "papertrace-routing", "cases": [{
                "case_id": "OTHER", "prompt": "Read only.", "expected_primary": "none", "critical": True,
            }],
        }), encoding="utf-8")
        products.write_text(yaml.safe_dump({
            "schema_version": 1, "suite": "papertrace-product-surfaces", "cases": [self.case],
        }), encoding="utf-8")
        argv = ["--cases", str(routing), "--product-cases", str(products),
                "--skills-root", str(skills), "--case-id", "CODE", "--json"]
        if results:
            records = self.root / "results.jsonl"
            records.write_text(json.dumps(self.result) + "\n", encoding="utf-8")
            argv += ["--results", str(records)]
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = EVAL.main(argv + list(extra))
        return code, json.loads(output.getvalue())

    def test_real_file_change_passes_file_check_only(self):
        self.change()
        score = self.score()
        self.assertEqual(score["checked_cases"], ["CODE"])
        self.assertEqual(score["failures"], [])

    def test_self_report_cannot_replace_file_change(self):
        self.assertEqual(EVAL.score_products({"CODE": self.case}, {"CODE": self.result})["failures"], [])
        self.assertTrue(self.score()["failures"])

    def test_log_only_change_does_not_complete_code_task(self):
        (self.after / "CODE/STATUS.md").write_text("done\n", encoding="utf-8")
        self.assertTrue(self.score()["failures"])

    def test_deleted_product_is_not_completion(self):
        (self.after / "CODE/src/model.py").unlink()
        self.assertTrue(self.score()["failures"])

    def test_empty_product_is_not_completion(self):
        (self.after / "CODE/src/model.py").write_bytes(b"")
        self.assertTrue(self.score()["failures"])

    def test_new_product_is_valid_file_change(self):
        (self.before / "CODE/src/model.py").unlink()
        self.assertEqual(self.score()["failures"], [])

    def test_all_declared_products_are_required(self):
        self.change()
        self.case["artifact_paths"].append("results/comparison.json")
        self.assertTrue(self.score()["failures"])

    def test_protected_split_change_is_rejected(self):
        self.change()
        self.case["protected_paths"] = ["split.json"]
        (self.before / "CODE/split.json").write_text('["machine-a"]', encoding="utf-8")
        (self.after / "CODE/split.json").write_text('["machine-b"]', encoding="utf-8")
        self.assertTrue(self.score()["failures"])

    def test_unchanged_protected_split_passes(self):
        self.change()
        self.case["protected_paths"] = ["split.json"]
        for root in (self.before, self.after):
            (root / "CODE/split.json").write_text('["machine-a"]', encoding="utf-8")
        self.assertEqual(self.score()["failures"], [])

    def test_read_only_product_must_remain_unchanged(self):
        self.case["must_change_product"] = False
        self.assertEqual(self.score()["failures"], [])
        self.change()
        self.assertTrue(self.score()["failures"])

    def test_snapshot_cannot_be_missing_or_same_directory(self):
        self.assertTrue(EVAL.score_artifacts({"CODE": self.case}, self.before, self.before)["failures"])
        self.assertTrue(EVAL.score_artifacts({"CODE": self.case}, self.before, self.root / "missing")["failures"])

    def test_artifact_cannot_escape_snapshot(self):
        self.case["artifact_paths"] = ["../outside.txt"]
        self.assertTrue(self.score()["failures"])

    def test_symlink_cannot_import_outside_artifact(self):
        outside = self.root / "outside.txt"
        outside.write_text("not a captured product", encoding="utf-8")
        target = self.after / "CODE/src/model.py"
        target.unlink()
        try:
            target.symlink_to(outside)
        except OSError:
            self.skipTest("symlinks are unavailable in this runtime")
        self.assertTrue(self.score()["failures"])

    def test_unconfigured_cases_are_explicitly_unchecked(self):
        del self.case["artifact_paths"]
        score = self.score()
        self.assertEqual(score["checked_cases"], [])
        self.assertEqual(score["unchecked_cases"], ["CODE"])

    def test_results_do_not_set_behavior_executed(self):
        code, report = self.cli()
        self.assertEqual(code, 0)
        self.assertTrue(report["reported_results_scored"])
        self.assertFalse(report["behavior_executed"])
        self.assertFalse(report["host_execution_verified"])
        self.assertIsNone(report["artifact_metrics"])

    def test_definition_mode_is_json_and_never_runs_host(self):
        code, report = self.cli(results=False)
        self.assertEqual(code, 0)
        self.assertEqual(report["mode"], "definitions-only")
        self.assertFalse(report["behavior_executed"])
        self.assertFalse(report["reported_results_scored"])

    def test_selected_case_checks_actual_output(self):
        code, report = self.cli("--before", str(self.before), "--after", str(self.after))
        self.assertEqual(code, 1)
        self.assertTrue(report["artifact_metrics"]["failures"])
        self.change()
        code, report = self.cli("--before", str(self.before), "--after", str(self.after))
        self.assertEqual(code, 0)
        self.assertEqual(report["routing_case_definitions"], 0)
        self.assertEqual(report["product_case_definitions"], 1)
        self.assertFalse(report["host_execution_verified"])

    def test_unknown_case_does_not_silently_pass(self):
        code, report = self.cli("--case-id", "MISSING")
        self.assertEqual(code, 1)
        self.assertTrue(report["errors"])

    def test_partial_snapshot_arguments_are_rejected(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            self.cli("--before", str(self.before))

    def test_protection_only_definition_is_rejected(self):
        del self.case["artifact_paths"]
        self.case["protected_paths"] = ["split.yaml"]
        code, report = self.cli(results=False)
        self.assertEqual(code, 1)
        self.assertIn("CODE.protected_paths requires artifact_paths", report["errors"])

    def test_unsafe_path_definition_fails(self):
        self.case["artifact_paths"] = ["../../private.txt"]
        code, report = self.cli(results=False)
        self.assertEqual(code, 1)
        self.assertTrue(report["errors"])


if __name__ == "__main__":
    unittest.main()
