# Review routing

Read [the workflow contract](workflow-contract.md) first. This plugin is skills only:
never install agents, override `reviewer`, pin models, or touch credentials to run it.

## Standard review: built-in `reviewer`

Call `agent({agent_id: "reviewer", prompt: brief})`. Each call is a fresh context
that normally inherits the parent's model. Thermos makes two calls in one batch,
each with a different full rubric. Same-model review is the normal mode, not a
fallback, but two lenses are not model diversity. If a user override binds a
different model, report the actual binding and leave it alone.

The reviewer has read tools only: no shell, no delegation. So the parent:

- Collects diffs, history, PR discussion, and validation results itself, and puts
  the scoped diff, full rubric, constraints, and needed source in each prompt (or in
  an immutable snapshot the child can read). Never tell a child to run Git or builds.
- Gets committed source through Git, not live files. A child must not swap a supplied
  snapshot for the mutable worktree.
- Reports missing context or tools. Missing coverage or an agent error is never approval.
- Keeps run IDs and waits for every required result. No polling, no duplicates,
  no finishing after one of two passes.
- Owns validation (max 8 build jobs, logs redirected). Reviewers don't edit, commit,
  publish, or run tests. Verify findings; don't count votes.

## Optional: cross-model `interrogate`

Only when the host exposes model-selecting delegation (e.g. T3 Code):

1. Find `orchestrator_capabilities` and `delegate_task` in the tool catalog and read
   their schemas. Use the live model catalog, not hard-coded IDs, and follow the
   host's delegation instructions.
2. Pick genuinely different model families. Send self-contained, read-only tasks
   with identical scope, intent, evidence, and rubric. Batch launches, keep task IDs,
   await all results, and use stable request IDs for retries. No top-level threads.
3. Report actual provider/model bindings, substitutions, failures, and gaps. A failed
   task is not a clean review. Never change credentials, install toolchains, or wrap
   `rho run` as a homemade model runner.

Without such delegation, say **cross-model interrogation is unavailable in this
session**. Offer a same-model `reviewer` pass, run it only if the user accepts, and
never call it cross-model. Thermos and the other skills still work.

Model fields belong to the host's API. Rho's native `agent` takes only `agent_id`
and `prompt`.
