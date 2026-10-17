# Review routing without custom agents

This is a skills-only plugin. Do not install agent definitions, override `reviewer`,
pin models in global configuration, or change credentials to run it.
Read [the workflow contract](workflow-contract.md) first.

## Portable Rho path

Use the existing `reviewer` agent via `agent({agent_id: "reviewer", prompt: brief})`.
Each call starts a separate context and normally inherits the parent provider/model.
Thermos calls it twice in one batch, supplying a different full rubric to each.
**Same-model review is the normal supported mode**, not a degraded fallback. Two
contexts/lenses are useful but are not model diversity. If an existing user/project
override selects a different model, report the actual binding; never edit that
configuration or infer diversity from agent IDs.

The built-in reviewer has read tools, not a shell or nested delegation. The parent
must collect Git diffs/history, PR discussion and validation results. Supply the
actual scoped diff, full rubric, shared constraints and necessary source context
in each prompt, or expose a parent-prepared immutable snapshot through readable
paths. Do not tell the child to run `git show`, `git diff`, builds or shell commands.
For committed scope, the **parent** obtains pinned source with Git, not live-file
reads. Children may read a supplied immutable snapshot, but must not substitute a
mutable worktree for it. If required context/tools are unavailable, report the gap;
the parent can collect the missing evidence and rerun the affected review. Missing
coverage or an agent error is never approval.

Retain run IDs and await all required completions through Rho's automatic delivery.
Do not busy-poll, launch duplicates, or finish after the first of two required passes.
Reviewers do not edit, commit, publish or run tests. The parent owns authorized
validation (max eight build jobs, verbose logs redirected). Respect repository/user
policy, and verify findings rather than counting votes.

## Optional host-backed cross-model interrogation

`interrogate` uses model-selecting delegation **only when the host exposes it**.
For example, in T3 Code:

1. Discover `orchestrator_capabilities` and `delegate_task` through the available
   tool catalog and read their schemas. Use the live provider/model catalog, not
   hard-coded slugs. Follow the host's own delegation instructions.
2. Choose genuinely different available model families. Submit self-contained,
   read-only tasks with the same pinned scope, intent, evidence and full rubric.
   Batch independent launches; keep every task ID and await all results. Use stable
   request IDs for retries where supported; do not create top-level conversations.
3. Disclose actual provider/model bindings, substitutions, failed routes and gaps.
   Missing auth or a failed task is not a clean review. Never change credentials,
   install a toolchain, or wrap `rho run` in a homemade model runner to bypass this.

Without model-selecting host delegation, say **cross-model interrogation is
unavailable in this session**. Offer an ordinary same-model `reviewer` pass, but
only run that substitute if the user accepts; do not call it cross-model review.
This limitation does not block thermos, architecture, or evidence-trail review.

A provider/model field belongs to the host's model-selecting API, **not** Rho's
native `agent` call. Native calls take only `agent_id` and `prompt`; no Cursor Task,
`subagent_type`, `readonly`, per-call `model`, or background flag is needed.
