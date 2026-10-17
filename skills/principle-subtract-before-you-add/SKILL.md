---
name: principle-subtract-before-you-add
description: "Apply when sequencing an addition, refactor, or rewrite. Remove dead code, redundant validators, and stub references first, then build on the simpler base."
disable-model-invocation: false
---

# Subtract Before You Add

Read [the workflow contract](../../references/workflow-contract.md).

Consolidate each decision behind one source of truth; prefer a small direct diff
over elegant boilerplate. Remove a layer or state only after tracing its consumers
and proving the required behavior remains. Simplicity does not excuse deleting
useful comments, supported compatibility or safeguards required by the contract.

When evolving a system, remove complexity first, then build. Default to subtraction.

Make simplification a continual investment. Leave the design slightly simpler and more capable behind the same or smaller surface than you found it.

- Sequence removal before construction
- Cut before you polish (get to the minimum before investing in quality)
- Design for observed usage, not speculative edge cases
- No speculative validators, parsers, or guards beyond what the spec demands
- Simplify prompts (remove redundant instructions, excessive templates)
- When a reference has no novel content, delete it rather than leaving a stub
