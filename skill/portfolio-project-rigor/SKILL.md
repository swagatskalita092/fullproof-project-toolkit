---
name: portfolio-project-rigor
description: Use when picking, scoping, building, or extending a portfolio/engineering project where the goal is genuine, interview-defensible depth rather than just working code - structures the work into a disciplined pipeline from idea selection through verification and resume framing.
---

# Portfolio project rigor

A structured pipeline for building a portfolio/resume engineering project so it survives a skeptical interviewer poking at it, not just a project that runs. The point of a portfolio project isn't that it works - it's that every claim about it is something that was actually proven, not asserted.

The risk this whole skill has to watch for in itself: optimizing for *evidence of rigor* instead of *engineering judgment*. A strong portfolio project shows that the real risks were identified, the tradeoffs were sensible, and the important claims were verified - the amount of process applied is secondary, not the goal.

## Scale the rigor to the project's actual size - read this first

This full pipeline is for something going on a resume as a headline project. A small script, a one-off utility, or genuine throwaway exploration doesn't need a design doc or a numbered adversarial suite - over-applying this process to something small produces busywork, not credibility. The judgment call: if the person would plausibly be asked to defend it in an interview as a real piece of work, apply the pipeline; if it's a tool used once and forgotten, skip straight to building it. Even on a headline project, stop adding process once it stops answering a real question - the stopping rule is "can I say which demonstrated requirement or credible failure this addresses?"; if not, it's decoration.

## 0. Pick the idea deliberately - check for a real differentiator, not just novelty

Before scoping anything, name the differentiator: what does this prove that a shallow, generic version of the same idea wouldn't? A familiar project shape is not automatically weak - a conventional problem built with real depth is often stronger interview material than a novel-sounding idea with shallow execution. The real red flag isn't "this idea is common," it's "the honest answer to 'what does this prove' is nothing beyond gluing two tools together."

**Getting a second opinion, done properly:** the value isn't a verdict to defer to, it's a source of objections.

1. Write your own criteria and your own initial assessment of the idea first.
2. Ask the second opinion specifically for counterexamples, hidden assumptions, and the strongest reason to reject the idea - not "is this a good idea."
3. Check any factual claims it makes against real evidence.
4. Record what changed the decision and why - if nothing changed, say that too.

## 1. Record provisional decisions, not locked-in ones - with their uncertainty and revisit triggers

Write down the architecture and the specific tradeoffs chosen, each with the alternative that was rejected and why. Hold these as provisional: some decisions genuinely need a small implementation experiment before they can be made well. For each real decision, note what would change it and when to revisit.

## 2. Start from the risk, not the technique - then choose adversarial tests proportionate to it

First identify what must stay true for the project to be correct, and how it could plausibly fail. Once the real invariants and credible failure modes are named, write a handful of concrete, numbered adversarial scenarios (3-6 is normal) before building starts, each targeting a real failure mode.

## 3. Build incrementally, phase by phase, each phase independently verified before moving to the next

Decisions and risk analysis -> happy path -> the harder mechanism -> adversarial proof -> deployment -> documentation.

## 4. Support important claims with evidence that could actually expose an error - not just more reports

- Fresh clone, not the working directory that's been edited in place.
- Actually run the tests against real infrastructure, not just read that they "should pass."
- Fetch CI status via the API directly, not an HTML status page that can show a stale snapshot.
- Diff the actually-committed file against the exact drafted content byte for byte when it matters.
- Confirm a push actually landed by comparing local HEAD to the remote branch directly.
- Confirm a test actually encodes the invariant that matters before trusting it as evidence of anything.

## 5. Baseline engineering hygiene a real team would consider table stakes

Reproducibility (a fresh checkout runs with documented commands and no private credentials), basic CI, security fundamentals where applicable (real authorization, input validation, secrets out of code/logs), data correctness where applicable (constraints, transaction boundaries, a stated answer for concurrent writes), diagnosability (enough logged information to explain a failure), and explicit non-goals (a stated boundary between what's demonstrated, assumed, and untested).

## 6. Document honestly, including the bugs

Every real bug found during verification gets written up: root cause, the fix, and a regression test - never softened or hidden. Known limitations that aren't being fixed get stated explicitly rather than omitted.

## 7. No fabricated or rounded numbers, ever - and report the method, not just the figure

Every metric must trace back to a real captured run, with its method, environment, and workload stated, not just a bare number. Label an estimate or target explicitly as such. When evidence conflicts with an existing claim, flag the conflict rather than quietly reconciling it in the more flattering direction.

## 8. Keep scope anchored to real, already-committed-to skills - and keep real ownership of what's claimed

Don't let a project idea quietly require learning a whole new stack unless that's the explicit point and a conscious decision against the real calendar. The deeper test: can the requirement be changed and the resulting failure debugged without depending entirely on AI to do it? That's the actual ownership bar.

## 9. The design/build/verify split

Design the architecture and the verification plan first, let a builder implement it, then verify independently via step 4 - never trust the builder's own self-report as the final word.

## 10. When asked to assess a project's quality, give the honest read, not the flattering one

If asked "is this good enough" or "is there nothing left to add," resist the pull to just agree. Give genuine credit where earned, but name the real, still-open items. Superlatives aren't verifiable against any real benchmark - don't award them; describe concretely what's strong and what's still open instead.

## 11. Translate finished work into resume/interview material without breaking the honesty rules

State what's demonstrated, what remains uncertain, and what would change under different requirements. A resume bullet should name the mechanism and the proof: "built X, proven by deliberately breaking Y and confirming Z" beats a tech list. Draft new bullets as candidates needing sign-off, never land one silently. If a number can't be traced to a real captured run, don't draft it. Add a short "what I'd do differently now" reflection to the write-up too - hindsight judgment, distinct from a known limitation, and specifically the kind of thing that reads as more senior even in one short paragraph.
