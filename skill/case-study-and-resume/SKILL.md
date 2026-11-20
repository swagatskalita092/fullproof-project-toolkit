---
name: case-study-and-resume
description: Use when turning a finished project into a case study, portfolio writeup, or resume bullets - translates real work into interview-defensible material without fabricating or overclaiming.
---

# Case study and resume

A finished project and an interview-ready project are different things. This closes the gap.

**A case study should cover:** the problem and who it's for, the risk that actually mattered, the key design decision and its tradeoff, the proof that it holds (real adversarial test results), at least one real bug found during verification and how it was caught, and what's still open or explicitly out of scope.

**Resume bullets should name the mechanism and the proof, not just a tech list.** "Built X, proven by deliberately breaking Y and confirming Z" beats "built X using (tech, tech, tech)." Draft new bullets as candidates and get them reviewed before they land on an actual resume - a bullet shouldn't go live silently.

**If a number in a drafted bullet can't be traced to a real captured run**, don't draft it - figure out what's missing to make it defensible instead, or state what would be needed to measure it honestly.

**In practice:** draft the case study while the project is fresh. For every number, write down exactly how it was produced before it goes in the final doc. Write at least one real bug honestly - if verification genuinely found nothing, say that explicitly rather than inventing one. Re-read the "what's still open" section before publishing - if it's empty, that's usually a sign something wasn't looked at closely enough.

**What a reviewer actually scans for first.** Before anyone reads a case study, they open the repo - and reviewer-side accounts of what that first look actually checks are specific: a README stating the problem, the why behind it, a working setup path, an architecture snapshot, and proof (a screenshot, a GIF, a working demo). A commit history that reads as incremental and specific ("add retry logic for webhook delivery failures") rather than one dump commit or vague messages ("update code"). A small, real test suite - even a modest one signals regression-risk awareness more than a polished demo alone does. Honest failure states and clear error messages, not just a happy-path walkthrough. Fewer, more finished pinned projects beat a wall of unfinished ones. Build the case study on top of a repo that already passes this first look - the write-up can't compensate for a README that takes five minutes to make sense of.
