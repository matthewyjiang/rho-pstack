---
name: why
description: "Investigate design rationale, historical constraints, regressions, postmortems, or data-backed thresholds. Separate cited facts from inference; use how for runtime behavior."
disable-model-invocation: false
---

# Why

Read [the workflow contract](../../references/workflow-contract.md) and
`references/epistemics.md`. Investigate what forces led to the code's shape.

## Anchor the question

State the target and the actual why. Read source and types first. Gather relevant
`git blame`, `git log --follow -p -- <file>`, commit bodies, linked tickets and PR
bodies/discussion (`gh pr view` or the repo's equivalent). Inspect historical code,
not just the last touch. When changing ownership/layering, translate rationale
into constraints before proposing replacement architecture.

## Find evidence, not a story

Discover available tools/MCPs through Rho's tool catalog (`tool_search` or codemode
`search_tools` / `describe_tool` when exposed). No Cursor MCP directories or assumed
company integrations. Map evidence to these categories:

- source history and review;
- issues/tickets;
- long-form design documents;
- team deliberation/chat;
- infrastructure observability;
- errors/incidents;
- product/experiment analytics.

Use `references/source-playbook.md` and matching `references/sources/` playbooks
as search recipes, not promises about tool availability or schemas. Verify real
schemas before queries. Prefer bounded, read-only queries; never dump private data.
Defensive code especially warrants `references/sources/incident-postmortem.md`.

Search relevant available categories. Mark missing tools, permissions, retention,
null results and provably irrelevant categories explicitly. A null search is not
proof that no rationale existed. For substantial independent investigations, batch
`agent` calls to `explorer`, supplying the anchor, question, epistemic framework,
and `references/investigator-prompt.md` contents. Do MCP queries in the parent if
children lack those tools, rather than pretending they searched. Small questions
can be answered directly from sufficient primary evidence.

## Synthesize

Use `references/synthesizer-prompt.md`. Spot-check citations. Separate What we
found, What we can reasonably infer, Competing hypotheses, and What we don't know.
Include The question, Code in question, Sources consulted (including gaps/nulls),
and Confidence summary where useful. Never upgrade confidence while summarizing.
If a change follows, end with **Preserve / Change / Avoid / Risk** constraints.
