# Knowledge Governance

The knowledge store is a decision aid, not an authority dump. Add a record only when it changes retrieval or reasoning for a realistic product-design request.

## Record requirements

Every record must include:

- a stable ID and focused domain;
- actionable guidance and rationale;
- positive applicability and contraindications;
- artifact, platform, and risk scope;
- query keywords;
- evidence class and source links;
- verification date or an explicit unverified state;
- confidence calibrated to the evidence;
- observable acceptance checks.

Avoid duplicating generic advice the model already knows unless structured retrieval or a real failure case justifies it.

## Evidence and confidence

Use confidence to express support for the record's scoped guidance, not certainty that it applies to the current product.

- `0.90–1.00`: current normative requirement or repeatedly verified product invariant within its stated scope;
- `0.75–0.89`: strong platform guidance, empirical support, or durable expert synthesis with clear conditions;
- `0.55–0.74`: useful precedent or provisional synthesis requiring contextual validation;
- below `0.55`: keep out of active retrieval unless the record exists to test rejection or uncertainty behavior.

Normative, empirical, and platform-guidance records require a current primary source and review date before release. Visual inspiration cannot justify a usability or accessibility claim.

## Import policy

Third-party catalogs may seed candidates, taxonomies, aliases, or tooling when licensing permits. Imported rows start as `seed-review` and must not become authoritative merely because the source repository is popular.

Reject or rewrite records that:

- map an industry directly to one theme, palette, style, or page structure;
- turn a recommendation into a universal requirement;
- omit conditions, exceptions, or source scope;
- use self-referential provenance as evidence;
- assign confidence without a defensible basis;
- contain outdated platform or framework details;
- conflict with observed product evidence or an explicit user decision.

Retain required license notices for copied or substantially adapted material.

## Change control

Every knowledge change should pass:

1. schema and integrity validation;
2. retrieval tests for intended queries;
3. negative tests for nearby but inapplicable contexts;
4. held-out benchmark evaluation;
5. review of any changed normative claim;
6. confirmation that generated mirrors and indexes match the canonical source.

Do not raise benchmark thresholds by rewriting expected answers to match a regression.
