# 05 - Adversarial testing

This is usually the actual differentiator between a generic version of a project idea and a credible one: did the builder deliberately break it and prove what caught the breakage, with real captured output - not a claim that it "should" handle failure.

## Start from the risk, not the technique

Don't start with "what chaos-testing technique should I use." Start from the invariants and credible failure modes you named in step 02, and design a test for each one that actually matters. A duplicate payment callback or a leaked cross-account record deserves a deliberately designed test. Randomly killing an unrelated container may prove very little if nothing interesting depended on it surviving.

## Keep the list short and real

3-6 concrete, numbered scenarios is normal. A short list that's actually run, with real captured output, beats a long list padded for volume or improvised after the fact. Each scenario should name which invariant it's defending, so the list reads as deliberate risk coverage, not a grab-bag of chaos for its own sake.

## What "real captured output" means

Not "I expect this would work because the code looks right." Actually run the scenario - kill the process, revoke the access, remove the safety check - against real running infrastructure, and write down what actually happened: the log lines, the database state, the HTTP response. If something surprising happens (and it often does), that's usually the most valuable part of the whole exercise.

## A worked example

[`examples/flashbuy_chaos_testing.md`](../examples/flashbuy_chaos_testing.md) walks through five real adversarial scenarios run against a real Docker Compose stack for a message-queue-based event delivery feature - including two real bugs that were found only by actually running the scenarios, not by reading the code.

Next: [06 - Verification checklist](06_verification_checklist.md).

## Step by step, in practice

1. Pull your ranked invariant list from step 02.
2. For each of the top 3-6, write a scenario as a single sentence: what you'll actually do to it, and what should happen if the system holds.
3. Before running anything, write your predicted result - this is what makes a surprising actual result meaningful instead of unremarked.
4. Run it for real against real infrastructure (a real container, a real process you actually kill), and capture the literal output - logs, database state, HTTP responses - not a paraphrase.
5. If the actual result differs from the prediction, that's usually either a real bug (fix it, write it up per step 06) or a wrong assumption about the system (update step 02/03 to reflect what you now know).
6. Write the scenario, prediction, and real captured result together in your project's own docs - this pairing is what makes the test suite readable as deliberate proof rather than a log dump.
