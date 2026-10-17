---
name: principle-guard-the-context-window
description: "Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents; keep summaries in the main thread, not raw payloads."
disable-model-invocation: false
---

# Guard the Context Window

Read [the workflow contract](../../references/workflow-contract.md).

**Why:** Context overflow degrades reasoning quality, creates compression artifacts, and halts progress.

**Pattern:**
- **Bound observations, not correctness.** Ask for paths/counts before full content, read focused ranges and redirect verbose logs to temporary files. Inspect success/failure and relevant excerpts rather than dumping logs. Do not guess file/turn caps; measure before imposing a budget and report any coverage omitted.
- Delegate substantial independent investigations, not bulk payloads that a filter can reduce. Keep evidence pointers and findings in the parent. Use Rho `sessions` with `scope: current` to recover compacted details, rather than guessing or rereading unrelated history.
