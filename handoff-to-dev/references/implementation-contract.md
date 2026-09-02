# Implementation Contract

## Contents

- Source and scope
- Screen contract
- Component contract
- Layout and measurement
- Content and data
- Interaction and navigation
- Instrumentation
- Documentation patterns
- Sources

## Source and scope

Declare at the top:

- canonical design/prototype and version;
- target release and platforms;
- design-system package, token, and asset versions;
- approved product decisions and open questions;
- included flows and explicit exclusions;
- content, data, API, permission, privacy, and analytics owners.

The handoff must not create a second hidden source of truth. Link stable artifacts and record the decision version. If design and code disagree, identify the authority by property and resolve the gap.

## Screen contract

For each screen or route specify:

`Purpose | Entry/preconditions | Scope | Regions | Primary action | Navigation | Data | States | Responsive | Accessibility | Events | Exit/completion`

Include:

- route/deep-link and access rule;
- page title, hierarchy, and landmarks;
- global versus local controls;
- retained state on back, refresh, interruption, or return;
- loading and rendering dependencies;
- empty, no-result, partial, stale, error, and permission behavior;
- destructive and irreversible consequences;
- success confirmation and next step.

## Component contract

Use:

`System name | Purpose | Anatomy | Properties | Variants | States | Tokens | Content/data | Behavior | Semantics | Responsive | Events | Tests`

For an existing component, reference its supported contract and specify only the chosen properties or product-level composition. For a new component or variant, document the full contract and route it through the system's contribution process.

Separate:

- variant from state;
- disabled from read-only;
- selected from active/pressed;
- loading from empty;
- validation error from system error;
- visual hierarchy from semantic hierarchy.

## Layout and measurement

State invariants before numbers:

- container and region relationships;
- grid, alignment, and spacing ownership;
- fixed, fluid, intrinsic, minimum, and maximum dimensions;
- wrapping, truncation, clipping, scroll, and overflow;
- aspect ratio and image crop/focal point;
- stacking, layering, portal, and z-index behavior;
- sticky and fixed behavior with browser chrome and safe areas;
- comparison or reading relationships that must remain adjacent.

Use semantic tokens when available. Exact measurements are appropriate for targets, icons, boundaries, fixed controls, and approved system values. Do not redline every gap when auto-layout, CSS layout, or native layout constraints express the rule more accurately.

For each value distinguish:

- system token;
- hard requirement;
- minimum/maximum constraint;
- current proposal;
- implementation-derived value.

## Content and data

Specify realistic bounds:

- content source and owner;
- required, optional, and fallback content;
- label/action grammar;
- minimum, typical, and maximum length;
- multiline, truncation, expansion, and full-value access;
- number, unit, currency, date, timezone, plural, and locale rules;
- zero, null, missing, unknown, redacted, and not-applicable display;
- image and file type, size, ratio, failure, progress, and retry;
- unsafe or user-generated content handling;
- sample fixtures with extremes.

Do not infer backend limits from the visual sample. Mark limits for product/engineering confirmation.

## Interaction and navigation

For each control state:

`Trigger | Preconditions | Immediate feedback | Request/action | Success | Failure | Retry | Cancel | Undo | Focus | Event`

Define:

- pointer, touch, keyboard, and assistive-technology behavior;
- focus entry and restoration for overlays and route changes;
- optimistic versus confirmed update;
- repeat submission and idempotency expectations;
- validation timing and error placement;
- back, escape, outside-click, and browser-refresh behavior;
- unsaved changes and conflicts;
- long-running task progress and background continuation;
- external navigation, new tabs, downloads, and return.

Do not write `standard behavior` when the component, platform, or context leaves an ambiguity.

## Instrumentation

Only specify approved events. Use:

`Event name | Exact trigger | Required properties | Object identity | Success/failure | Consent/privacy | Downstream question | Owner`

Avoid events named after UI implementation when the product needs stable behavioral meaning. Distinguish impression, available, viewed, attempted, submitted, succeeded, failed, cancelled, and reversed.

Do not include sensitive content, free-text prompts, personal data, or generated output in analytics without confirmed policy and necessity.

## Documentation patterns

Prefer:

- one flow diagram for sequence and branches;
- one state matrix for completeness;
- one component table for mapping;
- focused annotations for non-obvious behavior;
- executable stories/fixtures for variants and states;
- Given/When/Then acceptance criteria;
- open-decision log with owners.

Avoid duplicate annotations on every screen. Put shared rules in the component or pattern contract and link to them.

## Sources

- [Storybook: writing component stories](https://storybook.js.org/docs/writing-stories)
- [Storybook: UI testing](https://storybook.js.org/docs/writing-tests)
- [Design Tokens Format Module 2025.10](https://www.designtokens.org/TR/2025.10/format/)
- [GOV.UK Design System components](https://design-system.service.gov.uk/components/)
- [USWDS components and patterns](https://designsystem.digital.gov/components/)

Use public systems as contract examples. Use the product's actual design system, platform, data, and engineering architecture as the implementation authority.
