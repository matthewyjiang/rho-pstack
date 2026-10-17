---
name: how
description: "Explain subsystem architecture, runtime flow, placement, ownership, or layering before changing code. Use for how-does-this-work questions and grounding a nontrivial design."
disable-model-invocation: false
---

# How

Read [the workflow contract](../../references/workflow-contract.md).
Build a senior engineer's working mental model, not annotated source.

1. State the question and boundaries. For a known symbol or narrow module, trace
   it directly; do not delegate a trivial lookup.
2. For a broad unfamiliar subsystem, identify independent slices worth exploring.
   Batch `agent` calls to the available `explorer` with self-contained questions
   built from `references/explorer-prompt.md`. No model-per-call selection. If that
   ID is unavailable, inspect `rho` action `agents`, or investigate directly.
3. Await all required findings. Follow real entry points, types, ownership, state,
   calls and errors; cite file/line evidence and resolve contradictions in source.
4. Synthesize using `references/explainer-prompt.md`; usually do this in the parent,
   not another delegate just to rephrase. Keep unknowns visible.

Return only applicable sections: Overview, Key concepts, How it works, Where things
live, Gotchas. A small Mermaid diagram helps when control flow or relationships
are the point. Distinguish mechanism from rationale; use `why` for motivation.
