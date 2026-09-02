# Dashboard Interaction, Accessibility, and QA

## Contents

- Scope and filters
- Drilldown and action
- State model
- Responsive behavior
- Accessibility protocol
- Platform constraints
- Validation and acceptance
- Sources

## Scope and filters

For every filter define:

`Scope | Default | Values | Dependency | Apply model | Persistence | Empty behavior | Reset | URL/share behavior`

- Make global and local scope visually distinct.
- Reveal active scope without requiring a menu to be opened.
- Use immediate apply only when queries are fast, changes are reversible, and intermediate combinations are valid.
- Use explicit apply for expensive, multi-filter, or consequential queries; show pending changes.
- Preserve filters when the user visits detail and returns.
- Make reset predictable: reset one control, a region, or the full view explicitly.
- Expose unavailable or permission-limited values without implying zero.
- Keep date ranges, timezones, and comparison periods logically coupled.

## Drilldown and action

Specify:

`Trigger -> new scope -> retained context -> detail evidence -> action -> confirmation -> route back`

- Use the entire chart mark as a target only when selection is unambiguous and an alternate interaction exists.
- Show whether selecting a mark filters the page, opens details, navigates, or takes action.
- Keep breadcrumbs, titles, filter summaries, or selected entities sufficient for orientation.
- Preserve selections and scroll where useful.
- Provide a record-level path from an aggregate alert when action depends on evidence.
- Separate exploratory selection from consequential action.
- Confirm completion in domain language and update the originating view without silent inconsistency.

## State model

Define separately:

- initial load;
- incremental or streaming update;
- refresh in progress with existing data;
- stale but available data;
- partial source failure;
- true zero or valid empty state;
- no results caused by filters;
- delayed or suppressed data;
- permission-limited data;
- query error, timeout, and retry;
- offline or disconnected state;
- optimistic action, success, conflict, and rollback.

Never replace existing trusted data with a blank skeleton during routine refresh. Retain the prior timestamp and mark data as updating or stale.

## Responsive behavior

Define change by information priority and available space:

- scope controls that condense but remain inspectable;
- comparisons that must stay adjacent;
- charts that simplify labels, change orientation, or become another representation;
- tables that preserve row identity with horizontal scroll, column priority, or a task-specific detail view;
- actions that remain reachable above the virtual keyboard and safe areas;
- touch targets that meet platform guidance without forcing desktop density everywhere;
- large-display dashboards that remain legible at viewing distance and do not use hover.

Do not promise feature parity through visual stacking alone. State which analytical relationships and actions must survive each layout.

## Accessibility protocol

Use WCAG 2.2 AA as the default web baseline when applicable. Verify:

- meaningful headings, landmarks, and reading order;
- keyboard access, visible focus, logical focus movement, and no traps;
- accessible names, roles, states, values, and relationships;
- screen-reader access to scope, metric definitions, chart purpose, values, and updates;
- no color-only or hover-only information;
- text and essential graphics contrast;
- zoom, reflow, text scaling, and large-value wrapping;
- target size, drag alternatives, and touch behavior;
- status announcements for refresh, filter application, errors, and saved changes;
- equivalent data access for complex visualizations;
- reduced motion and controllable animation.

Label screenshot-only concerns as risks. A static visual cannot confirm semantics or keyboard behavior.

## Platform constraints

When the dashboard runs in Power BI, Tableau, another BI platform, or an internal chart library:

- inventory supported visuals, custom visuals, interaction limitations, export behavior, focus order, and accessible alternatives;
- distinguish a platform limitation from a design decision;
- avoid specifying unsupported chart or layout behavior as if it were immediately buildable;
- use the strongest native accessible feature before adding a custom visual;
- record where a companion table, page, or workflow is required;
- test the published and embedded experience, not only the authoring canvas.

## Validation and acceptance

Use realistic fixtures: long labels, maximum values, negative values, missing points, dense series, zero results, stale data, and permission gaps.

Sample acceptance criteria:

- The visible scope summary updates whenever a global filter is applied and persists through drilldown and browser back.
- A stale source displays its last successful timestamp and cannot be mistaken for current data.
- Every chart exposes its purpose, units, comparison, and equivalent detailed values without hover-only interaction.
- Keyboard users can apply, inspect, reset, and leave every dashboard control in a logical order.
- Returning from a record preserves the prior filter, selection, and scroll context unless the action changes the dataset.

## Sources

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [Power BI report accessibility](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-accessibility-creating-reports)
- [Tableau dashboard accessibility](https://help.tableau.com/current/pro/desktop/en-us/accessibility_dashboards.htm)
- [USWDS data visualizations](https://designsystem.digital.gov/components/data-visualizations/)

Research snapshot: 2026-08-09. Verify current platform features and official standards when version-specific or compliance-sensitive.
