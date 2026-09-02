# Evidence and Severity

## Contents

- Evidence labels
- Finding test
- Severity calibration
- Confidence calibration
- Prioritization rules
- Common calibration failures

## Evidence labels

Use one or more labels internally while analyzing. Expose them when the distinction matters.

| Label | Meaning | Valid example |
| --- | --- | --- |
| Observed | Directly seen in the supplied or inspected experience | The primary action disappears after opening the keyboard at 320 px width. |
| Measured | Verified with an appropriate tool or instrument | Text contrast measures 3.2:1 against its background. |
| Reported | Present in supplied research, analytics, support data, or stakeholder evidence | 18% of users abandon at identity verification. |
| Inferred | Plausible consequence based on observed design, not verified behavior | The unfamiliar icon may reduce discoverability. |
| Unknown | Required evidence is unavailable | Screen-reader name and role cannot be determined from the screenshot. |

Never rewrite an inference as an observation. Never present an unknown as a failure.

## Finding test

A ranked finding must pass all five checks:

1. **Evidence:** Identify the exact location, state, sequence, copy, behavior, or measurement.
2. **Consequence:** Explain what becomes harder, slower, riskier, inaccessible, or less trustworthy.
3. **Cause:** Name the product, content, interaction, or system decision responsible.
4. **Remedy:** Propose a change that addresses the cause.
5. **Verification:** Define how to know the fix works.

If evidence exists but consequence is speculative, lower confidence or move it to `Needs verification`. If a comment is only personal preference, omit it.

## Severity calibration

Consider five factors together:

| Factor | Questions |
| --- | --- |
| Task impact | Does it block, corrupt, delay, or merely inconvenience the task? |
| Reach | Does it affect all users, a role, a device, an assistive technology, or an edge case? |
| Frequency | Is it on every attempt, a common branch, or a rare condition? |
| Recovery | Is recovery obvious, costly, risky, or impossible? |
| Harm | Could it cause loss, exclusion, privacy exposure, unsafe action, or damaged trust? |

### S0 Critical

Use only when at least one is true:

- irreversible data, money, privacy, security, or safety harm is credible;
- a critical task is impossible with no viable workaround;
- consent or destructive behavior can produce severe unintended outcomes;
- the experience systematically excludes users from an essential service.

Require high-quality evidence. If the harm is plausible but unverified, report a high-impact risk needing immediate verification.

### S1 Major

Use when the issue:

- blocks or causes repeated failure in a primary task;
- creates substantial error, abandonment, or support risk;
- affects many users or a critical user group;
- prevents keyboard or assistive-technology completion of a critical path;
- seriously undermines trust at a consequential decision.

### S2 Moderate

Use when the issue:

- adds meaningful cognitive load, delay, or manual work;
- obscures a secondary action or important status;
- causes recoverable errors;
- affects a subset of users or conditions with a discoverable workaround;
- creates a repeated inconsistency that slows expert use.

### S3 Minor

Use when the issue:

- causes low-impact local friction;
- is a contained consistency or readability defect;
- has little influence on task completion;
- is noticeable polish with a clear quality benefit.

### Opportunity

Use for improvements not tied to an observed defect: optimization, differentiation, delight, or an experiment. State the hypothesis and success measure. Do not assign defect severity.

## Confidence calibration

- **High:** directly observed or measured; cause and consequence are well supported.
- **Medium:** evidence is direct but reach, frequency, or consequence is partly inferred.
- **Low:** artifact fidelity is limited, a state is unavailable, or behavior is inferred from a static representation.

High severity and low confidence is valid. Phrase it as a risk and define the verification step.

## Prioritization rules

- Fix upstream model and navigation problems before local styling symptoms.
- Fix error prevention before improving error messages.
- Fix accessibility barriers on critical paths before cosmetic consistency.
- Prefer a system change when it resolves repeated findings without harming valid exceptions.
- Separate release blockers from longer-term opportunities.
- Do not call a change a quick win unless dependencies and regression risk are genuinely low.
- Do not use an effort-versus-impact score without implementation context from engineering.

## Common calibration failures

- Ranking every issue S1 makes the audit unusable.
- Treating a rare edge case as minor can hide severe harm; account for harm and recovery.
- Treating expert density as clutter ignores the user's task and experience.
- Treating platform conventions as inconsistent ignores learned behavior.
- Treating an absent ideal feature as a defect confuses opportunity with failure.
- Using analytics without segment or journey context can misstate reach and cause.
