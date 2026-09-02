# Worked Example: Multi-brand Component Review

This is a synthetic demonstration of output quality. Its inventory applies only to this example.

## Input

- Scope: web Button and TextField across two brands and three products.
- Evidence: token JSON, Storybook, Figma library, component source, 24 sampled product instances, and six recent accessibility issues.
- Supplied authority: code is authoritative for released behavior; semantic tokens are generated from a shared package; Figma should follow the released component version.
- Observed drift: five primary-button colors, three focus treatments, product-level padding overrides, missing error description in one TextField wrapper, and no deprecation path for legacy variants.
- Exclusions: brand identity redesign and native mobile components.

## Output excerpt

### System frame

`Adopted multi-brand web system | Button + TextField | 24 product instances | Code is behavioral authority | Moderate confidence`

### Health summary

| Layer | Health | Strong evidence | Main risk | Confidence |
|---|---|---|---|---|
| Semantic tokens | At risk | Token package and compiled themes | Products bypass semantic aliases | High |
| Component contract | At risk | Source, stories, issue reports | Focus and error semantics differ by wrapper | High |
| Design-code parity | Mixed | Released code and Figma version metadata | Figma exposes retired variants | Moderate |
| Governance | Weak | Contribution notes and release history | No owner or migration path for exceptions | Moderate |

### Systemic finding | Focus behavior is an optional treatment

**Evidence:** The released Button has a focus-visible style, but two product wrappers remove it. Figma documents a separate `Focused` variant, implying focus is a selectable visual state. Four of six sampled keyboard issues involve a missing or clipped focus indicator.

**Product impact:** Keyboard users can lose location across repeated actions. New product teams may reproduce the defect because both design and extension guidance present focus as optional.

**System cause:** The component contract does not define focus as a mandatory interaction state, and wrapper APIs permit style replacement without an invariant check.

**Recommended decision:** Make focus-visible behavior an internal invariant of the primitive. Remove `Focused` as a manually selected Figma variant; document it as an interaction state. Limit wrapper customization to semantic focus tokens and preserve indicator geometry.

**Migration path:** Add visual and keyboard stories, warn on wrapper overrides, migrate the two affected products, then remove the escape hatch in the next breaking release.

**Acceptance criteria:** Every supported Button variant exposes a visible focus indicator in the released component; product wrappers cannot suppress it through documented APIs; Storybook tests exercise focus-visible; Figma usage guidance matches the released state model.

### Token and component plan

| Current | Decision | Target | Migration evidence |
|---|---|---|---|
| Product hex overrides | Deprecate | `action.primary.*` semantic aliases per brand theme | Token lint and product adoption report |
| `Button/Focused` Figma variant | Remove as authored variant | Interaction-state documentation | Figma migration note and parity check |
| TextField wrapper without error relationship | Replace | Shared field contract with description/error slot | Accessibility test and product fixture |
| Legacy dense Button | Retain temporarily | Named density mode with documented scope | Usage owner and removal date |

### Governance sequence

- **Stabilize:** repair TextField error semantics and focus invariants; publish affected-product list.
- **Consolidate:** introduce semantic action tokens and align Figma with released states.
- **Adopt:** ship codemods or mappings, product migration fixtures, and usage reporting.
- **Evolve:** evaluate whether the retained density mode is still a shared need.

### Explicit exception

The second brand may retain a distinct primary color because brand variation is intentional. It may not redefine focus behavior or error semantics because those are shared accessibility and interaction contracts.
