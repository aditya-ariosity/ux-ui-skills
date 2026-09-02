#!/usr/bin/env python3
"""Validate knowledge integrity without third-party dependencies."""

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "knowledge.jsonl"
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DOMAINS = {"research", "product-model", "information-architecture", "interaction",
           "visual-direction", "content", "accessibility", "data-visualization",
           "ai-experience", "trust", "implementation", "evaluation"}
EVIDENCE = {"normative", "empirical", "platform-guidance", "expert-synthesis",
            "product-precedent", "visual-inspiration"}
STATUSES = {"active", "seed-review", "deprecated", "rejected"}


def validate(path=DATA):
    errors = []
    warnings = []
    records = []
    for number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            errors.append(f"line {number}: invalid JSON: {error}")
            continue
        records.append((number, record))
    ids = [record.get("id") for _, record in records]
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        errors.append("duplicate ids: " + ", ".join(duplicates))

    required = {"id", "domain", "title", "guidance", "rationale", "applies_when",
                "avoid_when", "artifact_types", "platforms", "risk_levels", "keywords",
                "evidence_class", "sources", "status", "confidence", "acceptance_checks"}
    for number, record in records:
        missing = sorted(required - set(record))
        if missing:
            errors.append(f"line {number}: missing {', '.join(missing)}")
            continue
        if not ID_PATTERN.fullmatch(str(record["id"])):
            errors.append(f"line {number}: invalid id {record['id']!r}")
        if record["domain"] not in DOMAINS:
            errors.append(f"line {number}: invalid domain {record['domain']!r}")
        if record["evidence_class"] not in EVIDENCE:
            errors.append(f"line {number}: invalid evidence class")
        if record["status"] not in STATUSES:
            errors.append(f"line {number}: invalid status")
        if not isinstance(record["confidence"], (int, float)) or not 0 <= record["confidence"] <= 1:
            errors.append(f"line {number}: confidence must be from 0 to 1")
        if len(record["keywords"]) < 2 or not record["acceptance_checks"]:
            errors.append(f"line {number}: keywords and acceptance checks cannot be empty")
        for source in record["sources"]:
            if not source.get("title") or not str(source.get("url", "")).startswith(("http://", "https://")):
                errors.append(f"line {number}: invalid source")
        verified = record.get("verified_at")
        if verified:
            try:
                parsed = date.fromisoformat(verified)
                if parsed > date.today():
                    errors.append(f"line {number}: verification date is in the future")
            except ValueError:
                errors.append(f"line {number}: invalid verification date")
        elif record["evidence_class"] in {"normative", "empirical", "platform-guidance"}:
            warnings.append(f"{record['id']}: current-source review required")
    return records, errors, warnings


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DATA
    records, errors, warnings = validate(path)
    for warning in warnings:
        print("WARNING:", warning)
    if errors:
        for error in errors:
            print("ERROR:", error)
        raise SystemExit(1)
    print(f"OK: {len(records)} knowledge records; {len(warnings)} review warnings")


if __name__ == "__main__":
    main()
