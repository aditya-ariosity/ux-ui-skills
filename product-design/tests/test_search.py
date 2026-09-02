import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


search_module = load_module("product_design_search", ROOT / "scripts" / "search.py")
validate_module = load_module("product_design_validate", ROOT / "scripts" / "validate_data.py")
evaluate_module = load_module("product_design_evaluate", ROOT / "scripts" / "evaluate.py")
context_module = load_module("product_design_context", ROOT / "scripts" / "context_validation.py")


class SearchTests(unittest.TestCase):
    def test_data_integrity(self):
        records, errors, _warnings = validate_module.validate()
        self.assertGreaterEqual(len(records), 10)
        self.assertEqual(errors, [])

    def test_public_institution_routes_to_public_site_guidance(self):
        result = search_module.search(
            "bilingual sovereign public authority governance transparency",
            {"artifact_type": "public-information-site", "platforms": ["responsive-web"], "risk_level": "high"},
            limit=3,
        )
        self.assertIn("public-site-authority-and-findability", [item["id"] for item in result["results"]])

    def test_clinical_support_routes_to_human_authority(self):
        result = search_module.search(
            "clinical dosing recommendation rationale override final decision audit",
            {"artifact_type": "safety-critical-system", "risk_level": "safety-critical"},
            limit=3,
        )
        self.assertIn("safety-critical-review-override-traceability", [item["id"] for item in result["results"]])

    def test_expert_editor_routes_to_tool_guidance(self):
        result = search_module.search(
            "desktop canvas editor selection inspector shortcuts undo",
            {"artifact_type": "expert-tool", "platforms": ["desktop"]},
            limit=3,
        )
        self.assertIn("expert-tool-preserve-density-and-direct-manipulation", [item["id"] for item in result["results"]])

    def test_vague_preference_abstains(self):
        result = search_module.search("make it awesome and modern")
        self.assertTrue(result["abstained"])

    def test_benchmark_suite(self):
        report = evaluate_module.evaluate()
        self.assertTrue(report["passed"], json.dumps(report, indent=2))

    def test_benchmark_reports_failure_for_wrong_expectation(self):
        fixture_path = ROOT / "tests" / "fixtures" / "benchmark-cases.json"
        fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
        fixture["cases"][0]["expected_any_top3"] = ["id-that-does-not-exist"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "failing-cases.json"
            path.write_text(json.dumps(fixture), encoding="utf-8")
            report = evaluate_module.evaluate(path)
        self.assertFalse(report["passed"])
        self.assertFalse(report["gates"]["all_cases_pass"])

    def test_project_context_schema_is_enforced(self):
        valid = {
            "product": "NovaCart",
            "artifact_type": "transactional-flow",
            "critical_job": "Complete checkout",
            "scope": {"includes": ["checkout"], "excludes": ["account"]},
            "facts": [],
            "assumptions": [],
            "decisions": [],
        }
        self.assertEqual(context_module.validate_context(valid), [])
        invalid = {**valid, "artifact_type": "shopping", "invented": True}
        errors = context_module.validate_context(invalid)
        self.assertTrue(any("not allowed" in error for error in errors))
        self.assertTrue(any("unknown property" in error for error in errors))

    def test_search_command_does_not_depend_on_current_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "search.py"), "--query", "payment retry recovery"],
                cwd=directory,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(result.stdout.strip())


if __name__ == "__main__":
    unittest.main()
