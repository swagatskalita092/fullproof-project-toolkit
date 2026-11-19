# 04 - Build in phases

Build incrementally, with each phase independently verified before moving to the next. Don't let phases blur together or get marked done without actually checking them.

## The shape that works

Risks and decisions locked (steps 02-03) -> the happy path -> the harder mechanism the project actually exists to prove -> adversarial proof that it holds under pressure -> deployment -> documentation.

Each phase should produce something checkable on its own - a phase isn't done because you moved on to the next one, it's done because you verified it the way step 06 describes.

## Why phases, not one big build

A project built end to end before anything is tested tends to hide its real bugs until the very end, when they're most expensive to fix and hardest to isolate. Both of the real projects this repo's examples are drawn from found genuine bugs during intermediate verification passes - a consumer callback with the wrong number of arguments, a response type mismatch, a port collision, an uncaught exception class - each one caught because a phase was checked before the next one started, not because the whole system was reviewed once at the end.

## A note on scale

This doesn't mean every project needs six named phases. A small, well-scoped project might have three real phases. What matters is that whatever phases exist are independently verifiable, not that there's a specific number of them.

Next: [05 - Adversarial testing](05_adversarial_testing.md).
