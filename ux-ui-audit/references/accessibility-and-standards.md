# Accessibility and Current Standards

## Contents

- Current baseline
- Evidence rules
- Core test protocol
- Key WCAG 2.2 checks
- Platform touch guidance
- Performance baseline
- Primary sources

## Current baseline

Baseline verified: 2026-08-09.

- Use WCAG 2.2 Level AA as the default web accessibility target. W3C recommends using the latest WCAG 2 version.
- Do not use WCAG 3 drafts as a conformance target.
- WCAG 2.2 removes obsolete Success Criterion 4.1.1 Parsing and adds criteria for focus visibility, dragging alternatives, minimum target size, consistent help, redundant entry, and accessible authentication.
- Apply platform guidance in addition to WCAG where it is stronger or more specific. Keep normative requirements separate from platform recommendations.

When the user asks for current, legal, procurement, or regulated conformance, verify the applicable official standard and jurisdiction at audit time. Never imply that a UX audit is legal advice or a complete accessibility conformance evaluation.

## Evidence rules

- A screenshot can reveal visible risks, structure, copy, and some state problems. It cannot confirm keyboard order, accessible names, roles, values, announcements, focus management, or screen-reader operation.
- Measure contrast from source colors or a reliable rendered sample. Do not estimate by eye.
- Inspect the accessibility tree, DOM, native semantics, or implementation to confirm name, role, state, value, and relationships.
- Test the complete critical task with keyboard and relevant assistive technology when claiming operability.
- Automated tools catch only a subset of barriers. Report automated results as test inputs, not proof of conformance.
- Identify the criterion and exact evidence only for confirmed failures. Label plausible screenshot or implementation concerns as `Risk: needs verification`.

## Core test protocol

Run the applicable checks for the scoped platform and journey:

1. **Keyboard:** complete the task without pointer input; verify logical order, visible focus, no trap, and usable dialogs, menus, grids, and disclosures.
2. **Screen reader:** inspect names, roles, states, values, landmarks, headings, reading order, instructions, errors, and status announcements.
3. **Zoom and reflow:** test text resizing to 200% and web content at a width equivalent to 320 CSS px, commonly 1280 px viewport at 400% zoom; verify no loss or two-dimensional scrolling except legitimate two-dimensional content.
4. **Contrast:** measure text, essential graphics, component boundaries, and focus indicators against relevant adjacent colors.
5. **Target and input:** measure targets, spacing, gesture alternatives, drag alternatives, pointer cancellation, and orientation behavior.
6. **Forms:** verify labels, instructions, grouping, autocomplete, errors, suggestions, redundant entry, persistence, and authentication support.
7. **Media and motion:** check captions, transcripts, controls, autoplay, flashing, animation, vestibular risk, and reduced-motion behavior.
8. **Time and status:** check timeouts, session expiry, progress, asynchronous updates, live regions, interruption, and recovery.
9. **Responsive/mobile:** test text scaling, rotation, virtual keyboard, safe areas, and assistive-service navigation.

Record browser, OS, device or viewport, zoom or text setting, assistive technology, and test path for reproducibility.

## Key WCAG 2.2 checks

Use the full standard for conformance work. The items below are high-frequency audit checks, not a substitute for WCAG.

| Area | Baseline |
| --- | --- |
| Text contrast | At least 4.5:1 for normal text and 3:1 for large-scale text under WCAG 1.4.3, subject to stated exceptions. |
| Non-text contrast | At least 3:1 for visual information required to identify components, states, and essential graphics under WCAG 1.4.11. |
| Color | Do not use color as the only means of conveying information or action under WCAG 1.4.1. |
| Resize text | Text can resize to 200% without loss of content or function under WCAG 1.4.4. |
| Reflow | Content reflows without loss or two-dimensional scrolling at 320 CSS px width for vertically scrolling content, with defined exceptions, under WCAG 1.4.10. |
| Keyboard | All functionality is keyboard operable, focus order is meaningful, and focus is not trapped under WCAG 2.1 and 2.4 criteria. |
| Focus visible | Keyboard focus is visible and not entirely hidden by author-created content under WCAG 2.4.7 and 2.4.11. |
| Dragging | Functionality requiring dragging also has a single-pointer alternative unless exempt under WCAG 2.5.7. |
| Target size | Pointer targets are at least 24 x 24 CSS px or satisfy a documented exception under WCAG 2.5.8. |
| Labels and instructions | Inputs have labels or instructions when needed under WCAG 3.3.2; labels should remain available while entering data. |
| Errors | Errors are identified in text; suggestions are provided when known and appropriate under WCAG 3.3.1 and 3.3.3. |
| Redundant entry | Information already supplied in the same process is auto-populated or selectable unless exempt under WCAG 3.3.7. |
| Authentication | Do not require an unsupported cognitive-function test; support mechanisms such as password managers and paste under WCAG 3.3.8. |
| Name, role, value | Components expose programmatic name, role, state, and value under WCAG 4.1.2. |
| Status messages | Important status changes are programmatically exposed without moving focus under WCAG 4.1.3. |

Do not confuse WCAG 2.5.8's 24 x 24 CSS px minimum with recommended mobile touch sizes.

## Platform touch guidance

- Apple recommends hit targets of at least 44 x 44 points.
- Android recommends touch targets of at least 48 x 48 dp for touch interfaces.
- A visible icon may be smaller when its interactive hit area meets the target guidance and does not collide with adjacent targets.

Use platform units and conventions. Report WCAG minimums as requirements only when the content and conformance context apply; report Apple and Android values as platform recommendations.

## Performance baseline

For implemented web experiences, use current Core Web Vitals only when measured:

- LCP: 2.5 seconds or less;
- INP: 200 milliseconds or less;
- CLS: 0.1 or less;
- evaluate the 75th percentile separately for mobile and desktop when field data is available.

Prefer real-user field data for population-level conclusions. Use lab data to reproduce and diagnose. Connect a performance finding to a user-visible consequence such as delayed primary content, unacknowledged input, unstable layout, or lost state.

## Primary sources

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C WCAG overview and version status](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [W3C: What's New in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)
- [W3C: Understanding Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [Apple Human Interface Guidelines: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility/)
- [Apple UI Design Tips](https://developer.apple.com/design/tips/)
- [Android: Make apps more accessible](https://developer.android.com/guide/topics/ui/accessibility/apps)
- [web.dev Core Web Vitals](https://web.dev/articles/vitals)

If an official source conflicts with this snapshot, follow the official source and disclose the updated criterion in the report.
