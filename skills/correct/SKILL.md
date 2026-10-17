---
name: correct
description: "Turn recurring agent mistakes into structural prevention: architecture, types, actionable lint, then behavior tests. Use after a repeated correction or when asked to harden the workflow."
disable-model-invocation: false
---

# Correct

Read [the workflow contract](../../references/workflow-contract.md).

Find recurring mistake classes in relevant commits, reverts, reviews, corrections
and repository instructions. Distinguish demonstrated recurrence from a speculative
new rule. Prefer the highest-level fix that removes the mistake:

1. Architecture: one state owner, one supported route, unreachable internals;
   derive shared lists from one source of truth, remove misleading dead examples.
2. Types: make invalid states unrepresentable. Then an actionable lint/check whose
   error names the supported type, function or file. Ratchet only new violations
   where the existing baseline cannot reasonably be migrated in scope.
3. Behavior tests: drive the real interface; prove the guard fails on an actual past
   mistake and passes on the intended behavior. Parent runs local/CI-equivalent checks.
4. Docs last for remaining judgment calls, with a concrete failure example. A new
   instruction alone is not enforcement. When structure solves it, avoid redundant rules.

Implement only fixes within the authorized task. Propose broad policy changes rather
than editing AGENTS.md, changing CI gates, granting exceptions or creating commits
unasked. If the repo already keeps an enforcement table, update it only when asked
or clearly in scope; do not impose a new one globally. Respect repo exception policy.

Return each class, evidence of recurrence, prevention level chosen, why stronger
prevention was unsuitable, and proof that the check catches the real mistake.
