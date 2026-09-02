# AI Evaluation and State Design

## Contents

- Evaluation stack
- Test-set design
- Task and interaction metrics
- State and failure matrix
- Feedback and learning
- Launch and monitoring
- Acceptance criteria patterns
- Sources

## Evaluation stack

Evaluate four connected layers:

1. **System quality:** factuality, relevance, safety, calibration, robustness, latency, cost, tool success.
2. **Interaction quality:** comprehension, control use, correction effort, provenance use, recovery, accessibility.
3. **Task outcome:** completion, quality, time, error, review burden, downstream action, confidence accuracy.
4. **Product consequence:** adoption of useful work, repeated failure, harm, support, fairness, privacy, operational and business outcome.

Do not launch because a model benchmark improved. A better model score may not improve the scoped workflow, and an excellent interface cannot repair unacceptable task reliability.

## Test-set design

Build cases from actual task distribution and risk:

- common and high-value tasks;
- rare but severe consequences;
- ambiguous or underspecified requests;
- missing, stale, and conflicting sources;
- long, multilingual, malformed, and accessibility-relevant inputs;
- adversarial and untrusted retrieved content;
- unsupported and policy-sensitive requests;
- tool failure, permission loss, and partial completion;
- repeat use and memory effects;
- distribution shifts and new product states.

Record expected behavior at product level, including refusal, clarification, escalation, or safe fallback. Do not force one exact wording when several outputs are acceptable.

Use expert review, rubric grading, deterministic checks, model-assisted evaluation, and user research for the questions each can validly answer. Calibrate automated graders against human judgment and inspect disagreement.

## Task and interaction metrics

Select metrics tied to the hypothesis:

- task success and quality;
- time to acceptable result;
- number and cost of corrections;
- proportion accepted as-is, edited, rejected, or abandoned;
- source verification and citation-support accuracy;
- approval comprehension and scope errors;
- action success, duplicate action, rollback, or compensation;
- ability to detect intentionally seeded errors;
- appropriate reliance and overreliance;
- fallback and escalation success;
- latency distribution and cancellation;
- accessibility task completion;
- user-reported confidence compared with actual correctness.

Avoid engagement or output volume as a proxy for value. High use can signal repeated failure or forced workflow dependence.

## State and failure matrix

Specify at minimum:

| State | User needs | Interface response | Recovery |
| --- | --- | --- | --- |
| Awaiting input | know scope and examples | capability boundary, context, structured options | edit or exit |
| Processing | know progress and control | useful status, cancel, retained input | resume or retry |
| Partial output | judge what is complete | label partial sections and missing steps | continue, accept partial, cancel |
| Low evidence/conflict | avoid false certainty | expose missing/conflicting sources | add context, choose source, escalate |
| Tool unavailable | preserve work | name affected step and unchanged state | retry, alternate tool, manual path |
| Permission denied | understand needed scope | explain permission and consequence | grant, narrow task, manual path |
| Refusal/safety stop | understand boundary | concise reason and safe alternatives | reframe or escalate where allowed |
| Execution failed | know what changed | itemized success/failure and verification | retry safely, undo, compensate |
| Stale result | avoid acting on old data | timestamp and refresh option | re-run with current source |
| Complete | verify consequence | artifact/action summary and evidence | edit, undo, export, continue |

## Feedback and learning

Capture feedback when the user can judge the result:

- ask what was wrong or useful at a granular level;
- distinguish model quality, missing context, preference, tool failure, and policy mismatch;
- avoid thumbs-only feedback for consequential tasks;
- show whether feedback affects the current result, future personal behavior, product evaluation, or model training only when policy confirms it;
- let users correct persistent assumptions explicitly;
- protect sensitive content in feedback and review pipelines.

Do not adapt silently from noisy signals such as acceptance, dwell time, or a single edit. Some users accept poor results under time pressure.

## Launch and monitoring

Use staged release based on consequence and evidence:

1. internal task evaluation;
2. usability and accessibility testing;
3. limited pilot with monitoring and fallback;
4. expansion after thresholds and guardrails are met;
5. ongoing regression tests across model, prompt, retrieval, tool, policy, and UI changes.

Monitor:

- quality and safety by task/segment;
- source and tool health;
- latency and cost;
- corrections, refusals, escalations, and reversals;
- harmful or irreversible outcomes;
- drift after model or policy changes;
- unexplained differences across relevant groups;
- support and incident themes.

Define accountable owners and an incident path. Preserve audit records suitable to the risk and privacy policy.

## Acceptance criteria patterns

- The system shows the exact workspace, sources, and objects in scope before producing a consequential recommendation.
- Users can edit one part of an output without losing accepted work or original input.
- Every external action exposes destination and changed fields before approval and records success or failure per item.
- Cancellation states which steps stopped and which side effects already occurred.
- A citation opens the supporting source and the cited passage substantively supports the adjacent claim.
- Removing a memory changes future behavior in the stated scope and the removed item no longer appears in the memory view.
- When an evaluation threshold is not met, the feature follows the defined safe fallback rather than presenting uncertain output as complete.

## Sources

- [Microsoft HAX Guidelines](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/)
- [Google People + AI Guidebook](https://pair.withgoogle.com/guidebook/)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1)
- [Microsoft Research: Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/)
- [Smashing Magazine: designing with uncertainty](https://www.smashingmagazine.com/2026/06/designing-uncertainty-how-ai-supercharges-probabilistic-thinking/)

Research snapshot: 2026-08-09. Verify current policy, model, platform, and regulatory requirements at task time.
