# Product Design Evaluation

Evaluate whether the result satisfies the original user task, organizational outcome, constraints, and evidence—not whether it resembles the initial concept.

## Evaluation layers

1. **Retrieval:** Did the system find applicable knowledge and abstain from irrelevant guidance?
2. **Reasoning:** Do the product model, interaction decisions, and visual direction follow from context and evidence?
3. **Coherence:** Do structure, type, color, density, motion, and components reinforce the same direction?
4. **Rendered behavior:** Does the implementation work across critical states, widths, inputs, zoom, and content conditions?
5. **User evidence:** Can representative users understand and complete the task with acceptable confidence, error, and recovery?

Passing an earlier layer does not prove a later one.

## Render-review loop

For implemented work:

1. open the actual build;
2. inspect relevant content breakpoints;
3. exercise the critical path and state changes;
4. inspect focus, semantics, overflow, long content, loading, error, and recovery where applicable;
5. capture evidence for material failures;
6. fix the underlying cause;
7. inspect again.

Automated and heuristic checks produce leads. Confirm a failure with the test appropriate to the claim.

## Outcome record

Separate:

- confirmed defect;
- risk requiring verification;
- deliberate tradeoff;
- opportunity;
- preserved strength.

For material issues record evidence, consequence, cause, correction, and an observable acceptance condition.

## Benchmarking the skill

Use realistic cases that were not written to mirror the implementation. Include different artifact types, risk levels, platforms, and negative queries. Evaluate retrieval separately from final design quality.

Do not promote a benchmark threshold after tuning against the same cases. Preserve a held-out set and review judgments independently before treating them as a quality target.
