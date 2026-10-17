# rho-pstack

Matt's general engineering workflow for **any project**, packaged as a standard
[Rho Agent Plugin](https://agent-plugins.org/specification) 1.0.0.

A curated port of **Lauren Tan's pstack v0.15.25** plus **Cursor's thermos v1.0.0**:
design first, prove the actual result, and run one combined thermos review for each
PR. **Skills only: no custom agents, model pins, companion installer or MCP server.**

## Install

Requires Rho with Agent Plugins support (tested on **Rho 2.24.0**) and Git/private
repository access. Python 3 is needed only for the optional package/test scripts;
the skills themselves are Markdown and need no setup script or toolchain install.

```bash
git clone git@github.com:matthewyjiang/rho-pstack.git ~/projects/rho-pstack
rho plugins install "$HOME/projects/rho-pstack"
```

Use an **absolute path** on the tested Rho release. The package is copied to
`~/.agents/plugins/rho-pstack`, making its skills available in every project.
**Start a fresh Rho session** to refresh the skill catalog. Installation validates
the manifest and copies files; it executes no package code and changes no AGENTS.md,
agent definitions, provider settings, credentials or model aliases.

Update a copied install with:

```bash
git -C ~/projects/rho-pstack pull
rho plugins install "$HOME/projects/rho-pstack" --force
```

For development, `rho plugins link "$HOME/projects/rho-pstack" --force` can replace
a copied install with a symlink after inspection. Remote GitHub plugin installation
and automatic updates are not currently supported by Rho, so clone first.

For a project-only install, run `rho plugins install /absolute/path/to/rho-pstack
--scope project` from that repository and explicitly grant project plugin trust
with `RHO_TRUST_PROJECT_PLUGINS=1`. Do not grant trust to cloned code automatically.
No project-agent trust or agent installation is needed.

### Moving from v0.1

v0.2 removes the companion installer and all packaged reviewer definitions.
Reinstall the plugin with `--force`. If you installed v0.1's companion definitions,
move only those `pstack-reviewer-*` files out of `~/.rho/agents` (preserve any edits
in a backup); Rho's plugin removal/update does not manage loose agents.

An existing `~/.rho/agents/reviewer.md` or `~/.agents/agents/reviewer.md` overrides
Rho's built-in reviewer. This plugin neither needs nor creates such an override.
If you want the stock reviewer, back up and move that definition outside discovery;
do not remove unrelated agents. The local migration for Matt also removed his
requested existing `reviewer` override, with a recoverable backup.

## Use

```text
$pstack implement this feature, preserving the repository's existing API
$architect sketch the ownership model; stop before implementing
$why why is this retry limit here?
$thermos review this PR against its actual target branch
$interrogate challenge this design using host-backed model diversity
```

Rho supports `$<name>` mentions in interactive/ACP prompts and `/skill:<name>`.
The model may also select a relevant skill with the `skill` tool. For CLI automation,
ask it to load a skill explicitly, e.g. `rho run "Load the pstack skill and investigate
this failure; do not edit yet"`; do not assume mention preprocessing in every host.

`pstack` is a lightweight router, not autonomous operation, a writing style or merge
authority. **Thermos is the one combined PR review when using this workflow**,
not a GitHub hook, enforced CI status check or promise of unprompted invocation.
Invoke `thermos` directly when you want to explicitly request that review.

## Included skills

All **28** skills have names matching their directories and explicitly set
`disable-model-invocation: false`. Model selection does not expand task authority.
Review is read-only, architecture respects design-only requests/checkpoints, and
`correct` applies only requested/in-scope structural prevention.

| Group | Skills |
| --- | --- |
| Entry | `pstack` |
| Design first | `how`, `why`, `architect`, `sharpen` |
| Proof | `blast-radius`, `prove-it-works`, `show-me-your-work`, `correct` |
| Optional host-backed challenge | `interrogate` |
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
| `outcome-oriented-execution` | Merged into `principle-sequence-verifiable-units`, subordinate to repository gates |
| `redesign-from-first-principles` | Merged into `architect`'s reassess phase |
| `prove-it-works` | Promoted to the proof skill `prove-it-works` |
| `never-block-on-the-human` | Dropped; material choices/authority still require asking |

### Thermos: portable parallel review

Thermos calls Rho's existing **`reviewer` twice in parallel**, supplying the complete
correctness/security rubric to one and structural-quality rubric to the other.
Each is a separate context; the parent waits for both and synthesizes one verdict.
**Both normally inherit the parent model. Same-model review is the default, not a
degraded mode, and is never presented as cross-model independence.** Existing user
agent overrides remain user choices; this plugin does not alter them.

The parent supplies identical pinned intent/scope/evidence and full respective
rubrics, gathers all Git/PR context and owns validation/discussion checks. The stock
reviewer has read tools and **no shell**, so it receives evidence inline or through
a readable immutable snapshot, rather than instructions to run Git or builds.
Thermos preserves upstream's cross-module/devex/feature-gate audit, intended-breakage
calibration, code-judo lens and fresh audit before reading other review findings.

### Interrogate: optional host model selection

Cross-model interrogation uses host-provided delegation when available. In T3 Code,
the skill discovers `orchestrator_capabilities` / `delegate_task`, selects genuinely
different available model families, supplies identical rubrics/evidence, and
synthesizes Act on / Consider / Noted / Dismissed findings. It installs nothing and
hard-codes no provider/model IDs.

Without such an API, it explicitly reports **cross-model interrogation unavailable**.
It can offer an ordinary same-model reviewer pass, but runs that substitution only
if accepted and never labels it cross-model. Thermos/design/proof workflows remain
usable in standalone Rho. See [review routing](references/review-routing.md).

## Changes and exclusions

- Cursor Task/background/model-per-call conventions became ordinary Rho reviewer
  calls with full prompts. Optional model selection belongs to a host API, not
  unsupported native `agent` fields. No custom agents or homemade model runner.
- Transcript paths became current-scope `sessions` evidence and explicit receipts;
  children receive context rather than guessed parent transcript paths.
- Simple questions need no fan-out. Design alternatives do not require writable
  worktree orchestration. Fixed file/read-time limits became measured cohesion,
  ownership and reader-load checks, not universal line-count blockers.
- No poteto-mode/autonomy/playbooks/watchers, no-comments/comment-sicko, PR-writing
  or prose-style mandates, “land even if CI flakes”, unconditional human avoidance,
  automatic commits/pushes/merges, or repository-policy overrides.
- Optional arena/swarm, setup/help, teaching, reflection/recall, automation, UI,
  language-specific and verification-skill-generator bundles are excluded. Their
  needed design/proof methods are retained without those dependencies.
- Comments remain useful. No CHANGELOG or autogenerated upstream assets are
  manually maintained.

Every skill reads the [workflow contract](references/workflow-contract.md).
Repository AGENTS.md, user scope/merge rules and permissions take priority.

## Validate

```bash
cd ~/projects/rho-pstack
python3 scripts/check-package.py
python3 -m unittest discover -s tests -v
rho plugins inspect rho-pstack --json
python3 scripts/verify-rho.py
```

Package checks cover names, invocation policy, local-link containment and upstream
notices; Rho parses real YAML/manifest. Two focused behavioral tests cover TSV append,
single-line cells, quote-safe parsing and formula neutralization. The verifier
compares installed inventory and runtime-asset bytes to the checkout. `--live`
exercises skill calls using the configured model (billable). Rho's CLI receipts
omit arguments/loaded-source bodies, so successful-call counts are runtime-verified,
but distinct-name coverage is model-reported, not independent per-source proof.
See [VALIDATION.md](VALIDATION.md) for release evidence and limits.

Loose/built-in skills outrank plugin skills; nearer project plugins can also win.
Restart after updates and inspect loaded source paths if names collide.
`rho plugins disable rho-pstack` disables it for new sessions; `rho plugins remove
rho-pstack --yes` removes the managed package. This version installs no loose agents
to clean up afterward.

## Attribution and license

MIT. Derived from **Lauren Tan's pstack** and **Cursor's thermos**, pinned to
`cursor/plugins` commit `09d06eb4b97a1020ab31e84030e38baf1099c7dc`.
Both upstream MIT notices are retained verbatim in `licenses/`. See
[UPSTREAM.md](UPSTREAM.md) for exact sources, versions, license audit and provenance,
and [LICENSE](LICENSE) for the port's license. This is Matt's custom port, not an
official Cursor or upstream release.
