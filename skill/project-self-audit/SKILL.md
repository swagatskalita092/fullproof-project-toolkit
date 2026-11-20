---
name: project-self-audit
description: Use when a project already exists (yours or someone else's) and you want an honest check of whether it's actually interview-ready against this repo's pipeline - not a rubber stamp, a real audit that can come back with real gaps.
---

# Project self-audit

Point this at a project that's already built - partway or fully - and it checks that project against the nine steps, one at a time, looking for evidence, not self-report. The point of this skill is to resist the pull toward "looks good to me." A project that gets audited and comes back with zero gaps either is genuinely exceptional or the audit wasn't honest - and the second is far more common, so treat a clean result with more suspicion, not less.

## How to run it

Go through the checklist below in order. For each item, look for the actual artifact (a file, a commit, a captured test run) - don't accept a claim that something was done without seeing it. Mark each one **Pass** (evidence exists and holds up), **Gap** (missing, thin, or asserted without evidence), or **N/A** (genuinely doesn't apply, state why).

1. **Differentiator named** (step 01). Is there a written answer to "what does this prove that a shallow, generic version wouldn't"? If the only answer you can construct is a feature list, that's a Gap, not a Pass.
2. **Invariants stated as falsifiable sentences** (step 02). Find the actual sentence - "X can never happen." A README that only describes features, with no explicit invariant anywhere, is a Gap even if the code might secretly honor one.
3. **Decisions recorded with a rejected alternative and a revisit trigger** (step 03). Look for the alternative and the "why not," not just the choice made. A decisions doc that only lists what was chosen is a Gap - the rejected alternative is the part that proves the choice was deliberate.
4. **Phases independently verified, not just sequential** (step 04). Check for evidence each phase was checked before the next started (commit messages, a log, a changelog) - not just that the final result works.
5. **Adversarial tests that target the named invariants, with real captured output** (step 05). This is the one worth checking hardest: find the actual output of a real run (a log, a terminal capture, a CI artifact), not a sentence claiming "tested for X." No captured output behind a claimed adversarial test is a Gap, full stop - it's the single most common thing that gets asserted without evidence.
6. **Verification done independently, not just trusted** (step 06). Was this checked from a fresh clone, against real infrastructure, with CI status pulled directly rather than read off a page? If the only evidence is "I ran it and it worked," treat that as thin, not absent - note it as a partial Pass with what's missing.
7. **Documentation includes at least one real bug, honestly** (step 07/honest-documentation). A project with a "known limitations" section that's empty, or no bug write-up at all, is worth a direct question: was verification actually adversarial enough to find anything, or did it just not look? Don't assume the project is flawless - assume the audit stopped too early.
8. **No fabricated or unlabeled numbers anywhere in the docs.** Spot-check two or three numeric claims - can each one be traced to a method, environment, and workload? An unlabeled "fast" or a rounded number with no source is a Gap.
9. **Resume/case-study claims match what's actually demonstrated.** Read any drafted resume bullets or case-study claims against the evidence above - a claim that outruns what steps 1-8 actually showed is a Gap, regardless of how good the underlying project is.

## Reporting the result

List every Gap found, specifically - not "could be stronger," but "no captured output exists for the claimed duplicate-delivery test" or "the decisions doc doesn't name what was rejected." Don't soften a Gap into a suggestion if it's actually missing evidence. If everything above genuinely passes, say so plainly, but name what was checked and how, so the Pass is itself verifiable - a one-word "looks great" is not a real audit result.

This is the same discipline the rest of this repo applies to a project's own claims, pointed at the project as a whole: don't trust a single pass, including this one - a second person (or a second run of this same audit later, after changes) is still worth more than one confident read.
