---
name: phased-build
description: Use when planning or executing the build order of a project that needs to prove something real - structures work into independently-verified phases instead of one big build checked only at the end.
---

# Phased build

Build incrementally, with each phase independently verified before moving to the next. Don't let phases blur together or get marked done without actually checking them.

**The shape that works:** risks and decisions locked -> happy path -> the harder mechanism the project exists to prove -> adversarial proof it holds under pressure -> deployment -> documentation.

**Design, build, verify as a pattern, not an org chart:** design the architecture and verification plan first, build (or have a tool/agent build) it, then verify independently - never trust a builder's self-report, including your own in-the-moment confidence, as the final word. This is a distinction between thinking activities, not a requirement for separate people or formal handoffs.

**Why phases, not one big build:** a project built end to end before anything is tested tends to hide its real bugs until the end, when they're most expensive to fix and hardest to isolate. Real bugs get caught during intermediate verification passes far more often than during a single review at the end.

**In practice:** write the phase list before coding. For each phase, write one checkable sentence defining "verified" - not "it works," something concrete. Don't start the next phase until that sentence is actually true. If a phase reveals an earlier decision was wrong, update that decision explicitly rather than quietly working around it.
