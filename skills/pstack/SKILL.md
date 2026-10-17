---
name: pstack
description: "Lightweight entry point for Matt’s general engineering workflow. Route nontrivial tasks to design, proof, relevant principles, and thermos for every PR; no autonomy or merge-policy changes."
license: MIT
disable-model-invocation: false
---

# Pstack

Read [the workflow contract](../../references/workflow-contract.md).
This is a router, not an autonomous operating mode. Apply relevant skills through
Rho's `skill` tool; do not preload everything or make trivial edits ceremonial.

| Task | Route |
| --- | --- |
| Unclear framing / useful independent check | `sharpen` |
| Mechanism, ownership or layering unknown | `how` |
| Historical rationale or hidden constraints | `why` |
| Nontrivial architecture / state model | `architect` |
| Risk beyond the diff | `blast-radius` |
| Finish implementation / verify a fix | `prove-it-works` |
| Long, multi-phase work needs an evidence trail | `show-me-your-work` |
| Recurring operator correction | `correct` |
| Explicit cross-model challenge | `interrogate` |
| Any PR creation/update/review task | `thermos` — one combined review |

Pick principle skills by the actual decision: domain/types/boundaries before logic;
root cause when debugging; subtraction/reader load when simplifying;
idempotency/shared-state isolation when handling concurrency or retries;
measured numbers and behavior tests when proving results. Use sequence and a
small rerunnable lever when they reduce risk in a multi-step change.

Stay within the user's requested analysis/design/implementation scope. This entry
skill does not authorize PR writing, publishing, background autonomy, CI waivers
or merging, and adds no prose-style rules. Thermos is a workflow default when this
router is used, not an automatic GitHub hook or an enforced CI status check.
