# 04 - Build in phases

Build incrementally, with each phase independently verified before moving to the next. Don't let phases blur together or get marked done without actually checking them.

## The shape that works

Risks and decisions locked (steps 02-03) -> the happy path -> the harder mechanism the project actually exists to prove -> adversarial proof that it holds under pressure -> deployment -> documentation.

Each phase should produce something checkable on its own - a phase isn't done because you moved on to the next one, it's done because you verified it the way step 06 describes.

## Why phases, not one big build

A project built end to end before anything is tested tends to hide its real bugs until the very end, when they're most expensive to fix and hardest to isolate. Both of the real projects this repo's examples are drawn from found genuine bugs during intermediate verification passes - a consumer callback with the wrong number of arguments, a response type mismatch, a port collision, an uncaught exception class - each one caught because a phase was checked before the next one started, not because the whole system was reviewed once at the end.

## A note on scale

This doesn't mean every project needs six named phases. A small, well-scoped project might have three real phases. What matters is that whatever phases exist are independently verifiable, not that there's a specific number of them.

## A worked example

[`examples/stack_overflow_pipeline_full_walkthrough.md`](../examples/stack_overflow_pipeline_full_walkthrough.md) shows seven real phases, each independently verified before the next started - and shows what it looks like when a phase genuinely does reveal an earlier design decision was wrong (a global monotonicity guard that needed to become per-dimension once a second data year was added), updated explicitly per step 4 below rather than patched around in code.

Next: [05 - Adversarial testing](05_adversarial_testing.md).

## Step by step, in practice

1. Draft the phase list before writing code: typically decisions/risks -> happy path -> the hard mechanism -> adversarial proof -> deployment -> docs, but cut or merge phases that don't fit your project's real shape.
2. For each phase, write one sentence describing what "verified" means for it specifically - not "it works," something checkable (e.g. "all three chaos scenarios run against real containers with captured output").
3. Don't start the next phase until the current one's verification sentence is actually true, not just probably true.
4. If a phase reveals that an earlier design decision (step 03) was wrong, update that decision file explicitly rather than silently working around it in code.
5. Keep a running note of anything surprising that happened during a phase, even if it's not a full bug yet - today's "huh, that's odd" is often tomorrow's entry in step 06.
