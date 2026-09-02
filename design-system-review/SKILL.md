---
name: design-system-review
description: Review a design system, token architecture, component library, Figma library, or Storybook for product-wide consistency, accessibility, adoption, and governance. Trigger on "audit our design system", "review these components", or "assess token drift". Use ux-ui-audit for a product screen or flow. Do not create a visual brand from scratch.
metadata:
  argument-hint: "[library, tokens, Storybook, Figma, code, or product samples]"
---

# Design System Review

Review the system as a product and an operating model, not a screenshot library. A healthy system creates shared decisions, accessible defaults, predictable behavior, and a credible path from design to production.

## 1. Define the system boundary

Establish:

- products, platforms, brands, themes, locales, and teams served;
- available evidence: token files, component code, Storybook, Figma libraries, documentation, usage analytics, product screenshots, issue logs;
- source of truth for tokens, components, content, and release status;
- expected consumers and valid extension points;
- maturity stage: inventory, emerging library, adopted system, or multi-brand platform.

Do not equate visual inconsistency with system failure until intent and ownership are known.

## 2. Build an evidence inventory

Sample real product usage, not only pristine documentation. Create:

`Pattern | Instances | Intended source | Observed variants | State gaps | Accessibility risk | Adoption signal | Owner`

Trace representative components from semantic token to design asset to code to product. Record drift at the layer where it originates.

## 3. Review four layers

### Foundations and tokens

Read [references/tokens-and-theming.md](references/tokens-and-theming.md). Inspect semantic naming, primitive separation, modes, themes, aliases, units, typography, motion, elevation, density, breakpoints, deprecation, and distribution.

### Components and patterns

Read [references/component-contract.md](references/component-contract.md). Inspect anatomy, variants, states, content, behavior, semantics, keyboard support, responsiveness, composition, APIs, escape hatches, and test coverage.

### Documentation and tooling

Inspect discoverability, examples with real content, do/don't rationale, design-code linkage, changelogs, migration guidance, release channels, and executable stories or tests.

### Governance and adoption

Read [references/governance-and-adoption.md](references/governance-and-adoption.md). Inspect ownership, contribution, decision rights, review service levels, versioning, deprecation, exception handling, support, usage measurement, and funding.

## 4. Diagnose causes, not counts

Cluster symptoms into system causes such as:

- missing semantic layer;
- overloaded component API;
- absent state or content contract;
- inaccessible primitive;
- design-code source conflict;
- undocumented extension path;
- weak contribution and release process;
- migration cost with no product incentive.

Do not recommend one mega-component to eliminate every variation. Preserve legitimate domain differences and standardize the decisions that are truly shared.

## 5. Calibrate findings

Rate each finding by:

- product and accessibility impact;
- reach across instances and teams;
- recurrence and future drift risk;
- migration cost and dependency;
- confidence in evidence.

Use `Critical`, `Major`, `Moderate`, and `Minor` only when the organization already uses those terms; otherwise use `Blocker`, `Systemic`, `Local`, and `Opportunity`. Keep effort separate from impact.

## 6. Produce the review

For a complete input-to-output demonstration, read [references/worked-example.md](references/worked-example.md). Use it to calibrate evidence sampling, system-level diagnosis, and migration detail; do not treat its fictional component inventory as a default.

### System frame

State scope, maturity, evidence, exclusions, and source-of-truth assumptions.

### Health summary

Use a table:

`Layer | Health | Strong evidence | Main risk | Confidence`

Avoid an unweighted score unless criteria and evidence support it.

### Prioritized findings

For each:

`Evidence | Product impact | System cause | Recommended decision | Migration path | Acceptance criteria`

### Token and component plan

Show proposed semantic layers, component contracts, additions, consolidations, deprecations, and intentional exceptions.

### Governance plan

Define owners, contribution flow, release and deprecation rules, support, and adoption measures.

### Sequence

- **Stabilize:** accessibility, broken contracts, conflicting sources, high-risk drift.
- **Consolidate:** semantic tokens, component variants, documentation, parity.
- **Adopt:** migrations, tooling, product integration, measurement.
- **Evolve:** new patterns, multi-brand needs, experiments.

## Quality bar

- evidence includes real product instances;
- appearance, behavior, semantics, and API consistency are reviewed separately;
- tokens express meaning, not only raw values;
- all consequential states are part of the component contract;
- accessible defaults are built into primitives;
- exceptions have explicit owners and rationale;
- design and code have a declared authority and synchronization model;
- recommendations include migration and governance, not only cleanup.
