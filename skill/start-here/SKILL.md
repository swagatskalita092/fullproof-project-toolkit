---
name: start-here
description: Use when someone isn't sure which part of project-blueprint they need - a short router that asks where they're actually stuck and points at the exact doc/skill to use next, instead of making them read the whole repo first.
---

# Start here

This repo has nine steps, a case-study/skill layer, an idea bank, and now a self-audit and a consistency check. Most people arrive stuck at exactly one point, not needing all of it at once. This skill's only job is to find that point fast and hand off - it doesn't re-explain the methodology itself, the doc or skill it routes to does that.

## Ask one question first: where are you actually stuck?

**"I don't have an idea yet."**
→ [`docs/08_idea_bank.md`](../../docs/08_idea_bank.md), then run whatever you pick through [`docs/01_pick_your_idea.md`](../../docs/01_pick_your_idea.md) / [`skill/pick-your-idea`](../pick-your-idea/SKILL.md).

**"I have an idea, haven't started building."**
→ [`docs/01_pick_your_idea.md`](../../docs/01_pick_your_idea.md) first (check it's not a shallow version of something common), then [`docs/02_name_your_risks.md`](../../docs/02_name_your_risks.md) and [`docs/03_design_decisions.md`](../../docs/03_design_decisions.md) before writing code.

**"I'm mid-build."**
→ [`docs/04_build_in_phases.md`](../../docs/04_build_in_phases.md) / [`skill/phased-build`](../phased-build/SKILL.md) - the question to ask right now is whether the phase you just finished was actually verified, or just moved past.

**"It works, but I don't know if it's actually good enough."**
→ Run [`skill/project-self-audit`](../project-self-audit/SKILL.md) against it directly - this is almost always the real gap, not something new to build. It will point you back at steps 05 and 06 specifically, which is where most projects turn out thinner than assumed.

**"It's built and verified, now I need to write it up."**
→ [`docs/07_case_study_and_resume.md`](../../docs/07_case_study_and_resume.md) / [`skill/case-study-and-resume`](../case-study-and-resume/SKILL.md).

**"I'm writing a research paper, not a project."**
→ [`docs/09_research_paper.md`](../../docs/09_research_paper.md) / [`skill/research-paper-drafting`](../research-paper-drafting/SKILL.md) - same honesty rules, academic structure.

**"I want the whole pipeline at once, not routed piece by piece."**
→ [`skill/portfolio-project-rigor`](../portfolio-project-rigor/SKILL.md).

**"I maintain this repo and want to check the skills themselves are still consistent."**
→ [`skill/methodology-consistency-check`](../methodology-consistency-check/SKILL.md).

## If none of those fit

Say in one sentence what's actually true right now (have an idea / don't, have code / don't, have test results / don't) - that sentence alone usually makes the right doc obvious from the list above. If it genuinely doesn't, the honest answer is probably step 01 or 02: most things that feel directionless trace back to the idea or the risk never having been pinned down.
