# 06 - Verification checklist

Never trust a single report, including your own. The goal is independent evidence, not a higher count of checks - two reviews and a passing test suite can all share the same mistaken assumption and prove nothing new.

## The checklist

- **Fresh clone**, not the working directory that's been edited in place. A working directory can have uncommitted fixes or leftover state that won't exist for anyone else who checks the project out.
- **Actually run the tests against real infrastructure** (a real database/broker/container), not just read that they "should pass."
- **Fetch CI status via the API directly** (e.g. a GitHub Actions run endpoint), not an HTML status page, which can show a stale "in progress" snapshot after a run has already finished.
- **Diff the actually-committed file against the exact drafted content, byte for byte, when it matters.** A passing lint/test/width check does not catch a dropped character mid-word or a silently truncated last sentence - both have happened for real and only showed up this way.
- **Confirm a push actually landed** by comparing local HEAD to the remote branch directly. Don't assume a reported push succeeded.
- **Before trusting "the tests pass" as evidence of anything, confirm the test actually encodes the invariant that matters.** A passing suite that never asserted the real property proves nothing.

## Why this is its own step, not a footnote

It's tempting to treat "it builds, the tests are green" as the finish line. In practice, every real bug recorded in this repo's examples was found during a verification pass like this one - not during the original build. Verification isn't a formality after the real work is done; for a project whose whole point is correctness or reliability, it *is* the real work.

Next: [07 - Case study and resume](07_case_study_and_resume.md).
