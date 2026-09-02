# Dashboard Models and Decision Architecture

## Contents

- Model selection
- Decision and metric map
- Metric specification
- Information architecture
- Anti-patterns
- Validation
- Sources

## Model selection

Classify by the user's work, not the stakeholder's label.

| Model | Primary job | Time horizon | Typical interaction | Design priority |
| --- | --- | --- | --- | --- |
| Executive scorecard | judge progress, risk, and intervention need | weekly to quarterly | scan, compare, drill to explanation | targets, variance, trend, accountability |
| Operational monitor | notice a condition and act in time | live to daily | scan, acknowledge, assign, resolve | freshness, exceptions, ownership, recovery |
| Analytical workspace | investigate causes and test hypotheses | ad hoc | filter, compare, segment, inspect | flexible scope, definitions, traceable drilldown |
| Reporting surface | review required results or evidence | fixed cadence | read, export, annotate | completeness, stable definitions, provenance |
| Work queue | prioritize and process records | continuous | sort, filter, select, take action | row identity, status, age, batch action |
| Product home | orient and continue work | session-based | resume, navigate, respond to alerts | state, next action, recency, personalization |
| Public display | maintain shared awareness | live or scheduled | glance from distance | legibility, stability, critical signals only |

A product may combine models. Assign one primary job to each region and avoid giving one screen incompatible density, latency, and interaction expectations.

## Decision and metric map

For each user role, capture:

`Trigger -> Question -> Comparison -> Decision -> Action -> Confirmation`

Then map only the supporting information:

| Field | Meaning |
| --- | --- |
| Decision | The choice, escalation, allocation, investigation, or action the user owns. |
| Signal | The minimum information that indicates attention may be needed. |
| Baseline | Target, prior period, forecast, peer, benchmark, range, or control limit. |
| Grain | Entity, segment, geography, time interval, or cohort represented. |
| Freshness | Last successful update, expected cadence, latency, and stale rule. |
| Evidence | Detail or record required to judge whether the signal is real. |
| Action | Next step, destination, owner, or workflow. |
| Cost of error | Consequence of missing, misreading, or overreacting to the signal. |

Do not optimize for a generic `at-a-glance` experience if the real task requires comparison, investigation, or record-level action.

## Metric specification

Treat each metric as a contract:

- canonical name and plain-language definition;
- numerator, denominator, inclusion, exclusion, and aggregation;
- unit, currency, timezone, and rounding;
- reporting grain and time window;
- source system and accountable owner;
- update cadence, observed timestamp, and stale threshold;
- target, threshold, forecast, or comparison method;
- segment and permission rules;
- known gaps, revisions, lag, and confidence limitations;
- action or decision the metric informs.

Differentiate:

- **Outcome metric:** result for users or business.
- **Driver metric:** behavior or condition believed to influence an outcome.
- **Guardrail metric:** harm, quality, cost, fairness, or reliability constraint.
- **Diagnostic metric:** evidence used to explain variance.
- **Operational status:** state requiring ownership or action; not necessarily a KPI.

Never imply causality merely by placing two metrics together. Label forecasts, estimates, sampled data, and model-generated insights.

## Information architecture

Build from decision hierarchy:

1. **Scope bar:** entity, date range, comparison, filters, timezone, freshness, and data-health status.
2. **Attention layer:** exceptions, breaches, significant change, unresolved work, or critical uncertainty.
3. **Outcome layer:** the few measures needed to judge performance in context.
4. **Explanation layer:** drivers, segments, trends, and contributing dimensions.
5. **Evidence and action:** records, owners, notes, drilldown, export, or workflow controls.

Rules:

- Keep global scope stable and visible.
- Put a local control beside the region it affects.
- Distinguish a view switch from a filter and a filter from configuration.
- Show active scope in plain language and provide a safe reset.
- Preserve scope, scroll, and selection when returning from detail.
- Use progressive disclosure to manage complexity, not to conceal material evidence.
- Let frequent expert work remain dense when scan paths and targets remain usable.

## Anti-patterns

- KPI card walls with no baseline, action, or definition.
- Decorative gauges for values better compared on a common scale.
- Identical card weight for urgent status, secondary context, and navigation.
- A homepage assembled from what each department wanted to display.
- Hidden active filters or different denominators across adjacent metrics.
- `Last updated` that describes page render time rather than data freshness.
- Alerts with no owner, evidence, action, or resolution state.
- Drilldown that changes scope silently or loses the route back.
- Executive simplification that removes the context needed to trust the number.
- Mobile layouts that stack every module but destroy comparison and workflow order.

## Validation

Test with representative decisions and realistic data:

- Can the user state current scope and freshness?
- Can they identify the condition needing attention without prompting?
- Can they explain the comparison and definition correctly?
- Can they reach supporting evidence and take the intended action?
- Can they return without rebuilding scope?
- Do missing, stale, and partial data lead to the correct interpretation?

Measure interpretation accuracy, time to detect, time to act, missed signals, false escalations, filter errors, and recovery—not visual preference alone.

## Sources

- [NN/g: Dashboards and preattentive processing](https://www.nngroup.com/articles/dashboards-preattentive/)
- [NN/g: Choosing chart types in context](https://www.nngroup.com/articles/choosing-chart-types/)
- [Stephen Few, Information Dashboard Design and related library](https://www.perceptualedge.com/library.php)
- [Think Company dashboard guide](https://www.thinkcompany.com/guides/a-guide-to-dashboard-design/)

The books and articles provide frameworks and heuristics. Product data definitions and user evidence remain authoritative for the specific dashboard.
