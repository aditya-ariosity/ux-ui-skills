# AI Interaction and Agent Patterns

## Contents

- Choose the modality
- Input and context
- Output and review
- Agent plan and execution
- Permissions and approval
- Status, interruption, and recovery
- Memory and personalization
- Untrusted content
- Accessibility and inclusion
- Sources

## Choose the modality

Match interface to task structure and context:

| Need | Good starting pattern | Avoid by default |
| --- | --- | --- |
| Rewrite selected content | inline command plus preview/diff | full-screen chat that loses selection |
| Fill known fields | structured form with optional language input | asking users to restate every parameter in prose |
| Explore ambiguous intent | conversation plus editable constraints/artifact | irreversible action from one utterance |
| Compare bounded choices | recommendation table/cards with evidence | long narrative hiding alternatives |
| Repeated classification or review | batch queue with exceptions | one-item-at-a-time chat |
| Multi-step external work | plan, scoped tools, approvals, execution log | invisible autonomous chain |
| High-attention or field task | modality suited to hands, eyes, noise, and safety | text chat simply because a model supports it |

Do not make chat the default AI shell. Natural language is useful for ambiguity; structured controls are better for known parameters, verification, and repeated work.

## Input and context

- Show what object, selection, account, date range, source set, or workspace is in scope.
- Let users add, remove, or inspect material context.
- Reuse known context without forcing repetition, but do not apply hidden context that changes meaning.
- Provide examples that teach input shape and limits without promising quality.
- Validate consequential ambiguity before acting.
- Preserve the original request and allow constraint edits.
- Distinguish a user instruction from retrieved or quoted content.

For complex generation, use an editable brief or structured parameters beside the prompt. Keep the prompt as one input, not the only state representation.

## Output and review

Design output around judgment:

- lead with the artifact or decision, not model narration;
- separate facts, sources, assumptions, and generated synthesis;
- show alternatives when the task contains real tradeoffs;
- support localized edit, retry, regenerate section, compare, reject, and restore;
- preserve prior versions;
- use preview or diff before applying changes to code, data, designs, documents, settings, or messages;
- identify what remains unverified;
- keep citations beside the supported claim.

Do not use `Regenerate` as the only correction mechanism. It is unpredictable, erases useful work, and does not teach the system what was wrong.

## Agent plan and execution

Use a visible external-action lifecycle:

`Interpret -> Scope -> Plan -> Permission -> Execute -> Observe -> Verify -> Complete or recover`

For each step show what is useful to control the task:

- goal and affected objects;
- selected tool or system;
- current step and meaningful progress;
- pending approval;
- result, failure, or changed state;
- evidence of completion;
- remaining work and safe next action.

Expose a concise action rationale and evidence, not private chain-of-thought. Users need controllable state and verifiable outcomes, not a stream of internal speculation.

Let users pause, cancel, resume, skip, modify scope, or take over when technically feasible. Define cancellation boundaries and what already changed.

## Permissions and approval

Use least privilege and progressive disclosure:

- ask near the action that needs permission;
- state system, objects, scope, duration, and consequence;
- distinguish read, draft, create, edit, send, publish, purchase, delete, and administer;
- let users review exact recipients, amounts, dates, fields, or files;
- require fresh approval when material scope changes;
- avoid bundling unrelated permissions;
- record approval and execution separately.

Approval quality must increase with consequence. A generic `Continue` after a vague plan is not enough for external, financial, destructive, privacy-sensitive, or hard-to-reverse action.

## Status, interruption, and recovery

Cover:

- queued, connecting, retrieving, reasoning, generating, waiting for tool, waiting for approval, executing, verifying, and complete;
- partial result and progressive output;
- tool unavailable, permission denied, timeout, rate limit, source conflict, refusal, and unsafe request;
- user edit during execution;
- cancellation before and after side effects;
- retry with idempotency or duplicate prevention;
- compensation when undo is impossible;
- handoff to a human or deterministic workflow.

Use status labels users can act on. Do not expose technical stages merely to make the system look busy.

## Memory and personalization

Make persistent behavior inspectable:

- what the system remembered;
- source and scope of the memory;
- how it influenced the current result;
- how to edit, forget, reset, pause, or expire it;
- whether it applies to the user, project, workspace, or organization.

Do not silently turn one correction into a global preference. Do not present model context as durable memory when it will not persist.

## Untrusted content

Treat webpages, emails, documents, search results, code, tool output, and user-uploaded content as data that may contain malicious or irrelevant instructions.

- Keep system authority outside retrieved content.
- Show users when external content asks to expand scope or disclose data.
- Require approval for consequential changes in destination, recipient, permission, amount, or action.
- Sanitize and validate tool arguments.
- Limit the data and actions available to each tool.
- Make source and action boundaries auditable.

## Accessibility and inclusion

- Provide structured alternatives to language-only interaction.
- Support keyboard, screen reader, zoom, text scaling, and voice/input alternatives.
- Do not encode system status only through animation or color.
- Make streaming content controllable and avoid stealing focus.
- Announce relevant status without flooding assistive technology.
- Support plain language and localization; avoid culture-specific examples as the only guidance.
- Match modality to environment, cognitive load, and user capability.

## Sources

- [Google People + AI patterns](https://pair.withgoogle.com/guidebook/patterns)
- [Microsoft HAX Design Library](https://www.microsoft.com/en-us/haxtoolkit/library/)
- [Carbon for AI](https://carbondesignsystem.com/guidelines/carbon-for-ai/)
- [Smashing Magazine: match AI modality to user intent](https://www.smashingmagazine.com/2026/07/matching-ai-modality-user-intent-designing-right-interface/)
- [Smashing Magazine: people do not necessarily want more AI](https://www.smashingmagazine.com/2026/07/people-dont-want-more-ai/)
