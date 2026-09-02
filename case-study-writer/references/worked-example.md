# Worked Example: Public Library Search Case Study

This is a synthetic demonstration of output quality. Its project facts apply only to this example.

## Input

- Target: hiring-manager portfolio page for a senior product designer.
- Project: redesign of a regional public-library catalog search.
- Author's role: lead product designer for discovery, interaction design, prototype testing, and design QA; a researcher planned and moderated the study; engineers owned technical implementation.
- Evidence supplied: six moderated task sessions, search-query logs, support categories, two prototype rounds, launch notes, and a post-launch directional change in search reformulation. Exact business metrics are confidential.
- Supported finding: participants interpreted unavailable-format filters as active inventory and repeatedly reached dead ends.
- Decision: move availability into result context and preserve format as a preference, with clear branch behavior.
- Constraint: legacy catalog API and shared government design system.

## Output excerpt

### Project card

`Reduced a recurring catalog-search dead end | Lead product designer | Research, product, engineering | Responsive web | Shipped`

### Executive summary

Library patrons were using format filters to find items they could borrow now, but the catalog treated format and availability as separate ideas. In six supplied task sessions, this mismatch repeatedly led to result pages with no actionable item. I led discovery synthesis, interaction design, two prototype rounds, and design QA, working with a researcher who planned and moderated the study and engineers who owned implementation. We moved availability into each result's decision context and kept format as a preference, while accounting for a legacy API that could not guarantee live inventory. The shipped product showed a directional reduction in reformulated searches; the exact metric is confidential and cannot establish causality on its own.

### What changed in our understanding

The initial brief framed the problem as weak filter discoverability. Evidence changed the diagnosis: people could find the controls, but the product's information model did not match the borrowing decision. Improving the filter styling would have made the wrong model easier to use.

### Evidence to decision

| Evidence | Interpretation | Decision | Tradeoff |
|---|---|---|---|
| Participants selected format, then expected borrowable results | Format was acting as a proxy for availability | Show branch-level availability in result context | More result density |
| Legacy API inventory could be delayed | A definitive `Available now` claim could become false | Show source time and branch status language approved by content | Less concise labels |
| Patrons returned to the same query after a dead end | Search intent was still valid | Preserve query and filters when changing branch | More state management |

### Iteration excerpt

**Round one:** Added availability as another top-level filter. Participants still had to predict which branch held inventory and could remove all results.

**Round two:** Kept format as a preference, placed branch availability and source time on each result, and allowed branch changes without clearing the query. Participants could explain why an item was or was not actionable before opening its detail.

### My contribution

I synthesized the research and behavioral logs into the revised problem statement, modeled the format/availability relationship, designed and prototyped both rounds, documented the legacy-data tradeoff, and partnered with engineering during design QA. The researcher owned study planning and moderation; product and library operations approved policy and content decisions.

### Outcome

The redesign shipped across the regional catalog. Available post-launch data showed a directional reduction in repeated query reformulation, while support continued monitoring availability confusion. Because the exact metric is confidential and other launch changes occurred, the case study presents this as a signal rather than proof of causal impact.

### Visual plan

| Placement | Artifact | Claim proved | Caption |
|---|---|---|---|
| First screen | Before/after result decision area | Information model changed, not just styling | Format became a preference; branch availability became decision context |
| Problem section | Anonymized task path | Users reached a predictable dead end | Repeated path observed in supplied sessions |
| Iteration section | Round-one and round-two prototypes | First solution did not resolve the model mismatch | Why another filter was insufficient |
| Outcome section | Redacted trend shape with method note | Post-launch signal existed but is limited | Directional, confidential, and non-causal |

### 30-second version

I led the redesign of a public-library catalog where patrons could find filters but still could not tell what they could borrow. Research showed that format and availability were modeled separately even though users treated them as one decision. I redesigned the result context, preserved search state across branch changes, and worked within delayed inventory data. The product shipped and showed a directional reduction in repeated reformulation, which I present cautiously because the exact data is confidential and other changes launched at the same time.
