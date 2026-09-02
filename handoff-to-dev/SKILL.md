---
name: handoff-to-dev
description: Convert an approved UX/UI design or prototype into a build-ready behavior, component, responsive, state, accessibility, and acceptance specification. Trigger on "prepare developer handoff", "spec this design", or "write acceptance criteria". Do not use while the product model is still being redesigned or invent backend contracts.
metadata:
  argument-hint: "[approved designs, prototype, system links, and platform constraints]"
---

# Handoff to Development

Handoff is a shared implementation contract, not a measurement dump. Specify intent, behavior, states, constraints, and verification so the team can build the experience without guessing or freezing the design into brittle pixels.

## 1. Confirm readiness

Collect:

- approved flow, screens, prototype, and decision history;
- target platforms, browsers, devices, locales, and input modes;
- design-system components, tokens, code links, and version;
- content source, data shape, ranges, permissions, and latency;
- API or service behavior known to the team;
- accessibility target and test environment;
- analytics plan, release scope, feature flags, and rollout constraints.

Label unresolved product, data, security, privacy, or technical decisions. Do not disguise them as visual annotations.

## 2. Map the critical flow

Write:

`Entry -> Preconditions -> User action -> System response -> Branches -> Recovery -> Completion -> Return`

Include deep link, refresh, back, cancel, interruption, duplicate submission, expired session, and partial completion where relevant. Define what state is retained.

## 3. Map design to system

For every visible region identify:

`Design object | Code component | Variant | Tokens | Content/data | Event | Owner | Gap`

Use existing component and token names. Avoid raw pixel, color, and typography values when semantic tokens or layout constraints exist. Mark new components and variants explicitly; do not silently create one-off implementations.

## 4. Specify component behavior

Read [references/implementation-contract.md](references/implementation-contract.md). Define anatomy, hierarchy, variants, states, interactions, semantics, content limits, responsiveness, and events. State intent and invariants before exact dimensions.

Use measurements for fixed or bounded values only. For flexible layouts, specify container, grid, min/max, wrapping, truncation, overflow, intrinsic sizing, aspect ratio, alignment, and priority.

## 5. Cover all states

Read [references/state-and-responsive-matrix.md](references/state-and-responsive-matrix.md). Include default and consequential states across component, page, data, network, permission, and session levels.

Provide realistic fixtures for long labels, empty data, maximum values, errors, translated content, and slow responses. Do not let `happy path only` designs become an implementation requirement.

## 6. Specify accessibility

Read [references/accessibility-qa-and-acceptance.md](references/accessibility-qa-and-acceptance.md). Define:

- semantic element or platform control;
- accessible name, role, state, value, and relationships;
- heading and landmark structure;
- keyboard model, focus order, focus entry and restoration;
- error identification and status announcements;
- contrast, target, zoom, reflow, text scaling, motion, and touch behavior;
- accessible alternative for charts, drag, gestures, and complex widgets.

Reference relevant WCAG 2.2 criteria for requirements, but do not claim conformance from the specification alone.

## 7. Define telemetry and performance

Only include approved analytics. For each event specify:

`Event | Trigger | Properties | Object ID | Success/failure | Privacy note | Owner`

Define user-visible performance behavior: immediate acknowledgment, loading strategy, cancellation, optimistic update, timeout, retry, state preservation, and layout stability. Add numeric budgets only when product or engineering owns them.

## 8. Write acceptance criteria

Use observable Given/When/Then statements or an equally testable format. Cover behavior, data, states, responsiveness, accessibility, instrumentation, and recovery. Avoid `matches design`, `looks correct`, or `works on mobile` as acceptance criteria.

## 9. Produce the handoff package

For a complete input-to-output demonstration, read [references/worked-example.md](references/worked-example.md). Use it to calibrate behavior-first detail, flexible layout rules, states, and acceptance criteria; do not reuse its fictional system names or API assumptions.

### Scope and dependencies

State included flows, platforms, feature flags, system versions, dependencies, and exclusions.

### Flow contract

Provide transitions, branches, state retention, and recovery.

### Screen and component specs

Use:

`Purpose | System mapping | Anatomy | Content/data | Behavior | States | Responsive | Accessibility | Events`

### State matrix

Include ownership and required fixtures.

### Acceptance criteria

Group by feature behavior, accessibility, responsiveness, data integrity, and resilience.

### Open decisions

Use:

`Question | Why it matters | Decision owner | Blocking? | Needed by`

### Design QA plan

Name environments, viewports, content fixtures, assistive technologies, browsers, and high-risk checks. Record deviations as defects, approved tradeoffs, or design changes.

## Quality bar

- the critical flow can be implemented without inferring hidden branches;
- system components and tokens are named, not approximated;
- content and data ranges shape the layout contract;
- loading, empty, error, permission, and recovery states are specified;
- responsive behavior uses constraints and priority, not device screenshots alone;
- accessibility semantics and focus behavior are explicit;
- acceptance criteria are observable;
- unresolved decisions have owners and do not masquerade as implementation detail.
