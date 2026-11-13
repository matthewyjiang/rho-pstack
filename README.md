# rho-pstack

Matt's engineering workflow as a [Rho Agent Plugin](https://agent-plugins.org/specification):
design first, prove the result, and run one combined `thermos` review per PR.
It ships skills plus three agents: the two thermos review lenses and Comment Sicko.
There is no installer and no model pin.

A port of Lauren Tan's [**pstack**](https://github.com/cursor/plugins/tree/main/pstack) v0.15.36 and Cursor's [**thermos**](https://github.com/cursor/plugins/tree/main/thermos) v1.0.0.

## Install

```bash
rho plugins install https://github.com/matthewyjiang/rho-pstack.git
```

Start a new Rho session so it picks up the skills and agents. To update, use `rho plugins update rho-pstack`

## Use

```text
$pstack implement this feature
$architect sketch the ownership model; stop before implementing
$why why is this retry limit here?
$thermos review this PR
$interrogate challenge this design with a different model
$unslop tighten this README
```

`/skill:<name>` also works, and the model can load skills on its own.

| Group | Skills |
| --- | --- |
| Entry | `pstack` (routes to the others) |
| Design | `how`, `why`, `architect`, `sharpen` (user-invoked; returns a rewritten prompt) |
| Proof | `blast-radius`, `prove-it-works`, `show-me-your-work`, `correct` |
| Review | `thermos`, `thermo-nuclear-review`, `thermo-nuclear-code-quality-review`, `interrogate` |
| Writing | `unslop` (user-invoked only) |
| Principles | 15 `principle-*` skills |

- **thermos** runs its two lens agents in parallel, one for correctness/security
  and one for code quality, then merges the results into one verdict. Both use the
  parent's model. If a lens agent isn't loaded or fails, that lens falls back to
  Rho's built-in `reviewer`.
- **interrogate** challenges a design across at least two model families, chosen
  per call through the `agent` tool's `model` field or through a host that delegates
  to other models, such as T3 Code's `delegate_task`. Each adversary must hand back
  a runnable repro; the parent runs them and keeps only findings the run proves.
  Without two families it says cross-model review is unavailable.

## Agents

Agent Plugins 1.0 standardizes only skills and MCP, so the agents live in Rho's
extension directory, `io.github.matthewyjiang.rho/agents/` (spec §8.2). Other
clients ignore it.

| Agent | Lens | Loads rubric |
| --- | --- | --- |
| `thermo-nuclear-review-subagent` | correctness/security | `thermo-nuclear-review` |
| `thermo-nuclear-code-quality-review-subagent` | code quality | `thermo-nuclear-code-quality-review` |
| `comment-sicko` | comment deletion | `how` / `why` when a comment's claim needs proof |

The two lenses mirror upstream Thermos' two subagents. Each loads its rubric skill itself,
so the thermos prompt carries only the scope and evidence. Both inherit the parent's
model, and a per-call `model` can move a lens to another one. Because they are
`runtime: rho`, they also run under T3 Code host delegation. Neither has edit
tools; their shell is limited to read-only Git/`gh` by instruction, not by sandbox.

`comment-sicko` is pstack's comment hater: hand it a diff or file scope and it
deletes comments outside a short keep list, flagging workaround code `MUST KILL`.
It has the `edit` tool and is told to touch comments only, never application code;
review its diff before keeping it. Upstream drives it through `/no-comments`, which
this port does not ship, so call it directly with the `agent` tool.

- **Rho version.** Loading these needs a Rho build with plugin-agent support. Older
  builds load only the skills, and `thermos` falls back to `reviewer`.
- **Overrides.** An agent file with the same id in `~/.agents/agents`,
  `~/.rho/agents` or `<project>/.agents/agents` (project files need
  `RHO_TRUST_PROJECT_AGENTS=1`) overrides the plugin's. It replaces the whole
  definition, so start from a copy of the shipped file and keep `tools`; omitting
  `tools` grants every tool, including edits.
- **Plugin scope.** A project-scope plugin overrides a user-scope one. A disabled
  plugin contributes no agents, and project plugins load only with
  `RHO_TRUST_PROJECT_PLUGINS=1`.
- **Files.** Agent files must resolve inside the plugin root; symlinks pointing
  outside it are rejected.

Repository `AGENTS.md`, user instructions, and permissions always win. See
[workflow-contract.md](references/workflow-contract.md) and
[review-routing.md](references/review-routing.md) for the rules the skills follow.

## License

MIT. Derived from [cursor/plugins](https://github.com/cursor/plugins/tree/ec569379616a4826b98f0f0a205dd3411b573611)
at commit `ec56937`: `pstack/` (© 2026 Lauren Tan) and `thermos/` (© 2026 Cursor).
The original notices are in [licenses/](licenses/); skill and agent files carry no
per-file attribution. This is an unofficial port.
