---
name: show-me-your-work
description: "Keep an evidence-linked decision trail for long or multi-phase work, then audit it against this Rho conversation and actual artifacts. Local by default; no automatic commits."
license: MIT
disable-model-invocation: false
---

# Show me your work

Read [the workflow contract](../../references/workflow-contract.md).
Keep one canonical TSV log for a substantial run; do not log every routine action.

Use `references/decision-log-template.tsv` and
`scripts/log.sh <logfile> <phase> <decision> <why> <evidence> <result>`.
Columns are ts (ISO8601), phase, decision, why, evidence pointer, result. Cells stay
single-line. The helper sanitizes tabs/newlines and spreadsheet formula prefixes.
The helper writes quoted TSV: double quotes within fields are doubled. Read it
with a CSV-aware tab-delimited reader, such as Python `csv.DictReader(...,
delimiter="\t")`, not raw `cut`/`awk` field comparisons. The leading apostrophe
neutralizes formula prefixes for display; it is part of the parsed text. Existing
rows written by an older helper are not retroactively made quote-safe.
Evidence is a resolvable commit, file/line, run ID, PR or artifact, not a paragraph.
Log meaningful forks, verification checkpoints, pivots, reverts and blockers.

Default to a local ignored path such as `.audit/<task>.tsv`, checking the repo's
ignore policy. Never change gitignore or commit the log just because this skill
was loaded. Preserve privacy; redact secrets before writing, not just before publishing.
Each run has one writer; separate delegate logs and synthesize rather than racing
on a shared file. At a new run/pickup, append a `start` row naming prior rows/time
range and this run's ID. Reserve `start` for ownership boundaries.

## Audit the evidence

Before handoff, compare this run's rows with actual actions and artifacts.
Use Rho `sessions` search/read with `scope: current` and returned anchors when
conversation details have been compacted. Do not invent transcript filesystem
paths or search unrelated sessions. If current-scope session access is unavailable,
use supplied receipts and current context, explicitly mark the missing coverage,
and never claim a full transcript audit.

Follow each evidence pointer. Append superseding rows for wrong claims; do not
rewrite history. Add omitted decisions that materially shaped the work. Audit only
your run's stretches, except to supersede an older error discovered by your own work.

For a high-stakes trail, request an independent reviewer via
[review routing](../../references/review-routing.md). Give the TSV, safe evidence
excerpts and relevant receipts explicitly; do not assume a child has the parent's
conversation. No edits/builds. Ask it to flag weak evidence, unproved verification,
scope drift and risky choices, not redo the task. Disclose unavailable diversity.
Do not claim review if no reviewer completed.

Return an **Attention** section for a run with a trail: actual reviewer/model and
flags pointing to rows, or state that independent review was not run and why.
No flags is valid only after the evidence was checked.
