---
name: interrogate
description: "Optional adversarial cross-model review to challenge a design or find blind spots, using the plugin's pinned reviewers or host model delegation. Report missing model diversity honestly; thermos remains the combined PR review."
license: MIT
disable-model-invocation: false
---

# Interrogate

Read [the workflow contract](../../references/workflow-contract.md) and
[review routing](../../references/review-routing.md). Model diversity—not personas
on one model—is the independent signal here. No edits, automatic fixes, or changes
to agent definitions. Diversity comes from the shipped `pstack-reviewer-*` agents,
which pin model families, or from host model-selecting delegation.

1. **Scope and intent.** Resolve the requested files/diff/PR and actual base/head,
   not an assumed main. Pin requested working-tree evidence if applicable. State
   the intended outcome and repository constraints; ask only if missing intent
   materially changes correctness. Parent gathers all Git/PR evidence and pinned
   context. A moving snapshot invalidates affected conclusions.
2. **Pick the panel.** Default to `pstack-reviewer-openai` and
   `pstack-reviewer-anthropic` through native `agent` calls; this also works under
   T3 Code. If one is unavailable, fall back and count families per review
   routing. For other models, or to restore a lost family, use host
   model-selecting delegation (in T3, inspect
   `orchestrator_capabilities` and `delegate_task` and the live catalog). Need at
   least two genuinely different families; do not infer diversity from ids. Without
   them, state **cross-model interrogation unavailable**, and offer a same-model
   `reviewer` pass only if the user accepts. Do not edit definitions or global
   configuration to manufacture diversity.
3. **Launch.** Fill `references/reviewer-prompt.md` with the same intent, pinned
   scope/evidence, `references/rubric.md`, `references/code-quality-review.md` and
   workflow contract contents for every reviewer. Supply actual text, not unresolved
   paths. Require read-only operation, no builds/tests, no delegation, no external
   actions, and explicit missing-context/status reports. Use immutable evidence
   or supplied snapshots, never mutable-worktree substitutes. Launch independent
   child runs in one batch (host tasks follow host instructions). Record run IDs,
   actual models and any errors/substitutions; no top-level conversations or
   homemade shell model runner. Await every required completion, without polling
   loops or duplicate work. Failed/unavailable routes are not clean reviews.
4. **Synthesize.** Deduplicate by actual issue, keep model attribution and disagreements.
   Apply `references/lead-judgment.md`; verify real paths/counterevidence before
   accepting or dismissing. Consensus is signal, never proof; a lone security or
   correctness finding still warrants investigation.
5. **Judge.** Sort into Act on (concrete material issue), Consider (valid tradeoff),
   Noted (not actionable now), Dismissed (wrong/context/style, with rationale).

Return Intent; Reviewers (actual provider/model, status, finding count); Act on /
Consider / Noted / Dismissed with evidence/remedies; Agreement map; failures and
unreviewed areas. Never describe a user-accepted same-model alternative as
cross-model interrogation. For PR work, use `thermos` as the one combined review
unless a distinct interrogation was requested; do not stack redundant review runs.
