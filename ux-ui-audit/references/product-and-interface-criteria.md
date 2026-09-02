# Product and Interface Criteria

## Contents

- Task and value clarity
- Information architecture and navigation
- Interaction and state completeness
- Forms and validation
- Content and decision support
- Visual hierarchy and density
- Responsive and adaptive behavior
- Dashboards, tables, and visualization
- Design-system quality
- Trust, consent, and destructive actions
- Perceived performance
- Localization and internationalization

Use these as diagnostic lenses, not a checklist. Apply a criterion only when it affects the scoped user, task, platform, or product outcome.

## Task and value clarity

Inspect whether the experience:

- makes the current task, status, and next meaningful action apparent;
- matches the user's language and mental model;
- reveals required effort, prerequisites, cost, and consequences before commitment;
- prioritizes the primary task without hiding necessary alternatives;
- confirms completion in terms the user cares about;
- avoids forcing account creation, permissions, or data entry before their value is clear.

Flag a problem only when ambiguity changes behavior or increases risk. A screen does not need a prominent call to action when its purpose is monitoring, reading, or expert analysis.

## Information architecture and navigation

Inspect:

- grouping by user goal rather than internal organization;
- labels that predict destination and scope;
- current location, selected state, hierarchy, and back behavior;
- continuity across deep links, refresh, interruption, and return;
- search, filtering, and sorting for large information spaces;
- preservation of user context when moving between overview and detail;
- distinction between navigation, commands, filters, and view switches.

Treat duplicate paths as harmful only when they create conflicting expectations or inconsistent state. Multiple valid entry points can improve efficiency.

## Interaction and state completeness

Inspect every relevant control and system state:

- default, hover, focus, active, selected, disabled, read-only;
- loading, progress, queued, empty, partial, stale, offline;
- error, validation, warning, success, timeout, retry;
- permission denied, expired session, conflict, duplicate action;
- optimistic updates, undo, cancellation, and irreversible completion.

Check that:

- control type matches behavior;
- labels describe the action or resulting state;
- feedback is immediate and proportional to latency;
- repeated submission is prevented where consequential;
- disabled controls are explained when users need to act;
- overlays preserve context, focus, dismissal, and escape routes;
- gestures and drag actions have discoverable alternatives;
- keyboard shortcuts supplement rather than replace accessible controls.

Do not recommend disabling a primary action as the default form-validation strategy when users would benefit from attempting submission and receiving specific errors.

## Forms and validation

Inspect:

- whether each requested field is necessary at this step;
- persistent visible labels, helpful examples, and correct input types;
- required versus optional signaling;
- sensible defaults, autocomplete, and reuse of previously entered data;
- grouping of related inputs and progressive disclosure of conditional fields;
- validation timing that helps without interrupting entry;
- error messages that identify the problem, location, and recovery;
- preservation of input after an error, retry, or session interruption;
- review and confirmation for high-consequence submissions;
- password-manager, paste, and accessible authentication support.

Avoid placeholder-only labels. Avoid clearing valid data after one field fails. Avoid generic errors such as `Invalid input` when a specific correction is known.

## Content and decision support

Inspect whether copy:

- names objects and actions consistently;
- leads with the information needed for the next decision;
- uses specific labels instead of generic `Continue`, `Submit`, or `Learn more` when the result matters;
- distinguishes facts, estimates, recommendations, and uncertainty;
- explains consequences at the point of action;
- uses progressive disclosure for secondary detail without hiding critical terms;
- supports scanning with meaningful headings, lists, and table labels;
- avoids blaming the user for system errors.

Do not shorten text when precision or risk requires detail. Improve structure before removing necessary information.

## Visual hierarchy and density

Inspect whether visual treatment:

- reflects information priority and interaction priority;
- makes related items appear related and distinct items separable;
- uses spacing, alignment, type, color, and position consistently;
- preserves readable line lengths and text scaling;
- differentiates interactive, selected, disabled, and static elements;
- avoids decoration that competes with data or commands;
- keeps controls near the objects they affect;
- provides enough density for the user's frequency and expertise.

Judge hierarchy from the task sequence, not from font size alone. Do not recommend more cards, larger headings, extra whitespace, gradients, shadows, or reduced density without a task-based reason.

## Responsive and adaptive behavior

Inspect at meaningful content breakpoints, not only named devices:

- priority and reading order as width, height, zoom, text size, and orientation change;
- wrapping, truncation, clipping, overlap, and off-screen controls;
- navigation adaptation and persistence of critical actions;
- virtual keyboard, safe-area, sticky header/footer, and browser chrome effects;
- tables, charts, editors, and other two-dimensional content;
- pointer, touch, keyboard, and assistive-input behavior;
- split screen, foldable, tablet, and large-screen layouts when in scope.

Do not require all layouts to collapse to one column. Preserve meaningful comparison and data relationships, with an accessible alternate view when necessary.

## Dashboards, tables, and visualization

Inspect whether the interface supports the user's decisions rather than merely displaying metrics:

- lead with actionable exceptions, change, status, or risk;
- define units, time range, comparison baseline, freshness, and source;
- distinguish filters from configuration and global from local scope;
- preserve context from summary to detail;
- make sorting and active filters visible and reversible;
- support scanning with stable alignment and appropriate numeric formatting;
- keep table headers, row identity, and actions understandable;
- expose chart values and meaning without relying on color or hover alone;
- use the chart type that matches the comparison, trend, distribution, or composition;
- show empty, partial, delayed, and unavailable data honestly.

Do not turn every metric into a card. Do not use a chart when a number or compact table answers the question faster. Do not hide material variance behind averages.

## Design-system quality

Inspect repeated patterns for:

- semantic tokens and consistent component anatomy;
- variant and state coverage;
- accessible defaults and escape hatches for valid exceptions;
- consistent behavior, not merely matching appearance;
- ownership of one-off patterns and documented rationale;
- content rules, responsive rules, and interaction contracts;
- drift between design assets and implemented components.

Distinguish intentional product variation from accidental divergence. Recommend token or component changes only when repetition shows a system-level cause.

## Trust, consent, and destructive actions

Inspect whether the experience:

- explains material cost, data use, renewal, scope, and consequences before commitment;
- presents accept and decline choices with comparable clarity;
- avoids preselection or visual manipulation for consequential choices;
- makes cancellation, export, deletion, and revocation findable and proportionate;
- confirms the object and scope of destructive actions;
- supports undo when technically and ethically appropriate;
- communicates security, privacy, and identity requirements without false reassurance;
- distinguishes reversible settings from irreversible transactions.

Do not reduce necessary friction in high-risk actions. Use confirmation only when it adds information or prevents a credible error.

## Perceived performance

Inspect behavior, then measure when tools are available:

- acknowledge input immediately;
- show progress appropriate to duration and certainty;
- preserve layout to avoid disruptive shifts;
- prioritize meaningful content and primary interaction;
- avoid skeletons that misrepresent final structure;
- allow cancellation or background continuation for long tasks;
- preserve user input and state across retry;
- distinguish loading, empty, stale, and failed states.

Do not diagnose network or rendering performance from a static artifact. Use field data when available; use lab results to reproduce and diagnose, not to claim population-level impact.

## Localization and internationalization

When in scope, inspect:

- expansion, wrapping, truncation, and flexible control widths;
- right-to-left order, mirroring, icon direction, and mixed-direction content;
- local date, time, number, currency, address, name, and plural formats;
- translation-safe concatenation and variable placement;
- fonts and line metrics for target scripts;
- locale switching without loss of task state;
- plain language and culturally dependent metaphors.

Do not assume English length, left-to-right layout, a Gregorian date, or one name/address model.
