# Research and Framework Use

## Contents

- Evidence hierarchy
- Foundational frameworks
- Lightweight validation
- Cognitive and pattern sources
- Current-source rule
- Reference corpus

## Evidence hierarchy

Use the strongest available basis for the claim:

1. observed behavior in the scoped product;
2. measured product or usability evidence;
3. supplied qualitative research, analytics, support, or operational data;
4. current normative standards and applicable platform requirements;
5. relevant peer-reviewed or clearly described empirical research;
6. established heuristics, books, and public design-system precedents;
7. editorial case studies, pattern galleries, and visual inspiration.

Lower tiers can generate questions and design directions. They cannot override direct product evidence or establish a defect by themselves.

## Foundational frameworks

Use these frameworks for their durable contribution, not as complete or current standards:

- **Lean UX, 3rd Edition — Jeff Gothelf and Josh Seiden:** express assumptions as hypotheses, define outcomes before deliverables, collaborate across disciplines, run the smallest useful experiment, and keep discovery inside delivery cycles.
- **Rocket Surgery Made Easy — Steve Krug:** make formative usability testing lightweight, frequent, observable, and connected to immediate fixes. Test important tasks with realistic participants and retest after change.
- **About Face, 4th Edition — Alan Cooper et al.:** model user goals, behaviors, context, and scenarios before selecting interface structures; align controls and system behavior with the user's mental model.
- **Designing Interfaces, 3rd Edition — Jenifer Tidwell, Charles Brewer, and Aynne Valencia:** select patterns by the problem they solve, user context, platform, scale, and tradeoffs rather than copying appearance.
- **Refactoring UI — Adam Wathan and Steve Schoger:** use concrete hierarchy, typography, spacing, color, and component tactics to improve visual communication; validate them against brand, accessibility, content, and task needs.
- **Don't Make Me Think, Revisited — Steve Krug:** make important paths self-evident, support scanning, reduce avoidable interpretation, and use clear labels.
- **The Design of Everyday Things, Revised and Expanded — Don Norman:** align signifiers, mapping, feedback, constraints, conceptual models, and error prevention.
- **Just Enough Research, 2024 Edition — Erika Hall:** begin with the decision and uncertainty, challenge internal assumptions, choose the smallest valid method, and distinguish evidence from organizational preference.

Do not claim that a recommendation appears verbatim in a book unless the supplied source supports that wording. Paraphrase and attribute ideas; never reproduce proprietary text or diagrams.

## Lightweight validation

Define:

`decision -> uncertainty -> participant/evidence -> task or question -> observation -> change -> retest`

- Use small rounds for formative diagnosis, not fixed-sample certainty.
- Recruit by relevant behavior, role, ability, or context rather than demographics alone.
- Test a task and observe behavior; do not ask participants to predict what they would do when direct use is possible.
- Keep the moderator neutral. Ask retrospective probes after behavior rather than leading before it.
- Debrief after each session, separate observation from interpretation, and preserve notable counterevidence.
- Prioritize issues by task impact and recurrence, then make a fix small enough to retest.
- Use larger or statistically planned samples for prevalence, benchmarking, segmentation, or experiment claims.
- Add distinct coverage for materially different roles, accessibility needs, locales, devices, or risk conditions.

The common `five users` rule is a planning heuristic for some formative studies, not a universal sample-size requirement or guarantee of finding a fixed percentage of issues.

## Cognitive and pattern sources

[Laws of UX](https://lawsofux.com/) is a useful index of psychological concepts. Use each law as a question, not a numerical command. Check the original research and context before relying on a specific threshold or memory claim.

[Growth.Design case studies](https://growth.design/case-studies) can reveal onboarding, retention, pricing, consent, and behavioral-design patterns. Treat their causal interpretations as secondary analysis and screen recommendations for manipulation, accessibility, and product ethics.

Public design systems demonstrate one organization's constraints and conventions. Reuse their reasoning where the context matches; do not transplant components or token values blindly.

## Current-source rule

Research snapshot: 2026-08-09.

When a request depends on current conformance, platform behavior, legal obligations, design-system versions, or performance metrics, verify the official source at task time. WCAG 2.2 is the current W3C-recommended WCAG 2 baseline in this snapshot; WCAG 3 remains draft material and is not a conformance target.

## Reference corpus

- [Lean UX, 3rd Edition — O'Reilly](https://www.oreilly.com/library/view/lean-ux-3rd/9781098116293/)
- [Refactoring UI — official site](https://refactoringui.com/)
- [Rocket Surgery Made Easy — ACM catalog record](https://dl.acm.org/doi/abs/10.5555/1805890)
- [About Face, 4th Edition — Wiley](https://www.wiley.com/en-us/About+Face%3A+The+Essentials+of+Interaction+Design%2C+4th+Edition-p-9781118766576)
- [Designing Interfaces, 3rd Edition — O'Reilly](https://www.oreilly.com/library/view/designing-interfaces-3rd/9781492051954/)
- [Just Enough Research, 2024 Edition — Mule Books](https://www.mulebooks.com/just-enough-research)
- [NN/g: 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [NN/g: Lean UX and Agile study guide](https://www.nngroup.com/articles/lean-ux-agile-study-guide/)
- [NN/g: why small iterative usability studies can be useful](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)
- [Digital.gov usability resources](https://digital.gov/topics/usability/)
- [W3C WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
