---
name: principle-sequence-verifiable-units
description: "Apply to multi-step work (sweeps, migrations, runs of similar edits) and to how you stack commits and PRs. Break work into small units that each end in a verifiable state, check each before the next, and order delivery so the sequence proves itself to a reviewer."
disable-model-invocation: false
---

# Sequence work into verifiable units

Read [the workflow contract](../../references/workflow-contract.md).

Order work as a sequence of small units, each ending in a state you can check, and don't advance until the current one is green.

**Why:** A break caught at the unit that caused it is cheap to localize. A break caught after a batch is buried, and you have already built further on a broken base. Sequencing those same units into a delivery a reviewer can replay turns "trust me" into "watch it go red, then green."

**Execution.** In a sweep, migration, or any run of similar edits, verify each coherent unit before starting the next. Each unit is a before/after bracket: recorded baseline, one change, run the check, then proceed. Preserve existing work; do not rebase or rewrite history unasked. When a lever makes the per-unit check cheap, run it.

**Delivery.** When commits/PRs are requested, order them to make the proof readable: baseline/reproduction before treatment, subtraction before reshaping, useful scaffold before feature. Follow repository rules about green commits and stack shape; do not create commits or stacks just because a skill suggests them.

**Planned migrations.** Optimize for the verified target, not throwaway compatibility machinery. Any temporarily broken intermediate work must be explicitly scoped, reversible and local to an accepted phase. Never publish broken checkpoints or waive CI against repository/user policy. Keep high-signal checks active and finish with full relevant static/runtime verification.

The sequencing complement to the **prove-it-works** principle skill, which keeps each check real, and the **build-the-lever** principle skill, which makes the per-unit check cheap.
