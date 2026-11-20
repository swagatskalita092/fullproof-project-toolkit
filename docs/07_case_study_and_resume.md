# 07 - Case study and resume

A finished project and an interview-ready project are different things. This step is where the gap between them gets closed.

## Document honestly, including the bugs

Every real bug found during verification gets written up: root cause, the fix, and a regression test - never softened, hidden, or quietly fixed without a trace. Known limitations that aren't being fixed get stated explicitly ("documented, not fixed") rather than omitted.

This isn't just ethics for its own sake - it's the actual credibility signal. A project that admits its gaps reads as more trustworthy than one that claims perfection, and in an interview, "here's a real bug I found and how I found it" is a far stronger answer than a project that supposedly has none.

## No fabricated or rounded numbers, ever

Every metric that appears in a README, a resume bullet, or project notes must trace back to a real captured run, and should carry its method, environment, and workload, not just a bare figure - "p99 1.2s, 500 concurrent users, measured via a load test against the committed stack" is defensible in a way "fast under load" is not. Label an estimate or a target explicitly as such rather than letting it read as a measured result. If a number can't be defended when asked "how did you measure that," it doesn't go in.

## Write the case study

A case study should cover, specifically: the problem and who it's for, the risk that actually mattered (from step 02), the key design decision and its tradeoff (from step 03), the proof that it holds (from step 05), at least one real bug found during verification and how it was caught, and what's still open or out of scope. Use [`templates/case_study_template.md`](../templates/case_study_template.md) as a starting structure.

**One more section worth adding, distinct from "what's still open":** a short hindsight reflection on what you'd do differently now. "What's still open" is about known gaps; this is about judgment that only shows up in hindsight - and reviewer-side accounts of reading junior portfolios specifically call out this kind of reflection as reading more senior, even in one short section.

## Translate into resume bullets, carefully

A resume bullet drawn from this kind of project should name the mechanism and the proof, not just a tech list: *"built X, proven by deliberately breaking Y and confirming Z"* beats *"built X using (tech, tech, tech)."* Draft new bullets as candidates and get them reviewed before they land on an actual resume - a bullet shouldn't go live silently. If a number in a drafted bullet can't be traced to a real captured run, don't draft it - figure out what's missing to make it defensible instead.

## A worked example

[`examples/stack_overflow_pipeline_bug.md`](../examples/stack_overflow_pipeline_bug.md) shows a real significant bug (a field silently null for every row since the start of a data pipeline project) written up with root cause, discovery, fix, and the real before/after numbers - the kind of writeup this step is asking for.

## Step by step, in practice

1. Draft the case study using [`templates/case_study_template.md`](../templates/case_study_template.md) while the project is still fresh - don't wait weeks and rely on memory for "how did you measure that."
2. For every number in the draft, write down next to it (in a scratch file, not the final doc) exactly how it was produced - the command, the tool, the sample size. If you can't, go re-measure it or cut the number.
3. Write at least one real bug honestly: root cause, how it was found, the fix, the regression test. If verification (step 06) genuinely found nothing, say that explicitly rather than inventing a bug for the sake of having one.
4. Draft resume bullets from the case study, not from the tech stack list - each bullet should survive "how do you know that's true" in an interview.
5. Get the bullets reviewed by someone else (or sit on them for a day) before they go on an actual resume - a bullet shouldn't go live the moment it's drafted.
6. Re-read the "what's still open" section out loud before publishing - if it's empty, that's usually a sign something wasn't looked at closely enough, not that the project is flawless.
