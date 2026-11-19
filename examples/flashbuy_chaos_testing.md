# Worked example: adversarial testing against real infrastructure

Real excerpt from a project adding durable event delivery (a transactional outbox plus a message broker) to a flash-sale checkout backend. The full original is in that project's own repo; this is a condensed version showing the method.

## The risk being tested

A checkout confirmation needs to reliably tell a separate, independent service "this order is confirmed" via a message broker - but brokers only guarantee at-least-once delivery, meaning the same message can arrive twice. The invariant: a duplicate delivery must never create a duplicate downstream job.

## The five scenarios actually run, against real Docker containers, not simulated

1. **Publisher crashes right after the broker confirms a publish, before marking it published locally.** Expected: the row stays unpublished and gets redelivered - a real, accepted duplicate. Actually run twice to force a genuine duplicate delivery of the same event ID. The consuming service's idempotent record of already-processed events caught it both times; one fulfillment job existed despite two broker deliveries.

2. **Consumer crashes after its local commit, before acknowledging the broker.** Expected: the broker redelivers the still-unacknowledged message, and the redelivery must not create a second job. Confirmed: after restart, the redelivered message was recognized as a duplicate and acknowledged without creating anything new.

   **A real bug was found here, not assumed:** the original code logged "job created" on every message, even on the duplicate-delivery path where nothing was actually created. The acknowledgment logic was correct; the log line was simply false on that path. Found by reading the actual captured output of this scenario, not by inspecting the code - fixed by tracking whether the delivery was a duplicate and logging accordingly.

3. **Sustained broker outage while normal activity continues.** Expected: confirming an order should stay a database-only operation, never blocked by the broker, and everything queued during the outage should deliver once the broker returns. Confirmed - three orders confirmed normally during the outage, all three delivered correctly once the broker came back.

   **A second real bug was found here:** on broker restart, a DNS lookup briefly failed with a plain `OSError` subclass that the retry loop's exception handler didn't catch (it only caught the message-queue library's own connection-error type), so the whole publishing process crashed instead of retrying. Confirmed via the container actually exiting. Fixed by broadening the exception handler, plus adding automatic restart as defense in depth.

4. **A malformed (poison) message must not block the queue.** Expected: it gets routed to a dead-letter queue, and a valid message sent right after it is unaffected. Confirmed directly via the broker's own queue inspection tool.

5. **No "baseline" scenario for the classic dual-write bug exists, and that's stated honestly rather than faked.** The confirmation write and the "intent to publish" write happen in the exact same database transaction - there's no code path where one could succeed without the other, so there's structurally nothing to reproduce. Saying so explicitly is more honest than manufacturing a fake failure just to have a "before" result to show.

## The point of including the bugs

Both real bugs above were found *during* this verification pass, not before it - neither would have been caught by reading the code twice. This is the actual value of running adversarial scenarios against real infrastructure instead of reasoning about what the code should do.
