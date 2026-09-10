# UX/UI Design Skills

A high-scoring UX/UI skill pack for evidence-led product-design work across Codex, ChatGPT, Claude, and other agentic AI tools.

Current release: `2.1.1`.

This repository contains six stable specialist skills and one experimental end-to-end product-design foundation. The stable skills are designed for professional UX/UI audits, dashboard redesigns, design-system reviews, AI product design, portfolio case studies, and developer handoff.

The pack has passed Tessl review and scored among the strongest UX/UI skill packs tested in this category, with several skills reaching near-perfect or perfect evaluation scores for description quality, workflow clarity, actionability, progressive disclosure, and evidence discipline.

## Stable Skills

- `ux-ui-audit`: Audits existing screens, flows, and product artifacts for hierarchy, usability, accessibility, layout, information architecture, responsive behavior, trust, states, and prioritized improvements.
- `dashboard-redesign`: Redesigns dashboards, reports, KPI views, operational consoles, and analytical workspaces around real decisions, data meaning, density, comparison, drilldowns, trust, responsiveness, and accessibility.
- `design-system-review`: Audits design systems, UI libraries, component libraries, tokens, spacing, typography, color, variants, states, documentation, design-code parity, contribution models, and governance.
- `ai-product-design`: Designs and evaluates AI assistants, LLM features, copilots, chatbots, agents, recommendations, automation workflows, trust flows, feedback loops, approvals, recovery, memory, permissions, and evaluation plans.
- `case-study-writer`: Turns supplied product-design evidence into concise, credible UX/UI portfolio case studies and interview narratives without inventing metrics, ownership, research, quotes, or outcomes.
- `handoff-to-dev`: Converts approved UX/UI designs and prototypes into build-ready behavior specs, component contracts, responsive rules, state matrices, accessibility requirements, analytics notes, QA criteria, and acceptance tests.

Each stable skill includes structured workflows, concrete output formats, validation checkpoints, and realistic examples. The examples demonstrate evidence quality, decision logic, output density, and what the skill must leave unresolved.

## Experimental Foundation

`product-design` is an explicit-invocation foundation for end-to-end product design.

It supports project framing, research retrieval, experience modeling, visual direction, artifact creation, and rendered validation. It includes a project-context schema, governed JSONL knowledge records, dependency-free retrieval, anonymized benchmarks, and executable tests.

It is intentionally marked experimental and should not replace the six stable specialist skills for isolated audits, dashboards, AI features, design systems, handoff, or case-study writing.

## Evaluation Status

The skill pack has been reviewed with Tessl and improved through multiple evaluation passes.

Highlights from the reviewed set include:

- Strong validation status across skill structure, frontmatter, references, assets, and relative links.
- High description scores for specificity, completeness, trigger-term quality, and low conflict risk.
- High content scores for concise instruction design, actionability, workflow clarity, and progressive disclosure.
- Several individual skills reached 94-98% overall review scores.
- `ux-ui-audit` reached 97%.
- Improved versions of key skills reached perfect or near-perfect sub-scores in content or description dimensions.

These results indicate the pack is not just a collection of prompts, but a structured skill system with clear routing, evidence discipline, realistic workflows, and measurable quality controls.

## Who This Is For

These skills are for designers, product teams, AI design teams, product managers, researchers, and engineers who need defensible product-design reasoning rather than generic visual suggestions.

Use this pack when the work requires:

- evidence-backed UX/UI critique;
- severity-calibrated findings;
- dashboard and data-product redesign;
- design-system diagnosis;
- AI-product interaction design;
- credible portfolio case-study writing;
- developer-ready handoff specifications;
- explicit uncertainty instead of invented precision.

The pack favors professional audit, specification, and decision quality over instant decorative output.

## What This Pack Does Not Do

The stable skills do not silently invent breakpoints, density values, metric thresholds, research findings, policies, backend contracts, or business rules.

When the task needs numbers or factual claims, the skills use supplied system values, inspected implementation constraints, or clearly labeled proposals with an owner and validation method.

The stable skills do not promise stack-specific production code. Use them to decide, critique, structure, and specify the experience; pair the output with the target implementation workflow when code is requested.

## Structure

```text
ux-ui-skills/
  ux-ui-audit/
  dashboard-redesign/
  design-system-review/
  ai-product-design/
  case-study-writer/
  handoff-to-dev/
  product-design/
