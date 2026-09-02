# Accessibility, Design QA, and Acceptance

## Contents

- Accessibility specification
- WCAG 2.2 high-frequency requirements
- Test protocol
- Acceptance-criteria grammar
- Design QA workflow
- Deviation handling
- Sources

## Accessibility specification

For each interactive pattern define:

`Native element/control | Name | Role | State/value | Relationships | Keyboard model | Focus | Announcement | Pointer/touch | Alternate interaction`

For each page define:

- title, language, headings, landmarks, and reading order;
- skip/bypass mechanism where needed;
- focus on entry, route change, errors, overlays, and completion;
- visible instructions and programmatic relationships;
- error summary, inline error, and correction behavior;
- status and asynchronous announcement strategy;
- media, animation, timeout, and session behavior;
- zoom, reflow, text scaling, orientation, and input modes.

Prefer native HTML or platform controls. If a custom widget is required, follow a suitable WAI-ARIA/APG keyboard and semantics pattern and test the implemented output.

## WCAG 2.2 high-frequency requirements

Use the full standard for conformance work. Common handoff items include:

- text contrast and non-text contrast;
- color not used as the only cue;
- text resize and content reflow;
- keyboard operability, order, no trap, and visible focus;
- focus not obscured by author-created content;
- alternatives to dragging;
- minimum pointer-target size or documented exception;
- labels, instructions, error identification, and suggestions;
- redundant entry reduction;
- accessible authentication;
- programmatic name, role, state, value, and status messages.

Do not mix the WCAG 24 by 24 CSS-pixel minimum target criterion with stronger platform touch guidance such as Apple's 44 by 44 points or Android's 48 by 48 dp. Specify which baseline applies.

WCAG 3 material is draft and is not the conformance target in this research snapshot.

## Test protocol

Record environment and path. Test:

1. keyboard-only critical flow;
2. screen reader on target browser/platform;
3. browser zoom and text resize/reflow;
4. contrast from resolved colors and rendered states;
5. touch targets, gestures, drag alternatives, and pointer cancellation;
6. labels, autocomplete, validation, error recovery, and authentication;
7. captions, transcripts, motion, reduced motion, flashing, and autoplay;
8. timeouts, progress, live updates, interruption, and retry;
9. responsive layout, orientation, safe areas, and virtual keyboard;
10. high-contrast mode and platform text-scaling settings where relevant.

Automated checks and design plugins catch only a subset of barriers. Do not sign off from an automated report alone.

## Acceptance-criteria grammar

Use Given/When/Then or direct observable statements.

Strong:

- `Given validation errors after submit, focus moves to the error summary; each summary link focuses the invalid control; valid inputs remain unchanged.`
- `When the modal closes by Save, Cancel, Escape, or the supported outside action, focus returns to the control that opened it unless that control no longer exists.`
- `At 400% browser zoom in the agreed desktop test viewport, content reflows without loss or two-dimensional scrolling except the specified data table.`
- `When background processing completes without moving focus, the status is announced once and the resulting action becomes keyboard reachable.`

Weak:

- `Accessible.`
- `Passes WCAG.`
- `Matches Figma.`
- `Works with screen readers.`
- `Responsive on all devices.`

Each criterion should identify trigger, observable behavior, retained state, and recovery when relevant.

## Design QA workflow

1. Confirm build/version, environment, scope, and source design.
2. Test the critical flow with realistic fixtures before pixel comparison.
3. Compare behavior, content, state, accessibility, responsiveness, and then visual craft.
4. Record evidence with route, state, viewport/device, browser/OS, and reproduction steps.
5. Classify the result as defect, design change, approved technical tradeoff, content/data issue, or open decision.
6. Assign owner and acceptance criterion.
7. Recheck the fix and relevant regression surface.

Prioritize blocked tasks, data loss, privacy/safety, accessibility barriers, and broken state/recovery above small visual drift.

## Deviation handling

Use:

`Expected contract | Implemented behavior | Evidence | User impact | Cause | Decision | Owner | Follow-up`

Do not ask engineering to reproduce an impossible design. If implementation evidence reveals a better constraint, update the canonical design and contract. If a deviation creates user harm or breaks a requirement, do not normalize it as a design update merely because it shipped.

## Sources

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C: What's New in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [Apple HIG accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Android accessibility guidance](https://developer.android.com/guide/topics/ui/accessibility/apps)
- [Storybook UI testing](https://storybook.js.org/docs/writing-tests)

Research snapshot: 2026-08-09. Verify official standards, platform requirements, assistive-technology behavior, and browser support for current or regulated work.
