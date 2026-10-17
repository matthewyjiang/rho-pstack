---
name: blast-radius
description: "Trace what a change could break beyond its diff and prove the load-bearing safety assumptions through real code. Use before risky changes or shipping."
license: MIT
disable-model-invocation: false
---

# Blast radius

Read [the workflow contract](../../references/workflow-contract.md).
`how` explains mechanism; `why` explains its shape. This skill finds what breaks
elsewhere, including dependencies a symbol search cannot see.

1. Pin the actual diff and intent; include deleted/renamed contracts and implicit
   behavior. Pull relevant historical/PR evidence when it explains a safety invariant.
2. Find the load-bearing safety facts. A long caller list is not a risk analysis.
3. Trace beyond grep: pinned library implementations/local patches, wire formats,
   storage schemas, feature gates, lifecycle ordering, teardown, tasks and other
   languages/services consuming the same data. Never invent a caller or API.
4. Distinguish confirmed risks, cleared cases and unknowns. Give a reachable failure
   scenario, likelihood/impact rationale and file/line evidence, not guessed percentages.
5. Prove each important fact through the real code or running user path. A small
   script importing the shipped library often beats a persuasive explanation.
   Parent runs validation; no delegate builds. If execution needs unavailable
   credentials/hardware or would have unsafe effects, mark it **unproven**.
6. For broad/high-risk review, an independent `reviewer` pass can pressure-test the
   assumptions. Use `interrogate` for cross-model input only when the host supports
   it. Do not block ordinary proof on model diversity or duplicate PR review:
   `thermos` remains the single combined PR review entry point.

Report: what changed; the facts safety depends on; proof artifacts/commands and
observed results; risks with evidence; cleared cases; cheapest meaningful check
before merge. State evidence strength explicitly: claim, source trace, demonstrated
unreachable path, real-code execution, or running-app reproduction. Do not present
source reading as runtime proof. Keep private material out of public artifacts.
