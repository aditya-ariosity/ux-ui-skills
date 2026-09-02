# Experience and Design Reasoning

Translate evidence into a product model before selecting components or aesthetics.

## Experience model

Describe the critical path as:

`intent → entry → orientation → decision → action → feedback → recovery → completion`

At each step define:

- what the user needs to understand;
- what object or information they act on;
- what decision they make;
- what the system must reveal or withhold;
- what confirms progress;
- what failure, interruption, or reversal requires.

Find the earliest mismatch between the user's mental model and the product model. Do not decorate a broken structure.

## Artifact-type guardrail

Confirm the artifact before using a default structure:

| Artifact | Primary design concern |
|---|---|
| Marketing page | comprehension, differentiation, confidence, conversion |
| Public-information site | findability, authority, transparency, accessibility, multilingual content |
| Transactional flow | prerequisites, commitment, error prevention, recovery, confirmation |
| Product interface | task continuity, state, commands, object relationships, efficiency |
| Dashboard | decisions, exceptions, comparison, freshness, drill-down, trust |
| Expert tool | density, direct manipulation, shortcuts, precision, undo, persistent context |
| Safety-critical system | source, uncertainty, review, override, traceability, safe failure |

Do not apply landing-page section patterns to operational interfaces.

## Information architecture

Organize around user goals and stable domain objects. Define:

- content and object inventory;
- hierarchy and relationships;
- primary and alternate entry points;
- navigation versus commands, filters, and view switches;
- overview-to-detail continuity;
- search, sorting, and filtering behavior;
- URL, deep-link, back, refresh, and state-restoration rules.

## Interaction and states

Model states that can change the task:

- default, focus, hover, active, selected, disabled, read-only;
- loading, progress, queued, empty, partial, stale, offline;
- validation, error, timeout, retry, conflict, success;
- permission, approval, destructive action, undo, cancellation;
- interrupted, resumed, and externally changed data.

State behavior is part of the design, not implementation cleanup.

## Decision rule

Prefer the smallest design decision that resolves the observed need. When evidence permits several solutions, state the required behavior and compare viable directions instead of presenting preference as correctness.
