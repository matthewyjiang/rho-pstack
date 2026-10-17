# Validation

## v0.2: skills-only routing

Tested on Rho 2.24.0 and Python 3.13.5. This version removes the companion agents
and installer. It uses two ordinary `reviewer` calls for thermos; cross-model
interrogation is optional and requires model-selecting host delegation.

- Package consistency checks pass for all 28 skill names, explicit invocation
  policy, relative file links and retained MIT notices. Rho parses real YAML and
  the Agent Plugins 1.0.0 manifest.
- The two retained behavioral tests exercise the decision-log helper's append,
  single-line, quoted-field round-trip and formula-prefix sanitation behavior.
  Tests for the removed companion installer were removed with that feature.
- Matt's pre-existing `~/.rho/agents/reviewer.md` override and the three previously
  installed pstack reviewer definitions were moved to a recoverable directory
  under `~/.rho/agent-backups/`. Other agents, instructions, credentials and provider
  configuration were left untouched. Rho diagnostics report no invalid definitions.
- The stock reviewer source has read tools only and no provider/model pin or shell.
  Parent prompts now supply Git/PR evidence and immutable source context; children
  are not instructed to run Git or validation commands.

- A real `rho plugins install /absolute/path/to/rho-pstack --force` replaces the
  copied install. Its agent definitions and old installer are absent; no loose
  pstack reviewer files or local reviewer override remain in discovery.
- `scripts/verify-rho.py --live` passes: installed runtime bytes match, 28 direct
  skill calls complete successfully, and the model reports all requested names.
  Local evidence: `/tmp/rho-pstack-live-u4tehtlf/` and
  `/tmp/rho-pstack-v02-live.log`. This is not per-source attestation (see below).

## Built-in parallel thermos test

An end-to-end standalone CLI run loaded the installed thermos skill and reviewed
immutable inline snapshots of `review-routing.md`, `thermos/SKILL.md` and
`interrogate/SKILL.md`. The parent supplied identical pinned scope/intent/evidence
plus full respective rubrics/shared contracts in one native agent batch:

| Lens | Agent / run ID | Terminal runtime / provider / model |
| --- | --- | --- |
| Correctness/security | reviewer / `0bba98` | rho / openai-codex / gpt-6.1-sol — ok |
| Structural quality | reviewer / `7dc38b` | rho / openai-codex / gpt-6.1-sol — ok |

Both independent contexts completed with no findings in that focused scope. The
parent waited for both actual terminal results and synthesized one verdict, with
no custom agents, fallback, shell use by children, or claims of model diversity.
This proves the portable same-model execution path in this session, not absence
of correlated blind spots or repository-wide defects.

Local receipts: `/tmp/rho-pstack-v02-thermos-prompt.txt`,
`/tmp/rho-pstack-v02-thermos.jsonl`, `/tmp/rho-pstack-v02-thermos-result.json`, and
the two Rho child result files. The inline snapshots were source-document review,
not historical diff analysis. No host-backed cross-model run is claimed for v0.2.

## Evidence limits

The CLI event stream exposes tool names, call IDs and status, but not each call's
arguments or loaded-source output. `scripts/verify-rho.py --live` therefore checks
successful direct skill-call counts and model-reported distinct-name coverage;
it does not independently attest per-name source identity. Static inventory and
installed runtime bytes are compared independently. The script fails on observed
failed/missing calls, unexpected tools/counts, nonzero exits or reported-name mismatch.

Rho's live agent diagnostics list user/project definitions rather than the entire
built-in catalog. Absence of a custom `reviewer` there is not by itself proof that
a launch succeeded; actual built-in reviewer launches are tested separately.

No real PR, post-audit discussion retrieval, spreadsheet execution, merge behavior
or exhaustive TUI/ACP compatibility test is implied. Optional host APIs/providers
must be checked in each session. Standard thermos review needs no model diversity.
Temporary evidence paths are local receipts; rerun README checks elsewhere.

## Prior release and preserved fixes

v0.1's provider-bound GPT/Claude thermos test completed both audits against commit
`ed0c7229c1931d14126bb9f0096573ecd26acffd`. It established that routing worked at that
time, not that v0.2 needs those definitions. v0.2 supersedes that setup; Git history
preserves the earlier evidence record.

The earlier audit found that a literal quoted TSV cell `"=1+1"` could lose its quotes
under CSV-style parsing. This was reproduced through the real helper and
`csv.DictReader`; a behavioral test failed before the fix and passed afterward.
The quote-safe serializer, leading-whitespace prefix check, honest live-coverage
wording, shared-asset comparison and corrected rationale link remain in this version.
Spreadsheet execution/exfiltration was not demonstrated, and old log rows are not
retroactively repaired. The original upstream MIT notices remain retained.

An older loose `thermo-nuclear-code-quality-review` skill was previously preserved
under `~/.rho/skill-backups/` to prevent it shadowing the plugin. Future loose/project
skill collisions can still change which source a session loads.
