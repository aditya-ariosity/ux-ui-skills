#!/usr/bin/env python3
"""Run observable retrieval benchmarks against the seed knowledge store."""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from search import search  # noqa: E402

DEFAULT_CASES = ROOT / "tests" / "fixtures" / "benchmark-cases.json"


def validate_fixture(fixture):
    errors = []
    cases = fixture.get("cases") if isinstance(fixture, dict) else None
    if not isinstance(cases, list) or len(cases) < 8:
        return ["benchmark must contain at least 8 cases"]
    ids = [case.get("id") for case in cases if isinstance(case, dict)]
    if len(ids) != len(cases) or any(not item for item in ids):
        errors.append("every benchmark case needs a non-empty id")
    if len(ids) != len(set(ids)):
        errors.append("benchmark case ids must be unique")
    negative_count = 0
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"case {index}: expected an object")
            continue
        label = case.get("id", f"case {index}")
        if not isinstance(case.get("query"), str) or not case["query"].strip():
            errors.append(f"{label}: query must be a non-empty string")
        if not isinstance(case.get("context", {}), dict):
            errors.append(f"{label}: context must be an object")
        expects_abstain = case.get("expect_abstain") is True
        expected = case.get("expected_any_top3")
        if expects_abstain:
            negative_count += 1
            if expected:
                errors.append(f"{label}: abstention cases cannot define expected results")
        elif not isinstance(expected, list) or not expected:
            errors.append(f"{label}: positive cases need expected_any_top3")
    if negative_count == 0:
        errors.append("benchmark needs at least one abstention case")
    return errors


def evaluate(path=DEFAULT_CASES, min_recall=1.0, min_abstention=1.0, min_forbidden=1.0):
    fixture = json.loads(Path(path).read_text(encoding="utf-8"))
    fixture_errors = validate_fixture(fixture)
    if fixture_errors:
        raise ValueError("Invalid benchmark fixture:\n- " + "\n- ".join(fixture_errors))
    records = []
    positives = []
    negatives = []
    forbidden_checks = []
    for case in fixture["cases"]:
        result = search(case["query"], case.get("context", {}), limit=3)
        ids = [item["id"] for item in result["results"]]
        if case.get("expect_abstain"):
            passed = result["abstained"]
            negatives.append(passed)
            records.append({"id": case["id"], "passed": passed, "abstained": result["abstained"], "actual": ids})
            continue
        expected = case.get("expected_any_top3", [])
        positive = any(item in ids for item in expected)
        forbidden = not any(item in ids for item in case.get("forbidden_top3", []))
        positives.append(positive)
        forbidden_checks.append(forbidden)
        records.append({"id": case["id"], "passed": positive and forbidden,
                        "expected_any_top3": expected, "actual": ids,
                        "forbidden_clear": forbidden})
    metrics = {
        "case_count": len(records),
        "expected_recall_at_3": sum(positives) / len(positives) if positives else 0,
        "negative_abstention": sum(negatives) / len(negatives) if negatives else 0,
        "forbidden_clear_rate": sum(forbidden_checks) / len(forbidden_checks) if forbidden_checks else 0,
    }
    gates = {
        "all_cases_pass": all(case["passed"] for case in records),
        "expected_recall_at_3": metrics["expected_recall_at_3"] >= min_recall,
        "negative_abstention": metrics["negative_abstention"] >= min_abstention,
        "forbidden_clear_rate": metrics["forbidden_clear_rate"] >= min_forbidden,
    }
    return {"passed": all(gates.values()), "gates": gates, "metrics": metrics, "cases": records}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", default=str(DEFAULT_CASES))
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--min-recall", type=float, default=1.0)
    parser.add_argument("--min-abstention", type=float, default=1.0)
    parser.add_argument("--min-forbidden", type=float, default=1.0)
    args = parser.parse_args()
    for value in (args.min_recall, args.min_abstention, args.min_forbidden):
        if not 0 <= value <= 1:
            raise SystemExit("benchmark thresholds must be from 0 to 1")
    try:
        report = evaluate(args.cases, args.min_recall, args.min_abstention, args.min_forbidden)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        raise SystemExit(str(error)) from error
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        for key, value in report["metrics"].items():
            print(f"{key}: {value}")
        for case in report["cases"]:
            print(("PASS" if case["passed"] else "FAIL") + ": " + case["id"] + " -> " + ", ".join(case["actual"]))
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
