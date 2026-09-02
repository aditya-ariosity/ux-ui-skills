---
name: dashboard-redesign
description: Redesign a dashboard, KPI view, operational console, or analytical workspace around real decisions and data meaning. Trigger on "redesign this dashboard", "improve these KPIs", or "fix this reporting view". Use ux-ui-audit for diagnosis without redesign and design-system-review for library-wide component issues. Do not invent metrics or thresholds.
metadata:
  argument-hint: "[dashboard artifact, users, decisions, and data definitions]"
---

# Dashboard Redesign

Design a decision instrument, not a wall of metrics. Preserve useful density, expose the comparisons that matter, and make data quality and scope legible.

## 1. Establish the decision model

Identify:

- primary role, expertise, frequency, and environment;
- decisions and actions the dashboard must support;
- monitoring cadence and acceptable time to notice;
- metric definitions, owners, source, freshness, and latency;
- required comparisons, targets, thresholds, and segments;
- downstream workflow from signal to investigation to action;
- devices, display duration, accessibility needs, and export requirements.

If these are unknown, state assumptions and mark metric semantics for owner validation. Never infer that a visible number is a KPI.

Do not invent viewport baselines, breakpoints, refresh thresholds, metric cutoffs, targets, card counts, or density values. Define the decision or content condition first; map it to an existing product constraint only when supplied or inspected.

Classify the surface using [references/dashboard-models.md](references/dashboard-models.md). A monitoring board, executive scorecard, operational queue, and analytical workspace need different density and interaction.

## 2. Inventory decisions before widgets

Build a compact matrix:

`Decision | Signal | Comparison | Grain | Freshness | Action | Failure cost`

Remove or demote data that does not support a scoped decision, diagnosis, or required reporting obligation. Identify missing context before selecting chart types.

## 3. Create the information architecture

Organize the page in this order when it matches the task:

1. scope and data state;
2. conditions requiring attention;
3. core outcome and comparison;
4. causes or contributing dimensions;
5. records, evidence, and actions.

Use stable regions and consistent reading order. Keep controls near the data they affect. Make global and local filters visually distinct. Preserve active filters, time zone, time range, currency, units, and comparison basis across drilldown.

Do not turn every measure into a card. A compact table or sentence can outperform a chart; a chart can outperform a single number when pattern or comparison matters.

## 4. Select representations

Read [references/visualization-and-metrics.md](references/visualization-and-metrics.md). For each element, state:

- the question it answers;
- why this representation is faster or safer than the alternatives;
- the comparison and baseline;
- encoding, units, precision, labels, and ordering;
- accessible equivalent or data access;
- behavior for missing, partial, stale, or delayed data.

Prefer position and length for precise comparison. Avoid 3D, decorative gauges, unbounded color ramps, and charts whose meaning depends on hover. Use direct labels when practical; do not rely on color alone.

Treat numerical layout values and styling directions as proposals only when the user asks for visual specification and the product system supports them. Otherwise specify hierarchy, constraints, and behavior without arbitrary radii, spacing, or canvas sizes.

## 5. Design interactions and drilldown

Define the path:

`overview -> notice -> compare -> isolate -> inspect -> act -> confirm -> return`

Specify filtering, cross-filtering, sorting, pagination or virtualization, selection, zoom, annotations, saved views, sharing, export, and reset only when the user needs them. Keep the transition from aggregate to record-level evidence reversible and context-preserving.

For operational dashboards, expose ownership, status, age, urgency, and next action. For analytical workspaces, support comparison and hypothesis testing without hiding definitions or silently changing denominators.

## 6. Cover states and constraints

Read [references/interaction-accessibility-qa.md](references/interaction-accessibility-qa.md). Define:

- loading, streaming, stale, partial, empty, no-result, error, permission, and offline states;
- responsive priorities and table/chart adaptation;
- keyboard and screen-reader behavior;
- reduced motion and non-color signals;
- latency feedback and expensive-query behavior;
- data lineage, freshness, and definition access.

## 7. Produce the redesign brief

For a complete input-to-output demonstration, read [references/worked-example.md](references/worked-example.md). Use it to calibrate decision architecture and specification depth; do not reuse its fictional metrics or thresholds.

Return:

### Diagnosis

Name the dashboard type, primary decisions, dominant failure modes, and evidence confidence in no more than five bullets.

### Decision architecture

Provide the decision matrix and proposed section order.

### Component specification

For each region use:

`Purpose | Content | Representation | Interaction | States | Responsive rule | Accessibility`

### Metric and chart rationale

Explain additions, removals, merges, and representation changes. Separate definition questions from visual design.

### Drilldown contract

Describe scope persistence, transition, detail, actions, and return behavior.

### Acceptance criteria

Write observable criteria for comprehension, data correctness, interaction, accessibility, responsiveness, and performance.

### Validation plan

Recommend task-based testing with representative users and real or realistic data. Include success signals such as time to detect, interpretation accuracy, decision confidence, error rate, and action completion. Do not use generic satisfaction as the sole measure.

## Quality bar

- every visible element supports a decision, diagnosis, action, or obligation;
- metrics expose definition, units, scope, comparison, and freshness where material;
- hierarchy follows urgency and task, not visual novelty;
- density reflects expertise and frequency;
- chart choice matches the analytical question;
- filters and drilldowns preserve context;
- missing and stale data cannot masquerade as zero or current;
- accessibility does not depend on a separate simplified dashboard.
