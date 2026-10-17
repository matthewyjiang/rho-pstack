---
name: prove-it-works
description: "Verify task outputs through the actual artifact or real user path before declaring completion. Use after implementation, fixes, migrations, or delegated work."
license: MIT
disable-model-invocation: false
---

# Prove it works

Read [the workflow contract](../../references/workflow-contract.md).
Derived from pstack's `principle-prove-it-works`.

Check the real artifact, not proxies, cached screenshots, file mtimes, a delegate's
summary or "it compiles". For a bug fix reproduce the user-visible failure first;
then show that the same path works after the fix and relevant bad paths remain safe.

- Define observable acceptance criteria from the request, not the implementation.
- Run the feature, read the actual value, inspect generated files/diffs, and check
  integrations in proportion to risk. If a result surprises you, validate the
  observation method before inventing a system failure.
- Use a small deterministic rerunnable check where useful. Demonstrate that it
  can detect a wrong result; tests whose expected values come from the same code
  prove nothing. Do not grow a smoke-test framework for a trivial edit.
- Keep commands, versions, scope and observed results with artifacts. Parent owns
  builds/tests, max eight jobs, logs redirected and inspected. A failed command is
  not evidence of success even if the intended output looks plausible.
- Distinguish pass, fail, not run and inconclusive. Explain missing credentials,
  hardware, runtime or coverage. Never fabricate screenshots, outputs or green CI.
- Use `show-me-your-work` when a long/complex run needs an auditable decision trail.

Report what was checked and its result, plus what remains unverified. Verification
never grants permission to commit, publish, merge or waive CI.
