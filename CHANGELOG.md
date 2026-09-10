# Changelog

## 2.1.1

- Updated six stable UX/UI specialist skills after Tessl review and improvement passes.
- Preserved the strongest reviewed skill content and descriptions from the approved evaluation versions.
- Improved routing clarity across audit, dashboard redesign, design-system review, AI product design, case-study writing, and developer handoff workflows.
- Strengthened skill descriptions with clearer triggers, boundaries, exclusions, and adjacent-skill routing.
- Added or refined explicit validation checkpoints, feedback loops, examples, and evidence-quality expectations across the skill pack.
- Clarified that the skills can be used with Codex, ChatGPT, Claude, and other agentic AI tools.
- Kept `product-design` as an experimental, explicit-invocation end-to-end foundation.
- Updated README positioning to reflect Tessl review performance and release status.

## 2.1.0-rc2

- Added CI linting for skill metadata, description length, and relative `SKILL.md` links.
- Added a validated `product-design/data/project-context.example.json` template.
- Updated product-design context documentation to point users to the example context file.
- Allowed `$schema` in project context files so examples and authored contexts can self-identify their schema.
- Kept `argument-hint` under `metadata` because the current Codex skill validator rejects top-level `argument-hint` in `SKILL.md` frontmatter.

## 2.1.0-rc1

- Refined trigger descriptions and routing exclusions for the six stable UX/UI skills.
- Added worked examples for every stable skill.
- Marked `product-design` as experimental and disabled implicit invocation.
- Added context validation, benchmark gates, and a regression test for the product-design foundation.
- Clarified README positioning, target audience, rigor tradeoff, and implementation scope.
