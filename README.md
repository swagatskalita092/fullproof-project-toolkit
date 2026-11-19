# project-blueprint

**Build interview-ready projects.**

Most "how to build a good portfolio project" advice is generic opinion. This repo isn't that. It's the actual, phase-by-phase pipeline used to build two real, independently verified engineering projects (a flash-sale checkout backend with chaos-tested concurrency, and a data pipeline with chaos-tested correctness), written down so anyone can follow it - and the worked examples in `examples/` are real excerpts from those two projects, not hypotheticals.

The point of a portfolio project isn't that it works. It's that every claim about it is something that was actually proven, not asserted. That's the bar this repo is trying to get you to.

## Quick start

**Have an idea already?** Start at [`docs/01_pick_your_idea.md`](docs/01_pick_your_idea.md) - check it's not a shallow version of something common before you invest time in it.

**Have a project already, and want to know what's missing?** Skip to [`docs/05_adversarial_testing.md`](docs/05_adversarial_testing.md) and [`docs/06_verification_checklist.md`](docs/06_verification_checklist.md) first - these are usually the gap between "it works" and "it's interview-ready." Then come back to [`docs/07_case_study_and_resume.md`](docs/07_case_study_and_resume.md) to write it up properly.

## The pipeline

| Step | What it covers |
|---|---|
| [01 - Pick your idea](docs/01_pick_your_idea.md) | The saturation check: is this a shallow version of something everyone has? |
| [02 - Name your risks](docs/02_name_your_risks.md) | What must stay true, and how it credibly fails - before any architecture |
| [03 - Design decisions](docs/03_design_decisions.md) | Recording tradeoffs as provisional decisions with stated revisit triggers |
| [04 - Build in phases](docs/04_build_in_phases.md) | Incremental, independently-verified phases instead of one big build |
| [05 - Adversarial testing](docs/05_adversarial_testing.md) | Designing a test suite sized to the real risks named in step 02 |
| [06 - Verification checklist](docs/06_verification_checklist.md) | Never trusting a single report - fresh clones, real infra, direct checks |
| [07 - Case study and resume](docs/07_case_study_and_resume.md) | Writing the finished project up as something you can actually defend |

## What's in this repo

- `docs/` - the methodology itself, one file per step.
- `templates/` - blank, fillable versions of the working documents each step produces.
- `examples/` - real excerpts from two actual projects, annotated to show the methodology in practice, not invented for this repo.
- `skill/portfolio-project-rigor/` - the same methodology packaged as an importable Claude skill, for anyone using Claude to help build their project.

## Why this exists

A project that just "works" and a project that survives a skeptical interviewer asking "how do you know that's true" are different things. The gap between them is almost always: were the real risks named before building, was anything deliberately broken to prove it's handled, and was the result verified independently instead of just trusted. This repo exists to make that gap closeable by anyone, not just something you stumble into after building two projects the hard way.
