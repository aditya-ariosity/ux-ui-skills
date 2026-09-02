# Component and Pattern Contract

## Contents

- Contract schema
- Variants and states
- Behavior and accessibility
- Content and data
- Responsive and composition rules
- Design-code parity
- Testing and evidence
- Sources

## Contract schema

Review each component as a contract:

`Purpose | Anatomy | API/properties | Variants | States | Behavior | Semantics | Content | Responsive | Composition | Tokens | Events | Tests | Status`

Start with the user problem and boundary. A component should represent a reusable interaction or presentation contract, not just a rectangle that appears more than once.

Differentiate:

- **Primitive:** low-level accessible behavior and style building block.
- **Component:** reusable interface object with stable anatomy and API.
- **Pattern:** composition of components for a recurring task or flow.
- **Template:** page-level structure with product content regions.
- **Product exception:** intentional local behavior with an owner and rationale.

## Variants and states

Separate independent axes:

- semantic role or hierarchy;
- size or density;
- content shape;
- interaction mode;
- emphasis;
- validation/status;
- platform or theme.

Avoid boolean-prop explosions and impossible combinations. Define allowed combinations and defaults.

Cover relevant states:

- default, hover, focus, pressed, selected;
- disabled and read-only as different concepts;
- loading, busy, progress, and queued;
- empty, partial, stale, and unavailable data;
- validation error, warning, success, and retry;
- permission, destructive, confirmation, and undo;
- high contrast, reduced motion, touch, and keyboard use.

If a state changes anatomy, behavior, semantics, or data flow substantially, consider a separate component or pattern rather than an overloaded variant.

## Behavior and accessibility

Specify:

- native element or platform control when available;
- keyboard model and shortcuts;
- focus entry, order, trapping, exit, and restoration;
- accessible name, role, state, value, and relationships;
- announcements for errors, status, and asynchronous changes;
- pointer, touch, drag, gesture, and single-pointer alternatives;
- dismissal, escape, outside-click, and back behavior;
- repeat action, optimistic state, cancellation, and recovery;
- reduced motion and animation purpose.

Use the WAI-ARIA Authoring Practices Guide as implementation guidance for custom widgets, not as a substitute for native controls or usability testing. Test the actual component with keyboard and relevant assistive technology.

## Content and data

Define:

- label and action grammar;
- required, optional, and supporting content;
- recommended and hard limits with truncation/wrapping behavior;
- localization, pluralization, number, date, currency, and RTL rules;
- loading, unknown, redacted, and error content;
- empty-state responsibilities;
- icon labels and tooltip use;
- example content using realistic extremes.

Do not make product teams infer content rules from lorem ipsum or a visually balanced sample.

## Responsive and composition rules

Specify invariants and change conditions:

- minimum and maximum size where materially required;
- intrinsic sizing, wrapping, overflow, and aspect ratio;
- container-query or viewport behavior;
- hierarchy and order changes;
- touch and pointer adaptation;
- allowed slots and child components;
- spacing ownership between parent and child;
- nested and adjacent component rules;
- z-index, portal, overlay, and scroll-container behavior.

Avoid baking page layout into a component unless that relationship is part of the reusable contract.

## Design-code parity

Declare authority by property:

| Decision | Suggested authority |
| --- | --- |
| semantic token meaning | canonical token source and governance record |
| runtime behavior and semantics | implemented component plus tests |
| supported design variants | shared component contract reflected in design assets |
| content guidance | versioned documentation owned with the component |
| release status | package or component registry |

The exact authority can differ, but ambiguity must not. Link design components, code components, stories, tokens, and docs using stable identifiers where the tooling permits.

Do not call a component `complete` when design exposes variants code cannot render, code supports hidden states design does not document, or product instances use forked behavior without status.

## Testing and evidence

Use real stories or fixtures for every consequential state. Storybook and equivalent component workbenches can make states executable and support:

- render tests;
- interaction tests;
- accessibility checks;
- visual regression;
- responsive and theme matrices;
- snapshot tests where stable markup adds value.

Automated accessibility checks are inputs, not proof of conformance. Add keyboard, screen-reader, zoom, content-extreme, localization, and product-composition testing.

Record coverage as:

`State or contract | Design example | Code story | Automated test | Manual test | Product instance | Gap`

## Sources

- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [Storybook: writing stories](https://storybook.js.org/docs/writing-stories)
- [Storybook: testing user interfaces](https://storybook.js.org/docs/writing-tests)
- [GOV.UK Design System components](https://design-system.service.gov.uk/components/)
- [USWDS components](https://designsystem.digital.gov/components/)
- [Carbon Design System](https://carbondesignsystem.com/)
- [Adobe Spectrum](https://spectrum.adobe.com/)
- [Fluent 2](https://fluent2.microsoft.design/)
