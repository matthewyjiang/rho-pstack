# Validation

Validated with **Rho 2.24.0** and Python 3.13.5. This is a Markdown/plugin package;
no compiler build or toolchain installation is needed.

## Passed checks

- `python3 scripts/check-package.py`: matching directory/frontmatter names,
  explicit invocation policy, package-relative link containment and retained
  upstream MIT notices. Rho itself validates the manifest and real YAML.
- `python3 -m unittest discover -s tests -v`: four focused behavioral tests cover
  repeat installation, preservation/preflight refusal of differing files, symlink
  and invalid-selection refusal, append/single-line decision logs, and untrusted
  formula/quoted-field handling. Bash syntax inspection passes too.
- `rho plugins install /absolute/path/to/rho-pstack`: real user-scope copied install.
- `rho plugins inspect rho-pstack --json`: **28 skills**, loaded/enabled, no problems.
- `python3 scripts/verify-rho.py`: installed inventory and exact runtime-asset bytes
  match the checkout, including shared references, companion definitions/scripts,
  and license notices. This compares packaged definitions, not customized installed
  copies under `~/.rho/agents`.
- Live loading after the helper fix: **28 successful direct `skill` completion
  receipts**, with the model reporting all 28 requested names. Evidence:
  `/tmp/rho-pstack-live-2n32f8bu/`. The calls were sequential despite a batching
  request. Final instruction/documentation refinements were checked statically
  and compared against the final installed copy afterward.
- Rho `agents` diagnostics loaded **all eight companion definitions** in an
  isolated HOME fixture with **no invalid entries**. Only Matt's selected
  openai/cliproxy/local panel is installed in the real global agent directory.
  Evidence: `/tmp/rho-pstack-all-definitions.log`.

**Live-receipt limitation:** Rho's CLI event stream includes the tool name, call ID
and success/failure, but not its arguments or loaded-source body. The verifier
therefore checks successful-call counts and **model-reported** distinct-name coverage;
it does not independently attest per-name source identity. Inventory and installed
bytes are independently checked. The script fails on any observed failed/missing
call, unexpected tool/count, nonzero run exit or reported-name mismatch, but does
not advertise a stronger proof than this interface supplies.

A pre-existing loose `thermo-nuclear-code-quality-review` skill shadowed the plugin
and required direct invocation. The live test caught it; it was preserved under
`~/.rho/skill-backups/` outside discovery, then all requested loads succeeded.
No remaining conflicting loose names were found in this validation workspace.
Existing user instructions, ordinary reviewers and provider configuration were
not changed. Future loose/project skill collisions still need inspection.

## Parallel thermos test

The full initial package at `ed0c7229c1931d14126bb9f0096573ecd26acffd` was reviewed
against Git's empty tree using **one native Rho agent batch**. Both children
received identical pinned scope/intent/evidence and their respective full rubric.
Both completed with `state: ok`, with no authentication failure, retry or fallback:

| Lens | Agent / run ID | Actual runtime / provider / model |
| --- | --- | --- |
| Correctness/security | `pstack-reviewer-openai` / `b978f1` | rho / openai-codex / gpt-6.1-sol |
| Structural quality | `pstack-reviewer-cliproxy` / `5b800e` | rho / cliproxyapi / anthropic/claude-opus-5-5 |

Terminal runtime metadata corroborated the actual provider/model bindings. The
parent waited for both and synthesized one combined verdict. Exact prompts,
receipts and synthesis: `/tmp/rho-thermos-ed0c722-w5x3lzdo/`; CLI result:
`/tmp/rho-pstack-thermos-result.json`.

The review retained two P2 and two P3 issues in that initial snapshot. They were
addressed before publication: TSV quote serialization, overly strong live-coverage
claims, omitted shared-asset comparison, and a stale rationale-heading fragment.
A focused follow-up review through T3 on Claude Opus 5.5 confirmed the helper fix
and raised an immutable-read instruction gap plus log-format/evidence-documentation
issues. These were addressed with explicit `git show`/`git grep`/`git diff` pinned
reads, CSV-aware TSV-reading instructions, and this updated evidence record.
The published version includes these follow-up fixes; the initial verdict is not
misrepresented as a clean review of later bytes.

## Helper reproduction

An untrusted TSV cell containing literal `"=1+1"` lost its outer quotes under
CSV-style TSV parsing and became `=1+1`. This was reproduced through the real
helper and `csv.DictReader`; spreadsheet execution/exfiltration was not tested.
The new behavioral case failed before the fix and passed afterward. The helper
now quotes/escapes field contents and neutralizes dangerous prefixes after leading
whitespace. Original upstream copyright/permission notices remain retained.
Reproduction/red/green evidence: `/tmp/rho-pstack-tsv-*` on the validation machine.

## Limits of the evidence

- Parsing optional Anthropic/Google/xAI/Antigravity/Claude-CLI definitions does not
  prove those accounts, current model IDs or external runtimes are available.
- This is an invoked skill workflow, not an installed GitHub webhook or CI gate.
- No real PR was created to test post-audit discussion retrieval or merge rules.
  No publishing/merging/CI-waiver behavior is authorized by the plugin.
- Live loading was exercised through the CLI; TUI/ACP mention preprocessing was
  not exhaustively tested. Start a new session after installation or updates.
- The helper was tested on the installed Linux Bash, not every spreadsheet or
  historical shell version. Logs created by an older helper are not repaired.
- Temporary logs contain local validation receipts, not portable packaged evidence;
  rerun the documented checks to establish results on another installation.
