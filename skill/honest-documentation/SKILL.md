---
name: honest-documentation
description: Use when writing up a project's README, engineering journal, or any claim about what it does - documents bugs and limitations honestly and never states a number that can't be traced to a real measurement.
---

# Honest documentation

Every real bug found during verification gets written up: root cause, the fix, and a regression test - never softened, hidden, or quietly fixed without a trace. Known limitations that aren't being fixed get stated explicitly ("documented, not fixed") rather than omitted.

**Why this is the actual credibility signal.** A project that admits its gaps reads as more trustworthy than one that claims perfection - and in an interview, "here's a real bug I found and how" is a stronger answer than a project that supposedly has none.

**No fabricated or rounded numbers, ever.** Every metric must trace back to a real captured run, with its method, environment, and workload stated, not just a bare figure. Label an estimate or target explicitly as such. If a number can't be defended when asked "how did you measure that," it doesn't go in.

**When evidence conflicts with an existing claim**, flag the conflict explicitly rather than quietly reconciling it in the more flattering direction. Deferring a fix is fine if stated as a deliberate, time-boxed decision; silently ignoring the discrepancy is not.

**When asked to assess a project's quality**, give the honest read, not the flattering one. Resist agreeing to "is this good enough, nothing left to add" - give genuine credit where earned, but name the real, still-open items. Superlatives aren't verifiable against any benchmark - describe concretely what's strong and what's open instead.
