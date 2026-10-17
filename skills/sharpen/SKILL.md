---
name: sharpen
description: "Frame a task before starting: expert methods, real user outcome, useful constraints, and an independent check. Use when a request is vague, overconstrained, or ready to execute."
license: MIT
disable-model-invocation: false
---

# Sharpen

Read [the workflow contract](../../references/workflow-contract.md).
Before starting, consider how a top expert would approach this task: primary
sources, real methods, and an outside check that the result is right. Identify what
the user actually needs and whether the task is over- or underspecified. Propose
relaxing constraints that obstruct the goal, but never silently loosen explicit
requirements, safety boundaries or repository policy. Leave material user choices
open and ask when needed. Fold in only what improves the work, not what makes it
bigger. Keep an independent check, then do the requested work; do not hand back a
rewritten prompt as the deliverable.
