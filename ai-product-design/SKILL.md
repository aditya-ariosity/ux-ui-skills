---
name: ai-product-design
description: Design or improve an AI-assisted feature, copilot, agent, recommendation, generation, or automation workflow with explicit capability boundaries, user control, recovery, trust, and evaluation. Trigger on "design this AI feature", "improve this copilot", or "plan this agent workflow". Do not default every AI product to chat.
metadata:
  argument-hint: "[AI use case, users, evidence, risks, and constraints]"
---

# AI Product Design

Design the human-system relationship, not only the prompt box. The experience must help users form an accurate model of what the system can do, judge its output, correct it efficiently, and retain control over consequences.

## 1. Test whether AI belongs

Define:

- user goal and current workflow;
- value AI may add: speed, scale, synthesis, prediction, personalization, or automation;
- deterministic alternative and why it is insufficient;
- acceptable error, latency, cost, and review burden;
- affected people, data, objects, and downstream actions;
- business outcome and user outcome;
- evidence needed to continue investing.

Do not invent organization policy, retention, approval roles, architecture, quality thresholds, or launch percentages. Mark recommended controls as proposals and assign unresolved values to the accountable product, policy, security, legal, data, or engineering owner.

Prefer deterministic interaction when rules are stable, correctness must be exact, or users can complete the task faster without probabilistic behavior.

## 2. Map capability and risk

Read [references/capability-risk-and-trust.md](references/capability-risk-and-trust.md). Create:

`Task | AI role | Inputs and sources | Expected quality | Failure modes | Consequence | Human control | Escalation`

Separate suggestion, drafting, classification, recommendation, and execution. A system that can generate a plan does not automatically have permission to carry it out.

## 3. Select the interaction form

Choose based on the task:

- inline assistance for local transformation or completion;
- structured controls for known parameters and repeatable outputs;
- recommendation with evidence for bounded choices;
- conversational interaction for ambiguous, iterative intent;
- batch workflow for repeated review and approval;
- agentic workflow for multi-step action across systems.

Chat is a pattern, not a product strategy. Pair open language with structured scope, previews, history, and controls when consequences matter.

Read [references/interaction-and-agent-patterns.md](references/interaction-and-agent-patterns.md) for detailed behavior.

## 4. Design the interaction lifecycle

Use the HAX lifecycle:

### Initially

- make capabilities and limits clear in task language;
- set realistic expectations for quality, latency, and coverage;
- provide safe examples without implying guaranteed output;
- request only necessary data and permissions.

### During interaction

- make status, scope, active context, and sources visible;
- let users adjust constraints and correct misunderstandings;
- distinguish user content, retrieved evidence, generated synthesis, and verified facts;
- make consequential implications visible before commitment.

### When wrong

- make correction cheaper than restart;
- preserve input and previous output for comparison;
- support edit, retry, reject, undo, escalate, and non-AI fallback as appropriate;
- explain actionable failure without exposing irrelevant internals.

### Over time

- expose history, memory, learned preferences, and behavior changes;
- let users inspect, correct, forget, reset, and disable persistence;
- prevent silent scope expansion after model or policy changes.

## 5. Specify agentic controls

For each action define:

`Permission | Scope | Preview | Approval | Execution status | Verification | Undo or compensation | Audit trail`

Require meaningful review for high-impact, external, destructive, financial, privacy-sensitive, or hard-to-reverse actions. A generic confirmation dialog is not meaningful review; show the affected objects and exact change.

Treat retrieved content as untrusted data. Never let instructions embedded in pages, documents, messages, or tool output silently expand system authority.

## 6. Design evidence and uncertainty

- Show sources where users need factual verification or provenance.
- Ensure citations support the specific claim and distinguish source content from generated inference.
- Communicate uncertainty only when it helps a decision. Avoid arbitrary confidence percentages.
- Show alternatives, ranges, missing inputs, or reason-for-recommendation when these are more actionable than a score.
- Do not use an explanation to encourage overtrust in a system that has not been evaluated for the task.

## 7. Evaluate the product

Read [references/evaluation-and-states.md](references/evaluation-and-states.md). Test system quality and interaction quality together across normal, edge, adversarial, and recovery cases. Measure task outcomes, not just model metrics or engagement.

## 8. Produce the design specification

For a complete input-to-output demonstration, read [references/worked-example.md](references/worked-example.md). Use it to calibrate the capability contract, approval model, failure coverage, and testability; do not reuse its fictional policies or thresholds.

Return:

### Product hypothesis

`For [user] doing [task], AI will improve [outcome] by [mechanism]. We will know through [measure], and stop or change course if [guardrail].`

### Capability contract

State what the system does, does not do, needs, stores, and can act upon.

### Interaction architecture

Describe entry, context, input, generation or action, review, correction, execution, completion, and return.

### State and failure matrix

Cover latency, partial output, refusal, uncertainty, unavailable tools, permission denial, source conflict, unsafe request, execution failure, and recovery.

### Trust and control plan

Define provenance, permissions, approvals, memory, privacy, escalation, auditability, and undo.

### Evaluation plan

Define test sets, task metrics, behavioral research, quality thresholds, guardrails, monitoring, and feedback-loop limits.

Express unknown thresholds as owner decisions or a method for establishing a baseline. Never create impressive-looking pass rates without evidence, risk analysis, and accountable approval.

### Acceptance criteria

Write observable criteria for behavior, controls, accessibility, safety, privacy, and recovery.

## Quality bar

- AI is justified by a user outcome;
- capability boundaries match evaluated performance;
- user control increases with consequence;
- correction is cheaper than restart;
- no critical action occurs through hidden or ambient consent;
- sources and uncertainty support judgment rather than decorate output;
- memory and permissions are inspectable and reversible;
- evaluation covers the whole task and downstream consequence;
- a reliable fallback exists where failure would block an essential task.
