# AI Experience Audit

## Contents

- Audit model
- Before interaction
- During interaction
- When AI is wrong
- Over time
- Generative AI specifics
- Evidence and reporting
- Primary sources

Use this reference only when probabilistic or automated behavior materially shapes the user experience. Evaluate the interface and the system behavior together; many AI UX failures cannot be fixed with copy or layout alone.

## Audit model

Trace:

`user intent -> input/context -> system action -> output -> evaluation -> correction -> downstream consequence`

Identify:

- what the user believes the system can do;
- what data and context it actually uses;
- how uncertainty and limits are communicated;
- how the user can inspect, correct, reject, undo, or escalate;
- what happens when output is wrong, delayed, unsafe, or unavailable;
- how feedback changes future behavior, if at all.

Do not recommend AI where deterministic interaction is more reliable, legible, or efficient.

## Before interaction

Inspect whether the product:

- explains the capability in task language rather than model language;
- sets realistic expectations for quality, latency, coverage, and failure;
- distinguishes suggestion, automation, and authoritative decision;
- requests only the context or permission needed for the task;
- provides examples that teach scope without implying guaranteed results;
- identifies consequential data use, retention, sharing, or human review.

Avoid generic disclaimers that shift all responsibility to the user while the interface still presents output as authoritative.

## During interaction

Inspect whether the product:

- makes system status and progress visible;
- shows what input, source, selection, or scope the output is based on;
- supports iteration without making users restate known context;
- lets users adjust relevant constraints and correct misunderstandings;
- distinguishes generated content from user-authored or verified content;
- presents confidence only when calibrated, understandable, and decision-relevant;
- preserves user control for consequential actions.

Do not add confidence scores by default. A precise number can create false certainty when users do not know what it represents.

## When AI is wrong

Inspect whether the experience:

- makes correction cheaper than starting over;
- supports edit, retry, alternative, reject, undo, and escalation as appropriate;
- preserves the original input and prior output for comparison;
- explains actionable failure without exposing irrelevant internals;
- avoids silently applying low-confidence or high-impact changes;
- prevents unsafe or irreversible action without meaningful review;
- captures feedback at the point where users can judge the result.

For high-consequence domains, require explicit review of the affected object and action before execution. A confirmation dialog is insufficient if it does not expose what changed.

## Over time

Inspect whether the product:

- communicates when behavior may adapt or change;
- gives users access to relevant history, preferences, and learned settings;
- lets users correct or reset persistent assumptions;
- avoids hidden personalization that makes outcomes impossible to explain;
- monitors repeat failure and offers a reliable non-AI path;
- keeps controls and expectations stable across model or policy changes.

## Generative AI specifics

Check:

- provenance and source access for factual or consequential output;
- clear boundaries between retrieved facts, user data, and generated synthesis;
- citation quality and whether a source actually supports the claim;
- preview and diff for generated changes to code, data, designs, or documents;
- versioning, undo, and recovery after application;
- safe handling of prompt injection or untrusted retrieved content where relevant;
- latency states, cancellation, partial results, and resume behavior;
- disclosure when humans may review prompts or outputs;
- export, deletion, and retention controls for sensitive content.

Do not label all hallucination risk as one finding. Tie each risk to a task, consequence, control gap, and recovery path.

## Evidence and reporting

Separate:

- observed interface behavior;
- observed model behavior from repeatable test cases;
- policy or system behavior confirmed by documentation;
- hypotheses requiring model, data, safety, privacy, or legal review.

Do not infer model capability, training data, retention, or reliability from interface copy. Recommend cross-functional work when the fix requires model evaluation, data changes, policy, or backend controls.

For each AI finding, include the failure moment:

- initial use;
- regular use;
- system error or uncertainty;
- behavior over time.

## Primary sources

- [Microsoft HAX Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/)
- [Microsoft HAX Toolkit](https://www.microsoft.com/en-us/haxtoolkit/)
- [Google People + AI Guidebook](https://pair.withgoogle.com/old-gb/)

Use these as evidence-based design guidance, not as conformance standards.
