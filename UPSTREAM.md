# Upstream provenance and license audit

Canonical repository: https://github.com/cursor/plugins

Pinned commit: `09d06eb4b97a1020ab31e84030e38baf1099c7dc`

| Component | Version at that commit | Author / copyright | License |
| --- | --- | --- | --- |
| [pstack](https://github.com/cursor/plugins/tree/09d06eb4b97a1020ab31e84030e38baf1099c7dc/pstack) | 0.15.25 (`pstack/plugin.json` and `.cursor-plugin/plugin.json`) | Lauren Tan, 2026 | MIT |
| [thermos](https://github.com/cursor/plugins/tree/09d06eb4b97a1020ab31e84030e38baf1099c7dc/thermos) | 1.0.0 (`thermos/.cursor-plugin/plugin.json`) | Cursor, 2026 | MIT |

Both component LICENSE files were read, not inferred solely from metadata. They
permit copying, modification and redistribution, including in a private repository,
provided copyright and permission notices are retained. Original notices are
preserved verbatim in [licenses/pstack-MIT.txt](licenses/pstack-MIT.txt) and
[licenses/thermos-MIT.txt](licenses/thermos-MIT.txt). The combined port is MIT;
[LICENSE](LICENSE) includes both upstream owners and Matthew Jiang's port work.
No trademark, endorsement or upstream maintenance relationship is implied.

## Derived material

- `skills/how`, `why`, `architect`, `sharpen`, `blast-radius`, `correct`,
  `show-me-your-work`, `interrogate` and the retained `principle-*` directories
  derive from the same paths under upstream `pstack/skills/`.
- `skills/prove-it-works` derives from `pstack/skills/principle-prove-it-works`.
- Bundled how/why/architect/interrogate reference files, the decision-log TSV
  template and `show-me-your-work/scripts/log.sh` derive from their pstack paths.
- All three `skills/thermo*` directories derive from `thermos/skills/` at the
  pinned commit; the security and quality subagent behavior is supplied as full
  rubrics in prompts to Rho's existing reviewer, not custom agent definitions.
- `skills/pstack`, shared contracts, package checks, tests and package documentation
  are this port's additions. The v0.1 companion agents/installer were removed in
  v0.2; optional cross-model interrogation now uses a host-provided delegation API.

This is a curated custom port, not a byte-for-byte mirror and not an upstream
release. See README for the merge/removal map. Future updates should diff these
pinned component paths, recheck licenses and routing assumptions, and rerun local
Rho loading/reviewer tests. Do not copy upstream CHANGELOG files into this package.
