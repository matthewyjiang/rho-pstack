---
name: interrogate
description: "Adversarial cross-model review to challenge a design or find blind spots. Use for interrogate, challenge this, or stress-test requests; thermos is the default combined PR review."
license: MIT
disable-model-invocation: false
---

# Interrogate

Read [the workflow contract](../../references/workflow-contract.md) and
[review routing](../../references/review-routing.md).
Different model families provide independent signal; different personas on one
model do not. Review only: never auto-apply findings.

1. **Scope.** Respect explicit files/diff/PR. Resolve actual base and head commits
   from PR metadata or branch tracking, not an assumed `main`. For a new repo or
   working-tree review describe that scope explicitly. Pin SHAs and record dirty
   state; include staged/unstaged/untracked content only when in scope. If the
   snapshot changes, invalidate affected conclusions and review the changed portion.
2. **Intent.** State the intended outcome from the request, commits and PR. Ask only
   if missing intent materially changes what correctness means.
3. **Panel.** Inspect `rho` action `agents` and follow routing. Select one reviewer
   per distinct configured model family, at least two for cross-model review.
   Do not pass a `model` to `agent` or silently substitute the parent. Missing
   diversity/auth is a visible blocker, not a successful interrogation.
4. **Launch.** Fill `references/reviewer-prompt.md` identically for each reviewer:
   intent, immutable scope/diff/context, `references/rubric.md`, and
   `references/code-quality-review.md`. Include actual contents, repository
   constraints and workflow contract. In one batch call
   `agent({agent_id: "pstack-reviewer-openai", prompt: "<filled brief>"})` and
   `agent({agent_id: "pstack-reviewer-cliproxy", prompt: "<same filled brief>"})`
   when that panel is installed. These are examples; available definitions decide.
   Keep run IDs and await every required completion; do not poll or launch duplicates.
5. **Synthesize.** Deduplicate by actual issue, record model attribution and
   disagreements. Apply `references/lead-judgment.md`; inspect the real caller/path
   yourself before accepting or dismissing. Consensus is signal, never proof.
6. **Judge.** Bucket findings into Act on (concrete material issue), Consider
   (valid tradeoff), Noted (not actionable now), Dismissed (wrong/context/style,
   with rationale). A lone security/correctness finding still warrants investigation.

Return Intent; Reviewers (actual runtime/provider/model, run status, count);
Act on / Consider / Noted / Dismissed with evidence and remedies; Agreement map;
unreviewed areas/failures. No findings is valid. Failed/incomplete review is not approval.
For PR work, prefer `thermos` as the one combined review unless a distinct
interrogation was explicitly requested; don't automatically stack redundant review runs.
