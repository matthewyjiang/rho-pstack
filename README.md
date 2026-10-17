# rho-pstack

Matt's general engineering workflow for **any project**, packaged as a standard
[Rho Agent Plugin](https://agent-plugins.org/specification) 1.0.0.

A curated port of **Lauren Tan's pstack v0.15.25** plus **Cursor's thermos v1.0.0**:
design before committing to a shape, prove the actual result, and run one combined
thermos review for every PR. No autonomous shipping mode and no imposed prose style.

## Install

Requires Rho with Agent Plugins support (tested on **Rho 2.24.0**), Git and Python 3
for the explicit reviewer setup/checks. The skills themselves are Markdown; no MCP
server, package-manager dependencies, toolchain installer or startup hook is added.
Private clone requires GitHub access to this repo.

```bash
git clone git@github.com:matthewyjiang/rho-pstack.git ~/projects/rho-pstack
rho plugins install "$HOME/projects/rho-pstack"
python3 ~/projects/rho-pstack/scripts/install-agents.py --preset matt
rho plugins inspect rho-pstack --json
```

Use an **absolute path** with `rho plugins install` on the tested Rho release.
This installs globally under `~/.agents/plugins/rho-pstack`, so the workflow is
available in every project. Start a new Rho session to refresh the skill catalog.
The setup command installs only namespaced `pstack-reviewer-*` files under
`~/.rho/agents`; it never changes existing built-in/custom reviewers, AGENTS.md,
provider configuration, credentials or model aliases. Differing files and symlinks
are refused rather than overwritten; identical installs are safe to repeat.

**Why a second command?** Rho's standard plugin format discovers `skills/` and
`mcp.json`, not agent definitions. `agents/` here is a portable explicit companion,
not an unsupported `plugin.json` extension or hidden install-time execution.
The installed plugin also contains the script and definitions, so setup can run
from `~/.agents/plugins/rho-pstack/scripts/install-agents.py` after a copied install.

Matt's preset uses his configured `openai-codex` and `cliproxyapi` routes. For native
API providers instead:

```bash
python3 ~/projects/rho-pstack/scripts/install-agents.py --preset native
# Or explicitly select optional existing CLI runtimes:
python3 ~/projects/rho-pstack/scripts/install-agents.py --only antigravity --only claude-cli
```

These are definitions, **not logins**. Inspect/edit the selected definitions to match
your actual Rho catalog and credentials. No API keys are bundled. The native preset
installs OpenAI Codex, Anthropic, Google, xAI and an explicit parent-model fallback;
optional Antigravity and Claude Code require their own installed runtime/sign-in.
See [review routing](references/review-routing.md) for all IDs and failure handling.

For local development, `rho plugins link "$HOME/projects/rho-pstack"` can replace a
copied install with `--force` after inspection. To update a copied install after a
pull, rerun `rho plugins install "$HOME/projects/rho-pstack" --force`. Reviewer
changes remain separately reviewed/installed; the setup script never force-overwrites
customizations. Rho does not support remote GitHub plugin installation or automatic
updates yet, so clone first rather than `rho plugins install owner/repo`.

Project-scoped install is optional: run `rho plugins install /absolute/path/to/rho-pstack
--scope project` from that repository, and explicitly grant project plugin trust
with `RHO_TRUST_PROJECT_PLUGINS=1`. Project-scoped agent setup is a separate choice:
`--destination /repo/.agents/agents`, requiring `RHO_TRUST_PROJECT_AGENTS=1`.
Do not grant trust automatically to cloned repository code.

## Use

In a fresh Rho interactive/ACP session:

```text
$pstack implement this feature, preserving the repository's existing API
$architect sketch the ownership model; stop before implementing
$why why is this retry limit here?
$thermos review this PR against its actual target branch
$interrogate challenge this design from different model families
```

Rho also supports `/skill:<name>`. The model may load a relevant skill with the
`skill` tool. For CLI automation, ask it to load the named skill explicitly, e.g.
`rho run "Load the pstack skill and investigate this failure; do not edit yet"`.
Don't assume interactive skill-mention preprocessing in every CLI/host path.

`pstack` is a small router. It doesn't turn on autonomous operation, write PRs,
change the response style, or grant permission to merge. **Thermos is the one
combined review on every PR when using this workflow**, not an installed GitHub
hook, mandatory CI check, or promise that an unprompted agent will always invoke it.
For a guaranteed requested review, invoke `thermos` directly.

## Included skills

All **28** skills have frontmatter names matching their directories and explicitly
set `disable-model-invocation: false`. They may be selected by the model because
these are general workflow tools, not privileged commands. Selection does not
expand the task's authority. Review skills are read-only; `architect` respects
design-only requests/checkpoints; `correct` only applies in-scope prevention.

| Group | Skills |
| --- | --- |
| Entry | `pstack` |
| Design first | `how`, `why`, `architect`, `sharpen` |
| Proof | `blast-radius`, `prove-it-works`, `show-me-your-work`, `correct` |
| Independent challenge | `interrogate` |
| Combined PR review | `thermos`, `thermo-nuclear-review`, `thermo-nuclear-code-quality-review` |

Retained principles (all `principle-` prefixed):

- `boundary-discipline`, `model-the-domain`, `type-system-discipline`
- `build-the-lever`, `guard-the-context-window`, `sequence-verifiable-units`
- `experience-first`, `explain-the-number`, `fix-root-causes`
- `make-operations-idempotent`, `separate-before-serializing-shared-state`
- `migrate-callers-then-delete-legacy-apis`, `minimize-reader-load`
- `subtract-before-you-add`, `test-behavior-not-implementation`

### Principle consolidation

| Upstream principle | Port decision |
| --- | --- |
| `attack-the-premise` | Merged into `principle-fix-root-causes` |
| `encode-lessons-in-structure` | Merged into `correct` |
| `exhaust-the-design-space` | Merged into `architect` |
| `foundational-thinking` | Merged into `principle-model-the-domain` |
| `laziness-protocol` | Merged into `principle-subtract-before-you-add` |
| `outcome-oriented-execution` | Merged into `principle-sequence-verifiable-units`, bounded by repository gates |
| `redesign-from-first-principles` | Merged into `architect`'s reassess phase |
| `prove-it-works` | Promoted to the requested `prove-it-works` proof skill |
| `never-block-on-the-human` | Dropped; reasonable in-scope decisions are fine, but material choices/authority still require asking |

### Thermos and interrogate

Thermos runs the **complete correctness/security rubric** and **structural-quality
rubric** as two independent same-batch `agent` calls, then waits for both and
produces one evidence-backed verdict. It preserves upstream's cross-module/devex/
feature-gate audit, intended-breakage calibration, code-judo lens, and fresh audit
before reading other PR findings. Full rubrics and identical pinned intent/scope/
evidence are supplied in the prompts. The parent owns discussion checks and all
build/test validation; child reviewers do not modify files or run builds.

Interrogate applies the shared adversarial rubric to reviewers from **different
model families**, then sorts findings into Act on / Consider / Noted / Dismissed.
Actual provider/model bindings live in individual agent definitions, not unsupported
per-call `model` parameters. Missing agents/auth/runtime, failed audits and unavailable
diversity are explicit blockers. There is no silent substitution to the parent model.
Same-model thermos requires explicit user acceptance and is labeled degraded.
Shell-enabled reviewer definitions are instructionally read-only, **not OS sandboxes**.

## Changes and exclusions

- Cursor `Task`, background flags, model-per-call slugs and `.cursor` model rules
  became Rho `agent` calls and installed provider-bound definitions. Independent
  children launch together and completion is delivered by Rho; no polling loops.
- Transcript-path assumptions became `sessions` with `scope: current` plus supplied
  evidence receipts. Children receive context explicitly, not guessed parent paths.
- The design methods remain, but simple questions no longer require a fan-out;
  architecture candidates do not need writable clone/worktree orchestration.
- Upstream fixed file-line/read-time limits became measured growth, cohesion,
  ownership and reader-load checks. No universal 1,000-line approval blocker.
- No `poteto-mode`, its playbooks/bootstrap/watchers, `no-comments`, `comment-sicko`,
  `poteto-agent`, writing-style skills/rules, PR-writing rules, autonomy, “land even
  if CI flakes”, unconditional human-avoidance or automatic merges.
- The upstream optional arena/swarm, setup/help, teaching, reflection/recall,
  automation, UI, language-specific and verification-skill-generator bundles are
  not included. Needed design/proof methods are retained without their dependencies.
- Comments remain useful where the repository wants them. No CHANGELOG or
  autogenerated upstream assets are maintained by hand.

Every skill reads the [workflow contract](references/workflow-contract.md).
The repository's AGENTS.md, user's scope/merge rules and permissions take priority.
No hooks modify those files or enforce policy outside an invoked skill.

## Validate

```bash
cd ~/projects/rho-pstack
python3 scripts/check-package.py
python3 -m unittest discover -s tests -v
rho plugins inspect rho-pstack --json
python3 scripts/verify-rho.py
```

The package checker checks names, invocation policy, local-link containment and
upstream notices; Rho itself parses the real YAML/manifest. The focused tests drive
the installer (idempotency, no overwrite, symlink refusal, selection preflight) and
TSV helper (append behavior and untrusted-cell sanitation). `verify-rho.py` compares
Rho's installed inventory and installed file bytes against this checkout. Use its
`--live` option to exercise actual skill tool loading with your configured model;
it costs a model request and reports any load failure. See
[VALIDATION.md](VALIDATION.md) for the checks performed for this release.

Loose/built-in skills outrank plugin skills; near project plugins can outrank this
user install. Inventory alone doesn't prove which body an active session uses.
Restart sessions after updates and inspect tool-load source paths for conflicts.
`rho plugins disable rho-pstack` disables skills for new sessions. Removing the
plugin doesn't remove explicitly installed companion reviewer files; remove only
the `pstack-reviewer-*` definitions you installed if you no longer want them.

## Attribution and license

MIT. This work derives from **Lauren Tan's pstack** and **Cursor's thermos**, pinned
to canonical `cursor/plugins` commit `09d06eb4b97a1020ab31e84030e38baf1099c7dc`.
Both upstream MIT copyright/permission notices are retained verbatim in `licenses/`.
See [UPSTREAM.md](UPSTREAM.md) for sources, exact versions, license audit and file
provenance, and [LICENSE](LICENSE) for the combined port's license. This is Matt's
custom port, not an official Cursor or upstream release.
