# rho-pstack

Matt's engineering workflow as a [Rho Agent Plugin](https://agent-plugins.org/specification):
design first, prove the result, and run one combined `thermos` review per PR.
It's skills only: no custom agents, no model pins, no installer.

A port of Lauren Tan's **pstack** v0.15.25 and Cursor's **thermos** v1.0.0.

## Install

```bash
git clone git@github.com:matthewyjiang/rho-pstack.git ~/projects/rho-pstack
rho plugins install "$HOME/projects/rho-pstack"   # absolute path required
```

Start a new Rho session so it picks up the skills. To update, `git pull` and
reinstall with `--force`. For development, use `rho plugins link` in place of `install`.

## Use

```text
$pstack implement this feature
$architect sketch the ownership model; stop before implementing
$why why is this retry limit here?
$thermos review this PR
$interrogate challenge this design with a different model
```

`/skill:<name>` also works, and the model can load skills on its own.

| Group | Skills |
| --- | --- |
| Entry | `pstack` (routes to the others) |
| Design | `how`, `why`, `architect`, `sharpen` |
| Proof | `blast-radius`, `prove-it-works`, `show-me-your-work`, `correct` |
| Review | `thermos`, `thermo-nuclear-review`, `thermo-nuclear-code-quality-review`, `interrogate` |
| Principles | 15 `principle-*` skills |

- **thermos** runs Rho's built-in `reviewer` twice in parallel, once with the
  correctness/security rubric and once with the code-quality rubric, then merges
  the results into one verdict. Both reviewers use the same model as the parent.
- **interrogate** needs a host that can delegate to other models, such as T3 Code's
  `delegate_task`. If the host can't, it says cross-model review is unavailable.

Repository `AGENTS.md`, user instructions, and permissions always win. See
[workflow-contract.md](references/workflow-contract.md) and
[review-routing.md](references/review-routing.md) for the rules the skills follow.

## License

MIT. Derived from [cursor/plugins](https://github.com/cursor/plugins/tree/09d06eb4b97a1020ab31e84030e38baf1099c7dc)
at commit `09d06eb`: `pstack/` (© 2026 Lauren Tan) and `thermos/` (© 2026 Cursor).
The original notices are in [licenses/](licenses/). This is an unofficial port.
