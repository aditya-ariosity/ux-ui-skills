# Visual Craft as Product Communication

## Contents

- Evaluation rule
- Composition and hierarchy
- Typography
- Spacing and layout
- Color, surfaces, and elevation
- Controls, icons, and imagery
- Data-dense and responsive craft
- Validation
- Source basis

## Evaluation rule

Evaluate visual design by whether it makes meaning, priority, relationship, affordance, state, and brand character easier to perceive. Do not equate visual quality with minimalism, more whitespace, large type, card-heavy layouts, gradients, shadows, or current fashion.

Record each visual issue as:

`observed treatment -> misread or extra effort -> affected task -> minimal correction`

Separate:

- **Communication defect:** hierarchy or grouping causes a likely task error or delay.
- **Accessibility failure or risk:** contrast, focus, scaling, motion, or semantics needs measurement or implementation testing.
- **System drift:** repeated values or component treatments diverge without a valid reason.
- **Craft opportunity:** polish may improve confidence or brand expression but no defect is observed.

## Composition and hierarchy

Inspect whether:

- one entry point or priority is legible for the current task;
- scale, position, contrast, and whitespace reinforce the same priority instead of competing;
- related elements share a visible region and unrelated elements have sufficient separation;
- headings describe the content below them and form a coherent outline;
- controls sit near the content they affect;
- alignment creates scan paths and comparison, not decorative rigidity;
- repeated modules have stable anatomy and do not create false equivalence;
- decorative content does not outrank status, data, instructions, or action.

Use blur, squint, grayscale, and rapid-glance checks only as probes. Confirm the inferred reading order with actual users when it is material.

## Typography

Inspect:

- type roles before individual font sizes: display, page title, section title, body, label, metadata, data, code;
- a restrained scale with distinguishable adjacent roles;
- weight, color, and spacing that remain legible at actual rendering sizes;
- line length and line height appropriate to reading density and script;
- numeric alignment, tabular figures, units, signs, decimals, and abbreviations for data-heavy interfaces;
- text resizing, translation expansion, and fallbacks;
- truncation only where the full value remains available and identity is preserved.

Do not solve weak hierarchy by enlarging every heading. Reduce competing emphasis and clarify roles first.

## Spacing and layout

Inspect whether spacing expresses relationships consistently:

- internal spacing binds a component;
- external spacing separates sections or concepts;
- repeated intervals come from a small intentional scale;
- containers exist for structure or interaction, not merely to put everything in cards;
- grids and max widths support reading, comparison, and responsive change;
- dense expert tools preserve scan efficiency and do not inflate row or card height without benefit;
- whitespace is allocated around high-value decisions rather than distributed uniformly.

Avoid prescribing an 8-point grid as universal. Use the active design system or derive a coherent scale from the product's density, platforms, and typography.

## Color, surfaces, and elevation

Inspect whether:

- semantic roles such as text, surface, border, action, focus, success, warning, and danger are distinct;
- brand color is not forced into every interaction or data series;
- color never carries essential meaning alone;
- contrast is measured for relevant text, graphics, boundaries, and focus indicators;
- muted text remains readable and is used for secondary importance, not essential instructions;
- surfaces and elevation communicate containment, overlap, or hierarchy consistently;
- dark, high-contrast, and themed modes preserve semantic meaning;
- status colors do not conflict with chart-series identity.

Treat shadow and border as tools for structure. Do not add both by default.

## Controls, icons, and imagery

Inspect whether:

- controls look interactive and their prominence matches consequence and frequency;
- primary, secondary, tertiary, destructive, selected, and disabled states are distinguishable;
- icon-only actions are familiar in context, labeled accessibly, and explained visually when ambiguity is credible;
- icon families share optical weight, size, stroke, and alignment;
- images clarify content, identity, or brand rather than consume priority without purpose;
- crops, aspect ratios, placeholders, failures, captions, and alt-text intent are specified;
- motion explains change, orientation, or causality and respects reduced-motion preferences.

## Data-dense and responsive craft

- Preserve stable baselines, column alignment, row identity, and visible scope.
- Use compact density deliberately for frequent expert tasks; provide larger targets or alternate layouts for touch.
- Do not rely on hover for values, actions, or explanations.
- Let content determine breakpoints. Define what wraps, truncates, collapses, scrolls, stacks, or becomes another representation.
- Preserve comparison when possible. A single-column mobile layout can destroy the relationship a dashboard or form requires.
- Test zoom, text scaling, long values, empty states, errors, and virtual-keyboard occlusion.

## Validation

Use appropriate checks:

- contrast measurement and grayscale/color-vision simulation;
- keyboard and focus review;
- target and spacing measurement;
- responsive snapshots at content breakpoints and zoom;
- typography checks with long, short, RTL, and non-Latin samples when relevant;
- five-second or first-impression tests for intended priority, without treating preference as usability;
- task testing for labels, grouping, navigation, and action hierarchy.

## Source basis

This reference synthesizes tactical visual-craft guidance from [Refactoring UI](https://refactoringui.com/), interaction patterns from [Designing Interfaces, 3rd Edition](https://www.oreilly.com/library/view/designing-interfaces-3rd/9781492051954/), and research-oriented hierarchy guidance from [NN/g Visual Hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/) and its [Visual Design study guide](https://www.nngroup.com/articles/visual-design-in-ux-study-guide/). Apply [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and platform guidance separately where requirements or conventions apply.

Use [Awwwards](https://www.awwwards.com/), [UX Collective](https://uxdesign.cc/), [Smashing Magazine UX](https://www.smashingmagazine.com/category/ux), and [Growth.Design](https://growth.design/case-studies) for discovery and examples only. Verify claims and test suitability in the product context.
