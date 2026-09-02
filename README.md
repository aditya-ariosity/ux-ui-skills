# UX/UI Design Skills

This repository contains six stable Codex/ChatGPT skills for evidence-led professional product-design work, plus one experimental end-to-end foundation.

## Stable skills

- `ux-ui-audit`: Reviews screens for hierarchy, usability, accessibility, layout, information architecture, responsive behavior, trust, states, and prioritised improvements.
- `dashboard-redesign`: Improves dashboards, KPI cards, charts, filters, density, drilldowns, comparison, data trust, responsiveness, and accessibility.
- `design-system-review`: Reviews components, tokens, spacing, typography, color, variants, states, documentation, design-code parity, and governance.
- `ai-product-design`: Designs AI features, chatbots, agents, copilots, trust flows, feedback loops, approvals, recovery, memory, permissions, and evaluation.
- `case-study-writer`: Converts product design work into concise, credible UX/UI portfolio case studies without inventing metrics or ownership.
- `handoff-to-dev`: Produces build-ready specs, annotations, acceptance criteria, responsive behavior, accessibility requirements, state matrices, and QA criteria.

Each stable skill includes a realistic input-to-output example. The examples demonstrate evidence strength, decision quality, output density, and what the skill must leave unresolved.

## Experimental

`product-design` is an explicit-invocation foundation for end-to-end research, product framing, experience modeling, visual direction, creation, and rendered validation. It includes a project-context schema, governed JSONL knowledge records, dependency-free retrieval, anonymized benchmarks, and executable tests. Its seed corpus is deliberately small and it is not yet positioned as a production replacement for the six specialist skills.

## Who this is for

These skills are for designers, product teams, and engineers who need defensible reasoning, accurate standards interpretation, explicit uncertainty, and testable design decisions. They favor professional audit, specification, and decision quality over instant decorative output.

The pack does not silently invent breakpoints, density values, metric thresholds, policies, or research. When the task needs numbers, it uses supplied system values, inspected implementation constraints, or clearly labeled proposals with an owner and validation method. This rigor can produce more open questions than a template-driven generator; that is intentional when false precision would mislead the team.

The stable skills do not promise stack-specific production code. Use them to decide and specify the experience; pair the output with the target implementation workflow when code is requested.

## Structure

```text
ux-ui-skills/
  product-design/
  ai-product-design/
  case-study-writer/
  dashboard-redesign/
  design-system-review/
  handoff-to-dev/
  ux-ui-audit/
```

## Notes

These skills synthesize established UX/UI practice from sources such as WCAG, NN/g, Lean UX, Refactoring UI, Rocket Surgery Made Easy, About Face, Designing Interfaces, Laws of UX, Growth.Design, Smashing Magazine, UX Collective, and related product-design references.
