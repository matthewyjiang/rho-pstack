# rho-pstack

Matt's engineering workflow as a [Rho Agent Plugin](https://agent-plugins.org/specification):
design first, prove the result, and run one combined `thermos` review per PR.
It ships skills plus two read-only reviewer agents pinned to different model
families. There is no installer.

A port of Lauren Tan's **pstack** v0.15.25 and Cursor's **thermos** v1.0.0.

## Install

```bash
git clone git@github.com:matthewyjiang/rho-pstack.git ~/projects/rho-pstack
rho plugins install "$HOME/projects/rho-pstack"   # absolute path required
```

Start a new Rho session so it picks up the skills and agents. To update, `git pull` and
reinstall with `--force`. For development, use `rho plugins link` in place of `install`.

## Use

```text
$pstack implement this feature
$architect sketch the ownership model; stop before implementing
$why why is this retry limit here?
$thermos review this PR
$interrogate challenge this design with a different model
```

`/skill:<name>` also works, and the model can load skills on its own.

| Group | Skills |
| --- | --- |
| Entry | `pstack` (routes to the others) |
| Design | `how`, `why`, `architect`, `sharpen` |
| Proof | `blast-radius`, `prove-it-works`, `show-me-your-work`, `correct` |
| Review | `thermos`, `thermo-nuclear-review`, `thermo-nuclear-code-quality-review`, `interrogate` |
| Principles | 15 `principle-*` skills |

- **thermos** runs two reviewers in parallel, correctness/security on
  `pstack-reviewer-openai` and code quality on `pstack-reviewer-anthropic`, then
  merges the results into one verdict. If either agent isn't loaded or fails, that
  lens falls back to Rho's built-in `reviewer`, which uses the parent's model.
- **interrogate** challenges a design across at least two model families, using the
  shipped reviewers or a host that delegates to other models, such as T3 Code's
  `delegate_task`. Without two families it says cross-model review is unavailable.

## Agents

Agent Plugins 1.0 standardizes only skills and MCP, so the agents live in Rho's
extension directory, `io.github.matthewyjiang.rho/agents/` (spec §8.2). Other
clients ignore it.

| Agent | Model family | Default binding |
| --- | --- | --- |
| `pstack-reviewer-openai` | OpenAI GPT | `openai-codex` / `gpt-6.1-sol` |
| `pstack-reviewer-anthropic` | Anthropic Claude | `cliproxyapi` / `anthropic/claude-opus-5-5` |

Both are `runtime: rho` with read, search, `skill` and shell tools and no edit
tools, so they also run under T3 Code host delegation.

- **Rho version.** Loading these needs a Rho build with plugin-agent support. Older
  builds load only the skills, and the review skills fall back to `reviewer`.
- **Rebinding.** The bindings are Matt's setup; `cliproxyapi` is a custom provider.
  To use your own model, put an agent file with the same id in `~/.agents/agents`,
  `~/.rho/agents` or `<project>/.agents/agents`. User and project agent files
  override plugin agents with the same id.
- **Plugin scope.** A project-scope plugin overrides a user-scope one. A disabled
  plugin contributes no agents, and project plugins load only with
  `RHO_TRUST_PROJECT_PLUGINS=1`.
- **Files.** Agent files must resolve inside the plugin root; symlinks pointing
  outside it are rejected.

Repository `AGENTS.md`, user instructions, and permissions always win. See
[workflow-contract.md](references/workflow-contract.md) and
[review-routing.md](references/review-routing.md) for the rules the skills follow.

## License

MIT. Derived from [cursor/plugins](https://github.com/cursor/plugins/tree/09d06eb4b97a1020ab31e84030e38baf1099c7dc)
at commit `09d06eb`: `pstack/` (© 2026 Lauren Tan) and `thermos/` (© 2026 Cursor).
The original notices are in [licenses/](licenses/). This is an unofficial port.
