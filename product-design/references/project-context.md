# Project Context Model

Capture only context that can change a design decision. Unknown values remain unknown; do not fill the model with plausible fiction.

## Required core

- **Product and artifact:** what is being designed, and whether it is a marketing page, public-information site, transactional flow, product interface, dashboard, expert tool, or safety-critical system.
- **Primary users:** role, expertise, access needs, language, environment, and frequency of use when known.
- **Critical job:** the outcome users need, not the control they should click.
- **Business or operational outcome:** what the organization needs to improve or protect.
- **Scope:** journey start, journey end, included surfaces, and exclusions.
- **Constraints:** brand, platform, technology, data, policy, deadline, content, accessibility, and decisions already made.

## Decision-changing context

Add when relevant:

- risk and consequence of error;
- reversibility and approval requirements;
- decision density and data complexity;
- device, viewport, input mode, connectivity, and environmental conditions;
- content maturity and source of truth;
- localization, right-to-left, and formatting requirements;
- existing design system and implementation state;
- available analytics, research, support evidence, and prior attempts.

## Context ledger

Use four explicit buckets:

| Bucket | Meaning | Treatment |
|---|---|---|
| Fact | Supplied or directly verified | May constrain the design |
| Evidence | Observed or measured behavior | May support a finding or decision |
| Inference | Reasoned but unverified interpretation | Label and validate if consequential |
| Open question | Missing information that could change the result | Ask or define a validation step |

Record user decisions separately. Do not quietly replace them during later synthesis.

## Persistence

When the project needs continuity, validate and store the context as `design-context/project-context.json`. Keep research and design decisions in separate files so evidence is not overwritten by later preferences.

Resolve this skill's directory from its loaded `SKILL.md`, then validate before retrieval:

```bash
SKILL_DIR="/absolute/path/to/product-design"
python3 "$SKILL_DIR/scripts/validate_context.py" design-context/project-context.json
```

The retrieval command performs the same validation when `--context` is supplied. Invalid enums, unknown fields, missing required core fields, and malformed nested values must fail rather than being silently ignored.

Suggested project artifacts:

```text
design-context/
  project-context.json
  research.md
  decisions.md
  design-system/
    master.md
    pages/
```

Do not create this structure for a one-off answer unless persistence will materially help.
