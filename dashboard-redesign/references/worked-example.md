# Worked Example: Fleet Operations Dashboard

This is a synthetic demonstration of output quality. Its data and thresholds apply only to this example.

## Input

- Product: desktop operations dashboard for a municipal vehicle fleet.
- Primary user: dispatch supervisor monitoring active service vehicles during a shift.
- Decisions: identify vehicles at risk of missing service, understand the cause, assign an intervention, and confirm resolution.
- Supplied definitions: `At risk` means an active route with a predicted delay above the operations-owned threshold; telemetry freshness is available per vehicle; intervention ownership exists in the dispatch system.
- Constraints: dense desktop use, keyboard operation, existing table component, no approved redesign of the prediction model.
- Current artifact: six equal KPI cards, a map, three donut charts, and a paginated vehicle table. Stale telemetry appears as zero speed.

## Output excerpt

### Diagnosis

- The current page behaves like an executive scorecard, but the user needs an operational exception queue.
- Equal KPI emphasis hides the small set of vehicles that require action now.
- Zero speed conflates a real stopped vehicle with missing telemetry, creating a potentially wrong intervention.
- Donut charts show composition but do not help a supervisor compare urgency or select work.

### Decision architecture

| Decision | Signal | Comparison | Grain | Freshness | Action | Failure cost |
|---|---|---|---|---|---|---|
| Which route needs intervention? | Risk state, predicted delay, confidence | Operations-owned threshold and shift target | Route | Per vehicle | Open incident | Missed service |
| Why is it at risk? | Delay contributors, last known location, open incident | Route plan and recent history | Vehicle/route | Per source | Inspect evidence | Wrong diagnosis |
| Who should act? | Owner, status, age, workload | Current dispatch queue | Incident | Live queue | Assign/reassign | Delayed response |

### Proposed section order

1. Scope, shift, source freshness, and degraded-data status.
2. At-risk exception queue ordered by urgency and age.
3. Selected-route evidence: timeline, location, prediction factors, and open incident.
4. Fleet-level comparison for staffing and recurring-pattern analysis.

### Component specification

| Region | Purpose | Content | Representation | Interaction | States | Responsive rule | Accessibility |
|---|---|---|---|---|---|---|---|
| Scope bar | Establish the data universe | Shift, depot, route state, last refresh | Persistent toolbar | Change filters; reset all | Loading, partial, stale | Preserve filters; wrap low-priority metadata | Named controls; status announced |
| Exception queue | Select the next intervention | Route, risk, delay, freshness, incident, owner | Sortable data table | Keyboard row selection; open detail | Empty, no result, partial, permission | Keep identity, risk, age, action; move secondary columns to detail | Headers and sort state exposed; no color-only risk |
| Evidence panel | Diagnose before acting | Timeline, prediction explanation, telemetry status | Detail panel with aligned time series | Compare plan/actual; inspect source | Missing telemetry, model unavailable | Stack below queue when side-by-side space is unavailable | Text summary and data table accompany chart |

### Metric and chart rationale

- Replace three composition donuts with one ordered comparison table because the task is to identify high-risk routes, not estimate parts of a whole.
- Retain fleet totals as secondary context, with definition and scope access. Do not promote them above exceptions.
- Render missing telemetry as `Unavailable - last received 09:42`, never as zero speed.
- Treat the supplied risk threshold as an operational dependency. The redesign does not choose or change it.

### Drilldown contract

`Select route -> preserve shift and depot scope -> inspect delay evidence -> open or assign incident -> receive success/failure -> return to same queue position and selection`

### Acceptance criteria

- Given stale telemetry, the queue shows an unavailable state and last-received time; it never displays a current zero derived from absence.
- When a supervisor returns from an incident, filters, sort, scroll position, and selected route are preserved.
- Every chart has a visible title, units, time scope, and non-chart access to the underlying values.
- Keyboard users can sort, select a route, open its detail, assign an incident, and return without losing context.

### Validation plan

Run representative shift scenarios with real-shaped data: identify the next intervention, explain its evidence, assign it, and recover from stale telemetry. Track interpretation accuracy, time to select the correct route, wrong interventions, and successful context return. Establish targets with operations after a baseline study.
