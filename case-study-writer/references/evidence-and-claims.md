# Evidence and Claim Integrity

## Contents

- Evidence ledger
- Claim classes
- Role and collaboration
- Research evidence
- Outcomes and causality
- Missing evidence
- Confidential work
- Verification pass
- Sources

## Evidence ledger

Build before drafting:

| Claim | Supporting artifact or source | Author's contribution | Team contribution | Evidence strength | Can publish? | Transformation needed |
| --- | --- | --- | --- | --- | --- | --- |

Acceptable inputs include design files, prototypes, research notes, recordings, reports, tickets, analytics, experiment results, launch notes, stakeholder feedback, support themes, implementation links, and the user's explicit account.

Label the source of each fact. Do not merge a remembered estimate, design intention, and measured result into one sentence.

## Claim classes

Use precise verbs:

- **Observed:** directly seen in research, analytics, or product behavior.
- **Measured:** supported by a defined measure, baseline, period, and population.
- **Reported:** stated by a participant, stakeholder, support channel, or team record.
- **Designed:** proposed or specified by the author/team.
- **Tested:** evaluated with named method and scope.
- **Shipped:** implemented and released to a stated audience.
- **Adopted:** used in practice, with the available adoption evidence.
- **Inferred:** a reasoned interpretation that remains uncertain.
- **Planned:** intended next step, not completed work.

Avoid `validated` unless the claim states what evidence was sufficient and what uncertainty remains.

## Role and collaboration

For each phase record:

`Decision or deliverable | Author's action | Collaborators | Decision owner | Implementation owner | Evidence`

Use `I` for direct work and `we` for team decisions. Name collaboration when it explains quality or constraint:

- product defined scope or priority;
- research recruited or moderated;
- engineering shaped feasibility and implemented behavior;
- content, data, accessibility, legal, security, or operations changed the decision;
- the author facilitated, synthesized, designed, tested, specified, or measured.

Do not inflate facilitation into ownership or erase leadership because the work was collaborative. Senior work often appears through framing, tradeoffs, alignment, system decisions, and enabling others—not just screen production.

## Research evidence

For every study state what helps the reader interpret it:

- decision or question;
- method and task;
- participant criteria and sample size;
- prototype or product fidelity;
- main behavior or pattern;
- notable counterevidence or limitation;
- design decision changed by the evidence.

Do not write `users wanted` from one quote. Use participant language carefully and separate observed behavior from expressed preference.

Show only the research artifacts that changed understanding or direction. A persona, journey map, affinity wall, or survey chart earns space when it supports the case—not because a template expects it.

## Outcomes and causality

Record:

`Metric | Baseline | Result | Period | Population | Data source | Other changes | Attribution limit`

Use outcome language proportionate to evidence:

- `Task completion increased from X to Y in a usability study of [scope].`
- `After launch, the metric moved from X to Y over [period]; the release coincided with [other changes], so attribution is directional.`
- `The prototype reduced median completion time in the evaluated tasks; production impact was not measured.`
- `The team adopted the component in N flows, reducing duplicate implementation; user impact remains unmeasured.`
- `The work ended before launch; the strongest result was a validated decision and an implementation-ready direction.`

Never invent a percentage, quote, award, client endorsement, or business result. Do not convert stakeholder approval into user impact.

## Missing evidence

When a material gap exists:

1. request the missing artifact or clarification;
2. narrow the claim;
3. label the limitation;
4. use a learning or measurement plan instead of a result;
5. omit unsupported detail that only makes the story sound complete.

Examples:

- `Analytics were unavailable during the contract, so I measured prototype task success and defined post-launch events.`
- `I no longer have the raw recordings; this theme comes from the final research report and is presented as reported evidence.`
- `The product did not ship. The case study focuses on the decision model, tested prototype, and handoff.`

## Confidential work

Use the least-distorting transformation:

- redact names, identifiers, sensitive values, and proprietary workflows;
- normalize numbers while preserving relationships, and label them as normalized;
- recreate screens with synthetic but structurally equivalent content;
- show cropped decisions or diagrams instead of full product views;
- generalize the organization and domain only as much as necessary;
- obtain permission where required.

Do not imply a recreation is the shipped screen. Do not reveal confidential information through captions, metadata, URLs, filenames, or unblurred background content.

## Verification pass

Before delivery verify:

- every number, date, quote, sample, role, and product status;
- tense matches shipped, tested, proposed, or planned status;
- `I` and `we` accurately attribute work;
- metrics include enough context to avoid a false causal claim;
- captions state what an artifact proves;
- confidential transformations are labeled;
- no generic methodology claim implies work that did not occur;
- limitations do not disappear from the polished summary.

## Sources

- [Just Enough Research, 2024 Edition](https://www.mulebooks.com/just-enough-research)
- [Lean UX, 3rd Edition](https://www.oreilly.com/library/view/lean-ux-3rd/9781098116293/)
- [NN/g: Creating a UX-design portfolio](https://www.nngroup.com/articles/ux-design-portfolios/)
- [NN/g: UX researcher portfolio recommendations](https://www.nngroup.com/articles/ux-researcher-portfolio/)

Use the books and guidance as methods. The user's project evidence is the authority for the case-study claims.
