# Story and Editorial Architecture

## Contents

- Audience model
- Narrative spine
- Section architecture
- Decision writing
- Visual storytelling
- Scannability and pacing
- Alternate formats
- Editing rules
- Sources

## Audience model

Design the case study for a decision the reader is making:

| Reader | First question | Strong evidence |
| --- | --- | --- |
| Recruiter | Is this relevant and understandable? | role, domain, scope, outcome, scannable craft |
| Design manager | How does this person frame and decide? | evidence, tradeoffs, iteration, role, reflection |
| Senior design panel | Can they handle ambiguity and systems? | constraints, alternative models, cross-functional influence, consequences |
| Craft reviewer | Is the interaction and visual execution strong? | behavior, states, design rationale, implementation quality |
| Product/engineering partner | Can they collaborate and ship? | shared decisions, feasibility, handoff, outcome, learning |

Use one primary audience and role target. Do not bury the core evidence to satisfy every possible reviewer.

## Narrative spine

Use:

`Context -> Tension -> Evidence -> Decision -> Change -> Outcome -> Learning`

- **Context:** who, what product, why now, and the author's remit.
- **Tension:** a real uncertainty, conflict, failure, risk, or constraint.
- **Evidence:** the observation or data that changed understanding.
- **Decision:** the pivotal choice and rejected alternative.
- **Change:** the behavior, structure, system, or workflow designed.
- **Outcome:** the strongest supported result.
- **Learning:** how evidence changed judgment or what remains unresolved.

Avoid a chronological `empathize, define, ideate, prototype, test` diary unless chronology itself explains the decision.

## Section architecture

Use only sections that advance the story.

### Opening screen

- project title in outcome or task language;
- one-sentence problem and result;
- role, team, duration, platform, and status;
- one representative final or before/after visual;
- a short statement of the author's contribution.

### Context and stakes

Explain the workflow, user, product/business stakes, and starting evidence. Avoid company history that does not affect the project.

### Role and constraints

State ownership, collaborators, timeframe, technical/platform limits, data/research access, and scope boundaries.

### Evidence and reframing

Show the few observations that changed the problem model. Connect each insight to a decision.

### Decisions and tradeoffs

For one to three pivotal choices use:

`We considered -> evidence/constraint -> chose -> gave up -> protected -> how we tested`

### Designed change

Explain flow, information architecture, system behavior, states, responsive behavior, and visual hierarchy in task order. Do not present a gallery without behavior.

### Outcome and reflection

State supported results, attribution limits, what remained unresolved, and the most credible next step.

## Decision writing

Use concrete causal sentences:

- `Because supervisors acted on exceptions rather than totals, I replaced the equal-weight KPI grid with an exception queue and a scoped trend view.`
- `Testing showed that the label was interpreted as a status, so we changed both the language and control type rather than styling the same interaction.`
- `The custom chart improved visual novelty but made exact comparison slower; we selected a sorted table with inline variance instead.`

Avoid unnamed best practices as rationale. Explain the user evidence, system constraint, or product principle that made a direction appropriate.

## Visual storytelling

Every visual needs a job:

| Artifact | Useful when | Caption pattern |
| --- | --- | --- |
| before/after | a specific behavior or hierarchy changed | `Changed X so Y could do Z; evidence was ...` |
| journey/flow | sequence, handoff, or recovery was the problem | `The former break occurred at ...; the new route preserves ...` |
| research excerpt | behavior changed the decision | `In [method/scope], participants ...; this led to ...` |
| alternatives | tradeoff shows judgment | `Direction A optimized ...; we chose B because ...` |
| annotated state | interaction details matter | `This state prevents/communicates ...` |
| outcome chart | a measured result needs context | `Metric, baseline, result, period, and attribution note` |

Crop aggressively around the evidence. Use arrows, labels, and sequence numbers sparingly. Keep source text readable. Provide alt text or equivalent descriptions in the final portfolio.

## Scannability and pacing

- Put the answer before the explanation.
- Use informative headings that state the decision or consequence.
- Keep paragraphs focused on one point.
- Alternate concise text with evidence-rich visuals.
- Use summary tables for role, constraints, and outcomes.
- Keep captions substantive enough to survive a fast scan.
- Repeat a key result only when the format changes, not throughout every section.
- Avoid process illustrations that take more space than the insight they support.

## Alternate formats

### 30-second summary

`User/problem | Author's role | Pivotal decision | Supported result`

### Five-minute walkthrough

1. context and role;
2. tension and evidence;
3. two key decisions;
4. final behavior;
5. outcome and learning.

### Interview deck

Use one claim per slide, large evidence, and speaker notes for detail. Plan branches for craft, research, collaboration, technical tradeoffs, and outcome questions.

### Application excerpt

Lead with relevance to the role, one decision, and one supported result. Link to the fuller evidence where allowed.

## Editing rules

- Remove generic claims such as `intuitive`, `seamless`, `innovative`, and `user-friendly` unless evidence defines them.
- Replace passive voice when it hides ownership.
- Cut tools lists unless the tool changed the method or constraint.
- Cut every artifact that does not prove a claim.
- Keep one consistent product name, user label, metric name, and tense.
- Explain acronyms on first use.
- Preserve the author's natural voice; do not make every portfolio sound like a consultancy pitch.
- Do not imitate proprietary case-study wording or reproduce book text.

## Sources

- [NN/g: 5 Steps to Creating a UX-Design Portfolio](https://www.nngroup.com/articles/ux-design-portfolios/)
- [NN/g: Creating a UX portfolio case study](https://www.nngroup.com/videos/ux-design-portfolio-case-study/)
- [Articulating Design Decisions, 2nd Edition](https://www.oreilly.com/library/view/articulating-design-decisions/9781492079217/)
- [Storytelling with Data](https://www.storytellingwithdata.com/)
- [Just Enough Research, 2024 Edition](https://www.mulebooks.com/just-enough-research)

Research snapshot: 2026-08-09. Portfolio conventions change; use current hiring evidence when the user targets a specific company, market, or format.
