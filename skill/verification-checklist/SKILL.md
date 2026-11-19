---
name: verification-checklist
description: Use before declaring any phase, feature, or claim "done" - verifies independently instead of trusting a single report, including your own.
---

# Verification checklist

Never trust a single report, including your own. The goal is independent evidence, not a higher count of checks - two reviews and a passing test suite can all share the same mistaken assumption and prove nothing new.

**The checklist:**
- Fresh clone, not the working directory that's been edited in place.
- Actually run the tests against real infrastructure (a real database/broker/container), not just read that they "should pass."
- Fetch CI status via the API directly, not an HTML status page, which can show a stale "in progress" snapshot after a run has already finished.
- Diff the actually-committed file against the exact drafted content byte for byte when it matters - a passing lint/test/width check does not catch a dropped character mid-word or a silently truncated sentence.
- Confirm a push actually landed by comparing local HEAD to the remote branch directly.
- Before trusting "the tests pass" as evidence of anything, confirm the test actually encodes the invariant that matters.

**Why this is its own step, not a footnote:** it's tempting to treat "it builds, tests are green" as the finish line. In practice, the real bugs in a project are usually found during a verification pass like this, not during the original build. For a project whose whole point is correctness or reliability, verification *is* the real work, not a formality after it.
