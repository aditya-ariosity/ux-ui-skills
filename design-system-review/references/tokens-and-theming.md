# Tokens and Theming

## Contents

- Token architecture
- Naming and semantics
- Modes, brands, and themes
- Typography, motion, and layout
- Distribution and interoperability
- Audit method
- Failure patterns
- Sources

## Token architecture

Use layers only when they reduce coupling:

1. **Primitive:** raw palette, dimension, duration, font, opacity, or shadow values. Keep these out of normal product use when a semantic choice exists.
2. **Semantic:** purpose such as `color.text.default`, `color.surface.danger`, `space.container.inline`, or `motion.duration.feedback`.
3. **Component:** a justified component-specific decision that aliases a semantic token, such as `button.primary.background.default`.

Do not require a component layer for every property. Create it when a component needs a stable public contract or must vary independently. Avoid raw values in product code and avoid alias chains so deep that consumers cannot trace the resulting value.

Record for every token:

`Name | Type | Value or alias | Meaning | Modes | Consumers | Status | Replacement | Owner`

## Naming and semantics

Prefer a grammar that expresses intent:

`category.role.emphasis.state.mode`

Adapt the grammar to the organization; do not force every segment into every token.

- Name by purpose, not current appearance: `text.muted`, not `gray.600` at the semantic layer.
- Keep direction-aware roles such as `inline-start` when internationalization matters.
- Separate content, surface, border, focus, icon, and data-visualization color roles.
- Distinguish interactive states from component variants.
- Give danger, warning, success, information, selected, disabled, and focus meanings stable contracts.
- Describe the decision a token represents and where not to use it.
- Use consistent types and units; do not encode unit or hex value into a semantic name.

## Modes, brands, and themes

Model axes explicitly:

- color scheme: light, dark, high contrast;
- brand or product family;
- density or input mode;
- platform;
- locale or writing direction;
- accessibility preference such as reduced motion.

Avoid a combinatorial token set. Separate axes, alias into a resolved theme, and test supported combinations. Define fallback behavior for an unsupported combination.

Check that modes preserve meaning and contrast. A dark theme is not a mechanical inversion; shadows, borders, elevation, status colors, charts, images, and focus treatment may need different decisions.

## Typography, motion, and layout

Typography tokens should distinguish:

- family and fallback;
- size, line height, weight, letter spacing, and decoration;
- semantic text role;
- responsive or platform adaptation;
- numeric and code requirements;
- language/script exceptions.

Motion tokens should distinguish duration, easing, distance, and purpose. Support reduced motion through semantic alternatives, not only zero duration.

Spacing tokens should express a coherent scale while permitting content-driven layout. Do not turn every container width, breakpoint, or intrinsic measurement into a global token. Use tokens for shared decisions; use component constraints for local behavior.

## Distribution and interoperability

Define:

- canonical storage and generated outputs;
- transformation pipeline and validation;
- target platforms and unit conversion;
- versioning and change classification;
- aliases and circular-reference detection;
- generated design-tool variables and code artifacts;
- documentation and ownership;
- deprecation and migration metadata.

The Design Tokens Community Group 2025.10 format is a versioned interoperability specification. It defines exchange structure and types; it does not choose the organization's semantic architecture, naming, governance, or accessibility.

## Audit method

1. Sample actual product values and components.
2. Trace them to code variables, design variables/styles, and token source.
3. Group raw values that serve the same meaning and identical values that serve different meanings.
4. Identify missing semantic decisions before deduplicating.
5. Test modes, brands, states, and product exceptions.
6. Measure contrast and inspect platform output after token resolution.
7. Estimate migration by consumer and dependency, not by token count alone.

Report drift as:

`Observed value -> intended semantic decision -> source mismatch -> product consequence -> migration`

## Failure patterns

- A color palette called a token system.
- Semantic names that leak a specific brand or theme value.
- One token per observed raw value with no meaning.
- A universal `primary` token used for text, action, data, and decoration.
- Component code consuming primitives directly.
- Design variables and code tokens with similar names but different values.
- Accessibility fixed in one theme but broken in another.
- Token renames released as visual changes without a migration map.
- Multiple density modes with no behavioral or target-size contract.
- Breakpoints copied from a framework without testing product content.

## Sources

- [Design Tokens Format Module 2025.10](https://www.designtokens.org/TR/2025.10/format/)
- [Atlassian design tokens](https://atlassian.design/foundations/tokens)
- [USWDS design tokens](https://designsystem.digital.gov/design-tokens/)
- [VA Design System tokens](https://design.va.gov/foundation/design-tokens/)
- [Material Design 3 foundations](https://m3.material.io/foundations)
- [Apple Human Interface Guidelines foundations](https://developer.apple.com/design/human-interface-guidelines/foundations)

Research snapshot: 2026-08-09. Verify current specifications and product-system versions before recommending a migration format.
