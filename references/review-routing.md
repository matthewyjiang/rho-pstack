# Review routing

Read [the workflow contract](workflow-contract.md) first. Never edit agent
definitions or touch credentials to make a review run.

## Agents

The plugin ships the two thermos lenses as Rho agents in
`io.github.matthewyjiang.rho/agents/`. Each one loads its own rubric skill, so the
parent sends only the shared scope/evidence packet, never the rubric text.

| Agent id | Lens | Rubric it loads |
| --- | --- | --- |
| `thermo-nuclear-review-subagent` | correctness/security | `thermo-nuclear-review` |
| `thermo-nuclear-code-quality-review-subagent` | code quality | `thermo-nuclear-code-quality-review` |

Both inherit the parent's model; their frontmatter holds the tool list. Other
review passes (interrogate, design perspectives, trail audits) use Rho's built-in
`reviewer`.

## Fall back

If a plugin agent is not loaded (a Rho build without plugin-agent support, the
plugin disabled, or an invalid override), or its run fails, including a lens that
could not load its rubric, relaunch that pass on `reviewer`. Use the same packet
and prepend the line the agent itself carries: "You are the `<lens>` lens of a
thermos review. Load the `<rubric>` skill and follow it as the complete rubric."
Report the failed id, the raw error and the substitution. A failed run is never
"no findings".

## Models

Agents run on the parent's model unless the call passes `model`
(`provider/model`, a catalog id, or an `@alias`), on Rho builds with per-call
model selection. Use only models the user named or configured. On supporting
builds an unknown model or missing credentials is an explicit error: report it and
do not guess another id. **Older Rho silently ignores the field** and runs the
parent's model, so a run counts as model-selected only when its receipt shows the
bound provider/model and it matches. A receipt without a model means the selection
is unproven: use host delegation or report cross-model review as unavailable. An
agent id or a requested model is not proof of what ran. Two passes on one model
family are not cross-model review.

## Brief every reviewer the same way

Reviewers are read-only and do not delegate. Shell, where a reviewer has it, is for
read-only Git/`gh` inspection; that limit is an instruction, not a sandbox. For
untrusted or external PRs, prefer a permission mode where delegated shell fails
closed (`supervised`, `allow_edits`, `plan`). The parent:

- Resolves pinned base/head (or a pinned snapshot) and puts the scope, diff or
  changed paths, constraints and needed source in each prompt. Reviewers with a
  shell may read more through `git show <head>:<path>` or `git diff <base> <head>`;
  a reviewer without one, or whose delegated shell will be denied (non-bypass
  permission modes), gets the pinned source it needs inline. Never substitute the
  mutable worktree for pinned source.
- Reports missing context or tools. Missing coverage or an agent error is never approval.
- Keeps run IDs and waits for every required result. No polling, no duplicates,
  no finishing after one of two passes.
- Owns validation (max 8 build jobs, logs redirected). Reviewers don't edit, commit,
  publish, or run builds/tests, even where their own instructions allow it.
  Verify findings; don't count votes.

## Other models through the host

When per-call `model` is unavailable, or a model is outside Rho's catalog, use host
model-selecting delegation if it exists, e.g. T3 Code:

1. Find `orchestrator_capabilities` and `delegate_task` in the tool catalog and read
   their schemas. Use the live model catalog, not hard-coded IDs, and follow the
   host's delegation instructions.
2. Send self-contained, read-only tasks with identical scope, intent, evidence and
   rubric. Batch launches, keep task IDs, await all results, and use stable request
   IDs for retries. No top-level threads.
3. Report actual provider/model bindings, substitutions, failures and gaps. Never
   change credentials, install toolchains, or wrap `rho run` as a homemade model runner.
