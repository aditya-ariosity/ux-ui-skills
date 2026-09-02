#!/usr/bin/env python3
"""Validate a persisted product-design project context file."""

import sys
from pathlib import Path

from context_validation import load_context


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: validate_context.py <project-context.json>")
    path = Path(sys.argv[1])
    try:
        context = load_context(path)
    except ValueError as error:
        raise SystemExit(str(error)) from error
    print(f"OK: valid project context for {context['product']}")


if __name__ == "__main__":
    main()
