#!/usr/bin/env python3
"""Small, dependency-free retrieval layer for product-design knowledge records."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from context_validation import load_context as load_validated_context

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "knowledge.jsonl"

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in",
    "is", "it", "of", "on", "or", "that", "the", "this", "to", "with",
}
SYNONYMS = {
    "website": "site", "webpage": "page", "colour": "color", "a11y": "accessibility",
    "bi": "dashboard", "analytics": "dashboard", "admin": "operations",
    "doctor": "clinician", "physician": "clinician", "medical": "clinical",
    "professional": "expert", "ide": "editor", "workspace": "tool",
}
SEARCH_FIELDS = {
    "title": 4.0,
    "keywords": 3.5,
    "applies_when": 2.0,
    "guidance": 1.4,
    "rationale": 0.8,
    "required_evidence": 0.7,
}
MIN_SCORE = 3.0


def tokenize(value):
    if isinstance(value, list):
        value = " ".join(str(item) for item in value)
    text = str(value or "").casefold()
    for source, target in SYNONYMS.items():
        text = re.sub(r"(?<!\w)" + re.escape(source) + r"(?!\w)", target, text)
    return [token for token in re.findall(r"[a-z0-9]+", text)
            if token not in STOPWORDS and len(token) > 1]


def load_records(path=DEFAULT_DATA):
    records = []
    with Path(path).open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise ValueError(f"Invalid JSONL at line {line_number}: {error}") from error
    return [record for record in records
            if record.get("status") in {"active", "seed-review"}]


def load_context(path):
    if not path:
        return {}
    return load_validated_context(path)


class BM25:
    def __init__(self, documents, k1=1.5, b=0.75):
        self.documents = documents
        self.k1 = k1
        self.b = b
        self.lengths = [len(document) for document in documents]
        self.average_length = sum(self.lengths) / len(self.lengths) if self.lengths else 1.0
        self.term_counts = [Counter(document) for document in documents]
        frequencies = defaultdict(int)
        for counts in self.term_counts:
            for term in counts:
                frequencies[term] += 1
        total = len(documents)
        self.idf = {
            term: math.log(1 + (total - count + 0.5) / (count + 0.5))
            for term, count in frequencies.items()
        }

    def score(self, query_tokens, index):
        score = 0.0
        counts = self.term_counts[index]
        length = self.lengths[index]
        for token in query_tokens:
            frequency = counts.get(token, 0)
            if not frequency:
                continue
            numerator = frequency * (self.k1 + 1)
            denominator = frequency + self.k1 * (
                1 - self.b + self.b * length / (self.average_length or 1.0)
            )
            score += self.idf[token] * numerator / denominator
        return score


def _field_text(record):
    tokens = []
    for field, weight in SEARCH_FIELDS.items():
        field_tokens = tokenize(record.get(field, ""))
        tokens.extend(field_tokens * max(1, round(weight * 2)))
    return tokens


def _context_values(context, key):
    value = context.get(key, [])
    if isinstance(value, str):
        return {value.casefold()}
    return {str(item).casefold() for item in value}


def _context_bonus(record, context):
    bonus = 0.0
    reasons = []
    artifact = str(context.get("artifact_type", "")).casefold()
    record_artifacts = _context_values(record, "artifact_types")
    if artifact and artifact in record_artifacts:
        bonus += 2.2
        reasons.append(f"artifact:{artifact}")
    elif artifact and record_artifacts and "other" not in record_artifacts:
        bonus -= 2.2
        reasons.append(f"artifact-mismatch:{artifact}")
    platforms = _context_values(context, "platforms")
    record_platforms = _context_values(record, "platforms")
    platform_matches = platforms & record_platforms
    if platform_matches:
        bonus += 0.8
        reasons.append("platform:" + ",".join(sorted(platform_matches)))
    elif platforms and "cross-platform" in record_platforms:
        bonus += 0.4
        reasons.append("platform:cross-platform")
    risk = str(context.get("risk_level", "")).casefold()
    if risk and risk in _context_values(record, "risk_levels"):
        bonus += 0.8
        reasons.append(f"risk:{risk}")
    return bonus, reasons


def search(query, context=None, domain=None, limit=5, data_path=DEFAULT_DATA):
    context = context or {}
    records = load_records(data_path)
    if domain:
        records = [record for record in records if record.get("domain") == domain]
    if not records:
        return {"query": query, "count": 0, "abstained": True, "results": []}

    query_text = " ".join(
        [query, str(context.get("product", "")), str(context.get("critical_job", "")),
         " ".join(context.get("constraints", []))]
    )
    query_tokens = tokenize(query_text)
    index = BM25([_field_text(record) for record in records])
    ranked = []
    for position, record in enumerate(records):
        lexical = index.score(query_tokens, position)
        context_score, context_reasons = _context_bonus(record, context)
        avoid_tokens = set(tokenize(record.get("avoid_when", [])))
        conflict = sorted(set(query_tokens) & avoid_tokens)
        penalty = min(3.0, len(conflict) * 0.75)
        score = lexical + context_score - penalty
        matched = sorted(set(query_tokens) & set(_field_text(record)))
        ranked.append((score, record, matched, context_reasons, conflict))
    ranked.sort(key=lambda item: (-item[0], item[1]["id"]))

    top_score = ranked[0][0] if ranked else 0.0
    abstained = top_score < MIN_SCORE
    results = []
    if not abstained:
        for score, record, matched, context_reasons, conflict in ranked[:limit]:
            if score <= 0:
                continue
            results.append({
                "id": record["id"],
                "domain": record["domain"],
                "title": record["title"],
                "guidance": record["guidance"],
                "status": record["status"],
                "confidence": record["confidence"],
                "score": round(score, 4),
                "why": {"matched_terms": matched, "context": context_reasons,
                        "conflicts": conflict},
                "acceptance_checks": record["acceptance_checks"],
                "sources": record["sources"],
            })
    return {
        "query": query,
        "domain": domain,
        "count": len(results),
        "abstained": abstained,
        "threshold": MIN_SCORE,
        "top_score": round(top_score, 4),
        "results": results,
    }


def format_markdown(result):
    if result["abstained"]:
        return f"No verified knowledge match for `{result['query']}` (score {result['top_score']}; threshold {result['threshold']})."
    lines = [f"## Knowledge matches for: {result['query']}", ""]
    for item in result["results"]:
        review = " — review required" if item["status"] == "seed-review" else ""
        lines.extend([
            f"### {item['title']}",
            f"`{item['id']}` · {item['domain']} · score {item['score']} · confidence {item['confidence']}{review}",
            "",
            item["guidance"],
            "",
            "Why matched: " + (", ".join(item["why"]["matched_terms"] + item["why"]["context"]) or "contextual score"),
            "",
        ])
    return "\n".join(lines).rstrip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--context")
    parser.add_argument("--domain")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--data", default=str(DEFAULT_DATA))
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    parser.add_argument("--diagnostics", action="store_true")
    args = parser.parse_args()
    if args.limit < 1 or args.limit > 20:
        raise SystemExit("--limit must be from 1 to 20")
    try:
        result = search(args.query, load_context(args.context), args.domain, args.limit, args.data)
    except ValueError as error:
        raise SystemExit(str(error)) from error
    if args.format == "json" or args.diagnostics:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(format_markdown(result))


if __name__ == "__main__":
    main()
