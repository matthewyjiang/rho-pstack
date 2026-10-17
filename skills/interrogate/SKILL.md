---
name: interrogate
description: "Optional host-backed adversarial cross-model review to challenge a design or find blind spots. Report unavailable model-selecting delegation honestly; thermos remains the portable combined PR review."
license: MIT
disable-model-invocation: false
---

# Interrogate

Read [the workflow contract](../../references/workflow-contract.md) and
[review routing](../../references/review-routing.md). Model diversity—not personas
on one model—is the independent signal here. No custom agents, model pins, edits
or automatic fixes. This skill's cross-model path requires host-provided
model-selecting delegation; standalone Rho's `agent` tool does not provide it.

1. **Scope and intent.** Resolve the requested files/diff/PR and actual base/head,
   not an assumed main. Pin requested working-tree evidence if applicable. State
   the intended outcome and repository constraints; ask only if missing intent
   materially changes correctness. Parent gathers all Git/PR evidence and pinned
   context. A moving snapshot invalidates affected conclusions.
2. **Check capability.** Discover the host's model-selecting delegation API. In
   T3, inspect `orchestrator_capabilities` and `delegate_task` schemas and live
   catalog. Choose at least two genuinely different available model families;
   do not infer diversity from different IDs. Without that capability, state
   **cross-model interrogation unavailable**, and offer an ordinary same-model
   `reviewer` pass only if the user accepts. Do not install definitions, change
   global configuration, or disguise native `agent` calls as model-selecting.
3. **Launch.** Fill `references/reviewer-prompt.md` with the same intent, pinned
   scope/evidence, `references/rubric.md`, `references/code-quality-review.md` and
   workflow contract contents for every reviewer. Supply actual text, not unresolved
   paths. Require read-only operation, no builds/tests, no delegation, no external
   actions, and explicit missing-context/status reports. Use immutable evidence
   or supplied snapshots, never mutable-worktree substitutes. Launch independent
   host child tasks in one batch following host instructions. Record task IDs,
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
