# Visualization, Metrics, and Tables

## Contents

- Representation rule
- Question-to-display map
- Quantitative integrity
- KPI cards
- Tables
- Color and annotation
- Accessible data access
- Sources

## Representation rule

Select the lightest representation that answers the user's question accurately:

- sentence for an explanation or status;
- number for one value when comparison is already obvious;
- compact pair or delta for a value and baseline;
- table for lookup, exact comparison, many attributes, or record action;
- chart for pattern, trend, distribution, relationship, or composition;
- map only when spatial position is analytically relevant.

Prefer encodings people compare more accurately, especially common-position and length. Area, angle, volume, color saturation, and animated change make precise comparison harder.

## Question-to-display map

| Question | Preferred starting point | Use carefully |
| --- | --- | --- |
| Change over ordered time | line, area only for magnitude, or compact sparkline plus values | missing periods, uneven intervals, dual axes |
| Compare categories | sorted horizontal or vertical bars | truncated scale, too many categories |
| Rank entities | sorted bars or numeric table | ranks without value difference |
| Part to whole | 100% stacked bar or direct percentages | pie/donut for many or similar slices |
| Distribution | histogram, box plot, strip/dot plot | averages that conceal spread |
| Relationship | scatter plot with appropriate context | implying causality, overplotting |
| Target or range | bullet-style bar, value plus target, control/reference band | decorative speedometers |
| Status over entities | table, dot plot, heatmap with accessible labels | color-only traffic lights |
| Hierarchy and magnitude | treemap only for broad pattern | precise comparison, too many levels |
| Flow between stages | funnel with counts and denominators, or step table | widths that misrepresent loss |
| Geography | map plus ranked table when location matters | mapping categorical values merely because geography exists |

Do not ban a chart type categorically. State the analytical tradeoff and choose based on the task, data shape, audience, and platform capability.

## Quantitative integrity

- Show the baseline and comparison period explicitly.
- Keep units, currency, timezone, and scale visible.
- Use consistent denominators across comparisons or label differences prominently.
- Start bars at zero when length encodes magnitude; disclose justified exceptions for other chart types.
- Represent missing, not applicable, delayed, suppressed, and zero as different states.
- Do not connect gaps in a time series unless interpolation is intended and disclosed.
- Preserve meaningful precision; avoid both false precision and destructive rounding.
- Sort for the task: magnitude, chronology, workflow order, severity, or a stable domain order.
- Label forecasts, confidence intervals, revisions, and model-generated values.
- Show sample size or coverage when it changes interpretation.
- Avoid dual axes unless the relationship is essential, scales are explicit, and misreading risk is controlled.

## KPI cards

Use a card only when the metric merits independent emphasis. A useful KPI block may contain:

`Name | Value | Unit | Comparison | Direction | Time range | Freshness | Definition access | Action`

Rules:

- Do not use green/red without stating whether higher or lower is desirable.
- Do not celebrate a positive delta when the underlying target or quality guardrail is missed.
- Keep the main number visually dominant but not detached from its definition.
- Use a sparkline only when its axis, period, and irregularities remain interpretable.
- Group metrics by decision or outcome, not by equal-sized decorative containers.
- If six cards all look primary, none is primary.

## Tables

Design around four common tasks: find a record, compare records, inspect or edit one record, and take action.

- Keep row identity stable and visually anchored.
- Align numeric values by place value; keep units in headers or values consistently.
- Use meaningful column order and allow user-controlled visibility when datasets are wide.
- Distinguish sort, filter, search, selection, and row action.
- Show the active sort and filter state.
- Keep bulk actions tied to visible selection and preserve it through safe operations.
- Use sticky headers or identifiers only when they do not obscure focus or content.
- Choose pagination, incremental loading, or virtualization based on scale, navigation, browser find, assistive technology, and task continuity.
- Define empty, no-result, partial, loading, error, and permission states.
- Do not place every action in an unlabeled kebab menu when speed or discoverability matters.

## Color and annotation

- Reserve semantic colors for stable meanings.
- Keep category colors distinct from status colors.
- Use direct labels where they reduce legend lookup.
- Reinforce color with text, shape, line style, pattern, position, or iconography.
- Annotate notable events and thresholds only when they explain the decision.
- Keep gridlines and decoration subordinate to data.
- Do not use brand palettes as sequential or categorical scales without checking distinction, contrast, and meaning.

## Accessible data access

Provide equivalent understanding and operation, not merely alt text:

- a concise chart purpose and trend summary;
- clear title, axes, units, legend, and data-source/freshness information;
- accessible name and description;
- keyboard access for interactive controls and data points where feasible;
- programmatic announcements for relevant updates;
- non-hover access to values and explanations;
- a structured data table or other equivalent access when the visualization carries detailed values;
- visible focus, sufficient contrast, reduced-motion support, and reflow or an accessible alternate presentation.

Do not claim accessibility because a library advertises accessible charts. Test the configured output, reading order, keyboard behavior, and assistive-technology experience.

## Sources

- [USWDS data visualization guidance](https://designsystem.digital.gov/components/data-visualizations/)
- [Massachusetts data visualization accessibility](https://www.mass.gov/info-details/data-visualization-accessibility)
- [Microsoft Power BI accessibility guidance](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-accessibility-creating-reports)
- [Tableau accessible dashboards](https://help.tableau.com/current/pro/desktop/en-us/accessibility_dashboards.htm)
- [Carbon data visualization](https://carbondesignsystem.com/data-visualization/getting-started/)
- [NN/g: Data tables and major user tasks](https://www.nngroup.com/articles/data-tables/)
- [Storytelling with Data](https://www.storytellingwithdata.com/)
- [Stephen Few's data-visualization library](https://www.perceptualedge.com/library.php)
