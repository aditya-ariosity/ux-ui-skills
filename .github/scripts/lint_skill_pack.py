#!/usr/bin/env python3
"""Lint skill metadata and local SKILL.md links without external dependencies."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
DESCRIPTION_MIN = 160
DESCRIPTION_MAX = 420


def read_frontmatter(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return {}, ["missing opening frontmatter delimiter"]
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return {}, ["missing closing frontmatter delimiter"]

    data = {}
    errors = []
    current_parent = None
    for line in lines[1:end]:
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            if current_parent == "metadata" and line.strip().startswith("argument-hint:"):
                _, value = line.strip().split(":", 1)
                data["metadata.argument-hint"] = value.strip().strip('"')
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        current_parent = key.strip()
        data[current_parent] = value.strip().strip('"')
    return data, errors


def lint_links(path):
    text = path.read_text(encoding="utf-8")
    errors = []
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = match.group(1).strip()
        if (
            "://" in target
            or target.startswith("#")
            or target.startswith("mailto:")
            or target.startswith("data:")
        ):
            continue
        local_target = target.split("#", 1)[0]
        if not local_target:
            continue
        if not (path.parent / local_target).exists():
            errors.append(f"broken relative link in {path.relative_to(ROOT)}: {target}")
    return errors


def main():
    errors = []
    for path in sorted(ROOT.glob("*/SKILL.md")):
        data, frontmatter_errors = read_frontmatter(path)
        label = path.relative_to(ROOT)
        errors.extend(f"{label}: {error}" for error in frontmatter_errors)

        name = data.get("name")
        description = data.get("description", "")
        argument_hint = data.get("metadata.argument-hint")

        if not name:
            errors.append(f"{label}: missing name")
        elif name != path.parent.name:
            errors.append(f"{label}: name must match folder name")

        if not description:
            errors.append(f"{label}: missing description")
        elif not DESCRIPTION_MIN <= len(description) <= DESCRIPTION_MAX:
            errors.append(
                f"{label}: description length {len(description)} outside "
                f"{DESCRIPTION_MIN}-{DESCRIPTION_MAX}"
            )

        if not argument_hint:
            errors.append(f"{label}: missing metadata.argument-hint")

        errors.extend(lint_links(path))

    if errors:
        print("Skill pack lint failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill pack lint passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
