# Review routing

Read [the workflow contract](workflow-contract.md) first. Never edit agent
definitions, pin models in calls, or touch credentials to make a review run.

## Reviewers

Rho binds models in agent definitions, not in `agent` arguments, so the plugin ships
read-only reviewers pinned to different model families in
`io.github.matthewyjiang.rho/agents/`:

| Agent id | Family | Default binding |
| --- | --- | --- |
| `pstack-reviewer-openai` | OpenAI GPT | `openai-codex` / `gpt-6.1-sol` |
| `pstack-reviewer-anthropic` | Anthropic Claude | `cliproxyapi` / `anthropic/claude-opus-5-5` |
| `reviewer` (built-in) | parent's family | inherits the parent model |

The id names the family; the binding is Matt's default. A user or project agent file
with the same id replaces it, so other setups rebind there, not here. Read the
actual binding from the run result or `rho` action `agents`. An id is not proof of a
model, and a loaded definition is not proof of working credentials.

## Pick and fall back

1. Use a panel the user asked for. Otherwise pick shipped reviewers by family as the
   calling skill says, then batch the `agent` calls (`agent_id` and `prompt` only).
2. If an id is not loaded (older Rho without plugin agents, plugin disabled, or an
   invalid override) or its run fails to bind, authenticate or finish, relaunch that
   pass with the built-in `reviewer` and the same prompt. Report the failed id, the
   raw error and the substitution. A failed run is never "no findings".
3. `reviewer` inherits the parent's family. Count it as that family when a skill
   needs diversity, and never call two passes on one family cross-model.

These are `runtime: rho` definitions, so they also work under T3 Code host
delegation: the child Rho loads the same definition from plugin discovery.

## Brief every reviewer the same way

Reviewers are read-only and do not delegate. Shell, where a reviewer has it, is for
read-only Git/`gh` inspection, not a sandbox. The parent:

- Resolves pinned base/head (or a pinned snapshot) and puts the scope, diff or changed
  paths, full rubric, constraints and needed source in each prompt. Reviewers with a
  shell may read more through `git show <head>:<path>` or `git diff <base> <head>`;
  the built-in `reviewer` may lack a shell, so include what it cannot fetch. Never
  substitute the mutable worktree for pinned source.
- Reports missing context or tools. Missing coverage or an agent error is never approval.
- Keeps run IDs and waits for every required result. No polling, no duplicates,
  no finishing after one of two passes.
- Owns validation (max 8 build jobs, logs redirected). Reviewers don't edit, commit,
  publish, or run tests. Verify findings; don't count votes.

## Other models through the host

When the shipped families aren't enough (the user asks for another model, or a
shipped reviewer failed and diversity is required), use host model-selecting
delegation if it exists, e.g. T3 Code:

1. Find `orchestrator_capabilities` and `delegate_task` in the tool catalog and read
   their schemas. Use the live model catalog, not hard-coded IDs, and follow the
   host's delegation instructions.
2. Send self-contained, read-only tasks with identical scope, intent, evidence and
   rubric. Batch launches, keep task IDs, await all results, and use stable request
   IDs for retries. No top-level threads.
3. Report actual provider/model bindings, substitutions, failures and gaps. Never
   change credentials, install toolchains, or wrap `rho run` as a homemade model runner.
