# State and Responsive Matrix

## Contents

- State taxonomy
- State specification
- Responsive contract
- Complex content
- Input and platform adaptation
- Test fixtures
- Acceptance patterns

## State taxonomy

Cover the relevant layers independently.

### Component

- default, hover, focus, pressed, selected;
- disabled and read-only;
- loading, busy, progress;
- valid, warning, error, success;
- expanded, collapsed, open, closed;
- drag target, drop accepted/rejected;
- destructive pending and undo.

### Page and task

- first use and returning use;
- no data and no results;
- draft, partially complete, unsaved;
- complete, archived, expired;
- blocked by prerequisite;
- interrupted and resumed;
- concurrent edit or conflict.

### Data and service

- initial loading;
- background refresh;
- stale but available;
- partial source success;
- delayed, suppressed, redacted, and unknown;
- timeout, rate limit, offline;
- request failure and retry;
- optimistic success, server rejection, rollback.

### Identity and permission

- signed out, expired session;
- permission missing or revoked;
- role-limited content;
- record unavailable versus nonexistent;
- consent required or withdrawn.

Do not use one generic empty state for valid zero, filters with no match, missing data, permission limits, and source failure.

## State specification

For each state use:

| Field | Requirement |
| --- | --- |
| Trigger | Exact condition that enters the state. |
| User need | What the user must understand or do. |
| Visible response | Content, control, data, and layout. |
| Programmatic response | Semantics, focus, and announcement. |
| Available actions | Retry, edit, cancel, navigate, request access, undo. |
| Retained data | Inputs, selection, scroll, draft, or previous result. |
| Exit | Success, failure, timeout, user action, or system event. |
| Analytics | Approved state or action event, if any. |

Define precedence when states overlap, such as stale data during refresh plus a partial source failure.

## Responsive contract

Do not hand off a desktop, tablet, and mobile screenshot as the complete rule. For every region define:

`Priority | Invariant | Width/content trigger | Layout change | Order | Size rule | Overflow | Alternate representation | Input adaptation`

Base changes on content and task constraints. Named device sizes are test points, not the source of truth.

Specify:

- navigation transformation and state preservation;
- region order and whether comparison must remain side by side;
- container, columns, gaps, min/max, wrapping, and intrinsic size;
- text growth and localization;
- sticky/fixed elements with safe areas and virtual keyboard;
- pointer, touch, keyboard, and hover capability;
- portrait, landscape, split-screen, and large-display behavior when in scope;
- zoom and reflow expectations;
- performance implications of hidden versus unrendered content.

## Complex content

### Tables

Choose and specify one or a combination:

- horizontal scroll with sticky identity column;
- prioritized columns with user-controlled reveal;
- task-specific row detail;
- stacked record cards only when comparison is not the primary task;
- responsive summary plus full table access;
- server-side sorting/filtering/pagination or virtualization.

State keyboard, screen-reader, focus, and selected-row behavior. Do not collapse a comparison table into cards automatically.

### Charts

Define label reduction, orientation change, aggregation, scrolling, aspect ratio, interaction, tooltip alternative, and equivalent data access. Do not shrink until labels or targets become unusable.

### Forms

Define field order, grouping, conditional regions, multi-column collapse, action placement, error summary, virtual-keyboard behavior, saved progress, and long-label expansion.

### Overlays

Define when a modal remains a modal, becomes full-screen, turns into a drawer, or should become a route. Preserve focus and back behavior across adaptations.

## Input and platform adaptation

- Do not rely on hover for essential information or action.
- Enlarge the interactive hit area without necessarily enlarging the visible icon.
- Provide alternatives to drag and complex gestures.
- Let keyboard shortcuts supplement visible controls.
- Preserve platform conventions for navigation, menus, dialogs, selection, and system back.
- Specify text scaling, dynamic type, reduced motion, high contrast, and orientation behavior.
- Distinguish CSS pixels, platform points/dp, device pixels, and design-tool coordinates.

## Test fixtures

Include:

- shortest and longest labels;
- translated strings and RTL where relevant;
- maximum, minimum, negative, and high-precision values;
- no image, broken image, slow image, extreme aspect ratio;
- one, many, and zero records;
- loading, stale, partial, offline, and error responses;
- permission-denied and expired-session branches;
- 200% text resize and 400% browser zoom/reflow for web where applicable;
- virtual keyboard open;
- touch-only, keyboard-only, and screen-reader operation;
- reduced motion and high contrast.

## Acceptance patterns

- At widths where the action row no longer fits without overlap, secondary actions move into the named overflow while the primary action and status remain visible.
- At 200% text resize, labels wrap without clipping and the control remains associated with its full label.
- When a refresh fails but prior data exists, the prior data remains visible with its timestamp and an error/retry status; it is not replaced by an empty state.
- When the virtual keyboard opens, the focused field, its error, and the task action remain reachable without trapping the user.
- When a table exceeds the available width, row identity and active selection remain understandable while the user accesses additional columns.

Research basis: [WCAG 2.2 reflow and resize requirements](https://www.w3.org/TR/WCAG22/), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [Material Design 3](https://m3.material.io/), and executable state practices in [Storybook](https://storybook.js.org/docs/writing-stories).
