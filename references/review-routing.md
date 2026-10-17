# Reviewer routing (Rho, not model-per-call)

Read the workflow contract first. Rho binds providers/models in **agent definitions**,
not in `agent` arguments. Standard Agent Plugins currently discover skills/MCP only;
`agents/` in this package is an explicitly installed companion, not a manifest extension.
Run `python3 scripts/install-agents.py --preset matt` from the checkout (or installed
plugin root) to install Matt's panel. The generic preset installs native provider
examples instead. Existing differing files are refused; inspect/edit them yourself.

## Panel selection

1. Inspect `rho` action `agents` to reload definitions and see invalid entries.
   Use only IDs actually available. Read their definitions to establish actual
   runtime/provider/model; an ID or persona name does not prove model diversity.
2. Use a panel explicitly requested by the user. Otherwise prefer Matt's installed
   pair `pstack-reviewer-openai` (OpenAI Codex) and `pstack-reviewer-cliproxy`
   (Claude through the configured cliproxyapi provider). If that pair is not installed,
   choose available definitions from different model families below.
3. `interrogate` requires different model families, not two personas on one model.
   Thermos requires two independent passes (correctness/security and quality);
   prefer the same cross-family pair. Assign a pass in each prompt, not in the model.
4. A loaded definition is not proof of working credentials. A bind/auth/model/runtime
   failure is a failed reviewer, not "no findings". Report the failed ID and raw error.
   Use another already-configured **distinct family** only with the substitution
   disclosed. Do not change models, credentials, aliases, or global configuration to
   make a review appear successful. If diversity is unavailable, report the blocker.
   Only with explicit user acceptance may thermos use `pstack-reviewer-local` for
   both passes; label it same-model/degraded and never call it cross-model review.
5. Batch independent `agent` calls with `agent_id` / `prompt`. There is no `model`,
   `readonly`, `subagent_type`, or `run_in_background` call field. The definitions
   withhold write/edit tools, but shell access is not a sandbox: read-only behavior
   is also an explicit instruction. Do not claim OS-enforced read-only isolation.
6. Supply identical pinned scope, intent, diff/context and repository constraints
   to each reviewer. Include the actual rubric/skill body and all relevant referenced
   instructions, not merely a path. Reviewers may inspect surrounding source with
   available tools; no child builds, edits, commits, pushes, or nested review runs.
   For committed scope, use `git show <head>:<path>`, `git grep ... <head>` and
   `git diff <base> <head>`, or a parent-supplied immutable snapshot. Do not use
   live-worktree reads for pinned source: even a clean checkout can change later.
7. Retain both run IDs, wait for both terminal results through automatic delivery,
   and investigate concrete findings yourself. Unfinished/failed review is incomplete.
   Model agreement raises confidence but does not replace an execution trace or proof.

## Shipped definitions

| ID suffix (`pstack-reviewer-…`) | Runtime / provider | Model |
| --- | --- | --- |
| `openai` | rho / openai-codex | gpt-6.1-sol |
| `cliproxy` | rho / cliproxyapi (custom) | anthropic/claude-opus-5-5 |
| `anthropic` | rho / anthropic | claude-opus-5-5 |
| `google` | rho / google | gemini-2.5-pro |
| `xai` | rho / xai | grok-4.7 |
| `antigravity` | antigravity / host sign-in | gemini-3.8-flash-high |
| `claude-cli` | claude-cli / host sign-in | claude-opus-5-5 |
| `local` | rho / inherits parent | inherits parent |

Models are editable examples, not permanent promises or proof of account access.
Check `/model` and provider documentation before changing a definition. Native pins use
`model-policy: require`; never depend on fallback behavior. No secrets are packaged.
Matt preset: openai + cliproxy + local. Native preset: openai + anthropic + google +
xai + local. Optional CLI runtimes must be installed/logged in separately and may
have permission-mode restrictions. The installer never installs toolchains or logins.

Rho references: `docs/subagents.md`, `docs/subagents/definition-schema.md`,
`docs/integrations/plugins.md` in https://github.com/matthewyjiang/rho.
