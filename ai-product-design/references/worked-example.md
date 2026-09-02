# Worked Example: Refund-Drafting Copilot

This is a synthetic demonstration of output quality. Its policies and constraints apply only to this example.

## Input

- User: customer-support agent handling ecommerce refund requests.
- Current task: inspect order history and policy, draft a response, then issue a refund in a separate internal tool.
- Proposed AI value: summarize the case and prepare a policy-grounded draft.
- Supplied constraints: the agent remains accountable; the system may read order and policy data; it may not issue refunds, alter orders, or message customers; refund policy varies by market; sensitive notes must not enter the draft.
- Evidence available: support-task recordings, correction logs from a limited prototype, policy documents, and permission definitions.
- Unknowns: acceptable error rate, review-time baseline, launch market, retention policy, and escalation owner.

## Output excerpt

### Product hypothesis

For support agents reviewing refund requests, a policy-grounded case summary and editable response draft may reduce evidence-gathering and writing effort while preserving the agent's decision authority. Continue only if task testing shows faster correct resolution without increased policy errors or leakage of internal notes.

### AI role decision

| Task | AI role | Why | Human control |
|---|---|---|---|
| Gather relevant order facts | Summarize retrieved records | High reading cost; source facts can be inspected | Expand each cited record |
| Interpret refund eligibility | Recommend with policy evidence | Policy varies and consequence is material | Agent accepts, changes, or rejects |
| Draft customer response | Draft | Language benefits from adaptation | Fully editable before use |
| Issue refund | None | Financial action exceeds supplied authority | Existing deterministic tool remains separate |

### Capability contract

**Does:** retrieve permitted order facts and current market policy; identify missing evidence; draft an editable response; show supporting records and policy sections.

**Does not:** issue refunds, send messages, modify orders, infer undisclosed customer intent, or include internal-only notes in customer-facing text.

**Needs:** confirmed market, order identifier, current policy source, and the agent's selected resolution.

**Stores:** unresolved. Product, privacy, security, and legal owners must define retention before launch.

### Interaction architecture

`Open case -> inspect retrieved facts and missing inputs -> review eligibility recommendation with policy evidence -> choose or change resolution -> generate draft -> edit -> copy to approved channel -> record final agent decision`

The interface uses structured case facts and resolution controls. Conversation is optional for follow-up questions; it is not the primary operating surface.

### State and failure matrix

| State | User must understand | Interface response | Recovery |
|---|---|---|---|
| Policy unavailable | Eligibility is not verified | Block policy claim; show affected market and last successful source | Open policy manually or escalate |
| Conflicting order records | Summary may be incomplete | Show conflict beside both source records | Agent selects authoritative record or pauses |
| Unsupported request | System cannot advise safely | Name the unsupported condition without fabricated policy | Use existing escalation path |
| Draft generation fails | Case work is preserved | Keep facts and selected resolution | Retry draft or write manually |
| Permission revoked | Retrieval stopped | Identify unavailable source without exposing data | Request access through existing workflow |

### Trust and control plan

- Cite the exact order records and policy section behind each eligibility recommendation.
- Keep recommendation, agent decision, and final response visually distinct.
- Require no approval dialog for generating a draft because it has no external effect.
- Preserve the separate existing confirmation for the actual financial action.
- Log the policy version and final agent-selected resolution; do not log hidden reasoning.

### Evaluation plan

Use held-out cases across supported markets, edge cases, conflicting records, and policy changes. Measure correct policy application, unsupported-case escalation, sensitive-note leakage, agent correction effort, task completion, and downstream refund errors. Establish launch thresholds with support, policy, privacy, and risk owners after baseline measurement; do not invent them in the design specification.

### Acceptance criteria

- Every eligibility recommendation links to the specific current policy section and relevant order evidence.
- The copilot cannot invoke refund or messaging actions through visible controls, keyboard paths, or tool permissions.
- Customer-facing drafts exclude fields classified as internal-only in the supplied data contract.
- Losing a source or generation request never clears agent-entered work or hides the manual workflow.
