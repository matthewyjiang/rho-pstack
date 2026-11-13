---
name: interrogate
description: "Optional adversarial cross-model review: adversaries on different model families try to break a change or design, and only findings proven by a run survive. Report unavailable model selection honestly; thermos remains the portable combined PR review."
license: MIT
disable-model-invocation: false
---

# Interrogate

Read [the workflow contract](../../references/workflow-contract.md) and
[review routing](../../references/review-routing.md). Adversaries try to break a
change or a design. A finding survives only when a run proves it. Report the
findings. Do not apply fixes.

## Frame

The scope is what the user names. Otherwise it is the branch diff from its merge
base with the base branch, through the working tree; resolve the real base, not an
assumed `main`, and pin it. State the intent in your own words from the user's
message, the commits and the PR description. Ask the user when the intent is unclear.

## Fan out

Pick at least two genuinely different model families: per-call `model` on Rho's
`agent`, or host model-selecting delegation (see review routing). Use models the
user named or configured; ask once if none are known. Without two families, say
**cross-model interrogation unavailable** and offer a same-model `reviewer` pass
only if the user accepts.

Launch one `reviewer` per model in one batch, each with the pinned scope, the
intent and this brief:

> Break this change. Each finding needs a repro against the real code: a failing
> test, a script, or a command, given in full so it can be run as written, plus
> the output you expect it to print and the output the intent requires. For a
> design or plan, give a prototype or a probe of the current tree. Do not run
> builds or tests yourself and do not edit files; the parent runs every repro.
> Leave out anything without a runnable repro. That covers style, naming,
> structure, and risks that need a future change to matter. No findings is a
> valid result.

Record run IDs and the actual bound models. A failed run is not a clean review.

## Verify

Run each repro yourself in a scratch location (a temp dir or a `git worktree` at
the pinned head), never in the user's working tree; max 8 build jobs, logs to a
temp file. Keep a finding when the output shows the failure and the failure
breaks the intent. Drop the rest. Merge findings that share a root cause.
Adversaries find different failures, so keep every verified finding; consensus is
not proof and a lone finding is not noise.

## Output

- **Intent**: the restatement.
- **Adversaries**: each one's actual provider/model, status and finding count.
- **Findings**: for each verified finding, the command, its output, how it breaks
  the intent, and the adversaries that found it. Say "no verified findings" when
  none survive.
- **Dropped**: for each adversary, the count of dropped findings and why.

Never describe a user-accepted same-model pass as cross-model interrogation. For
PR work, `thermos` is the one combined review unless the user asked for a distinct
interrogation.
