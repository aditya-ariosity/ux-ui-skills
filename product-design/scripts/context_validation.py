#!/usr/bin/env python3
"""Validate persisted project context against the bundled schema subset."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "data" / "project-context.schema.json"


def _type_matches(value, expected):
    return {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
    }.get(expected, True)


def _validate(value, schema, path="$", enforce_required=True):
    errors = []
    expected = schema.get("type")
    if expected and not _type_matches(value, expected):
        return [f"{path}: expected {expected}"]

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value {value!r} is not allowed")

    if isinstance(value, str) and len(value) < schema.get("minLength", 0):
        errors.append(f"{path}: must not be empty")

    if isinstance(value, list):
        if schema.get("uniqueItems"):
            normalized = [json.dumps(item, sort_keys=True) for item in value]
            if len(normalized) != len(set(normalized)):
                errors.append(f"{path}: values must be unique")
        item_schema = schema.get("items", {})
        for index, item in enumerate(value):
            errors.extend(_validate(item, item_schema, f"{path}[{index}]", enforce_required))

    if isinstance(value, dict):
        properties = schema.get("properties", {})
        if enforce_required:
            for key in schema.get("required", []):
                if key not in value:
                    errors.append(f"{path}.{key}: required property is missing")
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    errors.append(f"{path}.{key}: unknown property")
        for key, item in value.items():
            if key in properties:
                errors.extend(_validate(item, properties[key], f"{path}.{key}", enforce_required))
    return errors


def validate_context(context, schema_path=DEFAULT_SCHEMA, enforce_required=True):
    schema = json.loads(Path(schema_path).read_text(encoding="utf-8"))
    return _validate(context, schema, enforce_required=enforce_required)


def load_context(path, schema_path=DEFAULT_SCHEMA):
    try:
        context = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Unable to read context {path}: {error}") from error
    errors = validate_context(context, schema_path)
    if errors:
        raise ValueError("Invalid project context:\n- " + "\n- ".join(errors))
    return context
