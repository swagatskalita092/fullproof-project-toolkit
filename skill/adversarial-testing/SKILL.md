---
name: adversarial-testing
description: Use when designing how to prove a system holds under failure, attack, or edge-case load - builds a test suite from named risks/invariants rather than arbitrary chaos.
---

# Adversarial testing

The single biggest differentiator between a generic version of a project and a credible one: did the builder deliberately break it and prove what caught the breakage, with real captured output - not a claim that it "should" handle failure.

**Start from the risk, not the technique.** Don't start with "what chaos tool should I use." Start from the invariants and credible failure modes already named (see the name-your-risks skill), and design a test for each one that actually matters. A duplicate payment callback deserves a deliberately designed test; randomly killing an unrelated container may prove very little.

**Keep the list short and real.** 3-6 concrete, numbered scenarios is normal. A short list that's actually run, with real captured output, beats a long list padded for volume or improvised after the fact. Each scenario should name which invariant it defends.

**Real captured output, not expectation.** Actually run the scenario against real running infrastructure - kill the process, revoke the access, remove the safety check - and write down what actually happened: the log lines, the database state, the response. Surprising results here are usually the most valuable part of the whole exercise.

**In practice:** for each top-ranked invariant, write the scenario, your predicted result, then the actual captured result. A mismatch between predicted and actual is either a real bug (fix and document it) or a wrong assumption about the system (update the design).
