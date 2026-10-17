# Code-quality lens

Use in addition to the review rubric. Remain read-only and within the changed scope.
Be ambitious about deleting complexity, not just moving it around.

- Seek concrete "code judo": a state/ownership reframing that removes whole branches,
  modes or layers while preserving required behavior. Explain the simpler alternative.
- Measure before/after file growth when relevant. Judge cohesion, reader load, coupling
  and ownership boundaries; there is no universal line-count blocker. A cohesive large
  module can be better than needless fragmentation. Honor measured repo budgets.
- Identify special-case branching inserted into unrelated paths; ask whether a domain
  model, helper or state machine would remove complexity rather than hide it.
- Prefer direct maintainable flows. Flag identity wrappers, magical generic handling,
  speculative abstractions and extra indirection that buy no clarity.
- Inspect casts, any/unknown and optionality for a missing boundary invariant; do not
  flag legitimate raw boundary types just because the token is present.
- Keep knowledge in its canonical layer. Reuse real existing helpers where suitable;
  do not invent a canonical home or force a shared helper for coincidental repetition.
- Look for avoidable serialization of independent work, or related updates that leave
  half-applied state. Show the real failure/maintenance scenario and a simpler design.

Prioritize structural regressions, proven simplifications, tangled control flow,
then boundary/type/ownership and measured decomposition problems. No cosmetic pile-on.
A preference is not a blocker; support substantial findings with file/line evidence,
reachable scenario or demonstrated complexity, and an actionable remedy. Existing
repository policy and compatibility contracts outrank this lens. No auto-refactors.
