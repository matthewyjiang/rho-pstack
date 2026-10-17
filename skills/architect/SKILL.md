---
name: architect
description: "Sketch caller usage, types, signatures and module ownership before nontrivial implementation. Compare distinct designs, then implement only within the requested scope."
license: MIT
disable-model-invocation: false
---

# Architect

Read [the workflow contract](../../references/workflow-contract.md).
Design first; do not automatically write scaffolds or implement a design-only request.
Track Ground → Sketch → Agree → Implement → Reassess with `todo` for substantial work.

## Ground

Use `how` to understand touched subsystems. Use `why` when changing existing
ownership or layering. Greenfield work still needs integration constraints.

## Sketch and compare

Write caller-facing usage before deriving types, signatures and a module map.
Explore structurally distinct viable shapes, not cosmetic variants of one idea.
Compare at least two for a genuinely novel architectural choice; a narrow change
with an established pattern needs no manufactured alternatives.

Screen against `references/design-red-flags.md`: shallow modules, representation
leaks, temporal decomposition, pass-through methods, split ownership, duplicate
paths, importable internals and hand-synced lists. Prefer a smaller interface that
hides real complexity, not a deeper call chain. Data structures and invariants
come before logic. Subtract unnecessary state/layers before adding machinery.

For substantial independent design perspectives, use separate calls to the existing
reviewers per [review routing](../../references/review-routing.md): the shipped
`pstack-reviewer-*` agents give cross-family perspectives, with the built-in
`reviewer` as the fallback. Same-model perspectives are still valid. Supply
`references/runner-prompt.md`, `references/rationale-template.md`, the grounding
and same task to each in one batch. They return sketches in their results, without
editing files, creating worktrees or recursively running skills. Otherwise compare
candidates in the parent. Do not claim model diversity for same-model or self-generated designs.
Synthesize the best shape; record what won, what was borrowed/rejected and why.

## Agree and implement

Respect requested checkpoints. Ask if a missing decision materially changes the
result, compatibility or authority; otherwise proceed within the implementation
request. A design-only task ends with the design. In-memory/textual `not implemented`
bodies are fine for sketches, not an excuse to leave broken production commits.

Fill in the chosen contract. Repeated new casts, special cases, shared-state
workarounds or caller knowledge of internals suggest the sketch is wrong. Re-ground
and redesign as though the discovered constraints were original requirements;
do not keep bolting fixes on. Deliver verifiable increments under repository policy.

Output caller usage, type/signature sketch, ownership/module map, rationale,
alternatives/tradeoffs, risks, and next implementation step. Use the rationale template.
