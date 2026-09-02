# Capability, Risk, and Trust

## Contents

- Capability contract
- AI role and autonomy
- Consequence model
- Trust calibration
- Transparency and provenance
- Data, consent, and persistence
- Sources

## Capability contract

Define the product capability at task level:

`User goal | Supported inputs | Context used | Output/action | Quality boundary | Latency | Cost | User control | Fallback`

Separate what is:

- demonstrated in evaluation;
- expected but unverified;
- unavailable by design;
- prohibited by policy;
- unavailable because a tool, permission, or source is missing.

Do not describe the underlying model's general capabilities as the product contract. Tool access, retrieval, prompts, policies, data, interface, and downstream services determine the actual experience.

## AI role and autonomy

Use a clear role:

| Role | System behavior | Required control |
| --- | --- | --- |
| Assist | explain, find, transform, or suggest locally | easy edit/reject; no hidden action |
| Draft | create a candidate artifact | preview, provenance, edit, version, apply |
| Recommend | rank or propose choices | factors/evidence, alternatives, dismiss, escalation |
| Decide | select an outcome within delegated policy | explicit authority, appeal, audit, outcome monitoring |
| Act | change an object or contact a system | scope, approval, execution status, verification, undo/compensation |
| Orchestrate | plan and perform multiple actions | plan review, bounded permissions, step visibility, pause/stop, audit trail |

Increase autonomy only when task evidence, system reliability, user benefit, permissions, monitoring, and recovery support it. Do not treat user tolerance of drafting errors as permission for action errors.

## Consequence model

For every failure ask:

- Who is affected, including non-users?
- Can it cause loss, exclusion, privacy exposure, unsafe action, reputational harm, wasted work, or overreliance?
- Is the action reversible, compensable, reviewable, or time-sensitive?
- Can the user detect the error before consequence?
- Does the user have the expertise and evidence to judge it?
- Does repeated use amplify the harm or bias?

Classify product decisions by consequence and detectability, not by a generic `AI risk` label. A low-frequency error may still need strong review if harm is severe and hard to detect.

Map:

`Failure mode | Cause class | Detection | Consequence | Prevention | User recovery | System response | Owner`

Cause classes may include missing context, retrieval error, source conflict, model confabulation, stale data, unsafe instruction, tool failure, permission mismatch, ambiguous intent, distribution shift, or policy refusal.

## Trust calibration

The goal is appropriate reliance, not maximum trust.

- Set expectations in task language at the moment they matter.
- Let users inspect the inputs, scope, sources, and affected objects.
- Distinguish generated, retrieved, user-authored, and verified content.
- Show known limitations and missing context without blanket disclaimers.
- Provide alternatives and a non-AI path when users need certainty or continuity.
- Make correction and reversal visible enough to reduce fear of experimentation.
- Do not use anthropomorphic language or human-like identity to imply competence, intent, or accountability the system does not have.
- Do not display a precise confidence score unless it is calibrated, explained, evaluated for the task, and useful to the decision.

Avoid decorative sparkle icons as the only disclosure. The user should understand what AI changed and how to inspect or revert it.

## Transparency and provenance

Provide the minimum explanation needed to make a sound decision:

- source links and quoted evidence where factual verification matters;
- a concise summary of decision factors or rules;
- changed fields or a diff for generated edits;
- relevant missing or conflicting evidence;
- model or system limitation when it changes the action;
- timestamp and source freshness.

Do not expose private internal reasoning or present generated rationales as faithful access to model internals. Prefer evidence, inputs, rules, and a concise product-level explanation that can be verified.

Check every citation against the claim. A plausible source list that does not support the statement increases overtrust.

## Data, consent, and persistence

Specify:

- data requested and purpose;
- user, workspace, third-party, retrieved, and generated data boundaries;
- retention, training, review, sharing, and deletion behavior confirmed by policy;
- permission scope and duration;
- sensitive-data detection and handling;
- memory contents, visibility, correction, reset, and expiry;
- logs and audit access;
- behavior when consent or access is withdrawn.

Use progressive permission: request authority when the task requires it and explain the consequence. Do not infer consent to future training, persistent memory, external action, or broader data access from use of one AI feature.

## Sources

- [Microsoft HAX Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/)
- [Google People + AI Guidebook](https://pair.withgoogle.com/guidebook/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI 600-1 Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1)
- [OECD AI Principles](https://oecd.ai/en/ai-principles)
- [Carbon for AI](https://carbondesignsystem.com/guidelines/carbon-for-ai/)

These sources differ in purpose: HAX and PAIR guide interaction design, Carbon provides implementation precedents, and NIST/OECD address broader risk and governance. Do not present guidance as a legal or universal conformance requirement.
