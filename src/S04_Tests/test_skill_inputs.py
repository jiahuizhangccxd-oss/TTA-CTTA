"""Input/contract regressions, not model behavior or prose-quality tests."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "skill_input_validator", ROOT / ".agent/scripts/validate_agent_skills.py"
)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class SkillInputTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.skill = Path(self.directory.name) / "example"
        self.skill.mkdir()
        self.text = (
            "---\nname: example\ndescription: A bounded test fixture.\n---\n\n"
            "# Example\n\n## Purpose\nP.\n## Required Evidence\nE.\n"
            "## Workflow\nW.\n## Output\nO.\n## Validation\nV.\n"
        )

    def test_five_section_contract_is_accepted(self) -> None:
        (self.skill / "SKILL.md").write_text(self.text, encoding="utf-8")
        self.assertEqual([], validator.validate_skill(self.skill, routeable=True))

    def test_legacy_output_heading_is_not_an_exact_output_heading(self) -> None:
        (self.skill / "SKILL.md").write_text(
            self.text.replace("## Output\n", "## Output Contract\n"), encoding="utf-8"
        )
        self.assertTrue(validator.validate_skill(self.skill, routeable=True))

    def test_corrupt_instruction_bytes_fail_instead_of_being_replaced(self) -> None:
        (self.skill / "SKILL.md").write_bytes(self.text.encode("utf-8") + b"\xff")
        errors = validator.validate_skill(self.skill, routeable=False)
        self.assertEqual(1, len(errors))
        self.assertIn("cannot read UTF-8 Skill", errors[0])


if __name__ == "__main__":
    unittest.main()
