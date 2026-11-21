# Worked example: one project, start to finish (idea → resume)

The other examples in this repo show one step in isolation. This one follows a single real project - a flash-sale checkout backend built for limited, contended inventory - through all nine steps, so the connections between them are visible: how a named risk in step 02 becomes the adversarial test in step 05, how a provisional decision in step 03 gets revisited once step 05 actually tests it, and so on. Adapted and anonymized from a real project's documented history - the bugs, findings, and fixes below genuinely happened and were genuinely verified against real infrastructure, though specifics are paraphrased here rather than reproduced verbatim from the original project's own internal docs. This also isn't the complete history of that project - it's trimmed to what demonstrates the pipeline clearly, not everything that ever happened.

## 01 - Pick the idea

Paired, deliberately, against a separate full-stack project that already proved shipping ability end to end. This one was picked specifically to prove something that project didn't: systems-level backend depth under real concurrent load - race conditions, distributed locking, idempotency, queuing, and measured performance, not another CRUD app or another full-stack demo. The differentiator named up front: *"this proves I can reason about correctness under contention, not just ship a working feature."*

## 02 - Name your risks

Three invariants, written as plain, falsifiable sentences before any code:

- Fixed inventory is never oversold, no matter how many buyers hit it concurrently.
- A retried or duplicated checkout request never double-reserves or double-charges.
- The system stays responsive under a real concurrent surge - it doesn't silently degrade into timeouts or errors as load grows.

Credible failure modes named alongside them: two concurrent buyers both reading "stock available" before either writes (the classic race); a fixed admission rate creating a backlog that overwhelms the server under sustained load; a replica that freezes and later resumes still believing it's allowed to admit buyers, after another replica has already taken over.

## 03 - Design decisions (provisional, with the rejected alternative)

- **Chosen:** row-level locking (`SELECT FOR UPDATE`) plus idempotency keys and reservation expiry. **Rejected:** optimistic concurrency with conflict-and-retry. **Why:** a hard correctness guarantee under contention mattered more than throughput here, and the invariant ("never oversell") is exactly the kind of property locking makes provable rather than probable.
- **Chosen:** a Redis sorted-set waiting room with token-bucket admission. **Rejected:** accept every request and queue downstream. **Why:** keeps checkout's own latency predictable under surge instead of pushing the overload problem one layer down. **Revisit if:** the waiting room itself becomes the bottleneck instead of checkout.
- **Chosen:** Server-Sent-Events push-based admission. **Rejected:** status polling (the original choice). **Why this changed:** not guessed upfront - a real stress test in step 05 found polling's actual backlog cost, and the decision was revisited because of that evidence, not before it.
- **Chosen:** Redis-lock leader election across replicas via a Lua script. **Rejected:** a dedicated consensus service (etcd/ZooKeeper). **Why:** kept operational complexity proportionate to a portfolio-scale deployment. **Revisit if:** replica count grows past a handful.

## 04 - Build in phases

Roughly: a naive checkout, deliberately built broken first to prove the race condition exists → fixed for correctness (locking, idempotency, reservation expiry) → a waiting room and rate limiting → observability and a first load test → SSE push replacing polling, once step 05 showed why → multi-instance scaling with leader election → a fencing token closing a gap step 05 found in that design → a second, independent fulfillment service added later via a transactional outbox and a message broker. Each phase got its own verification (next section) before the next one started - phases weren't marked done because the team moved on, they were done because they were checked.

## 05 - Adversarial testing

- **The backlog stress test.** Not a vague "load test" - a scenario specifically designed to target the "stays responsive" invariant: admission rate crossed against reservation TTL under sustained concurrent load. It found a real, large number of failed requests under the original polling design (tens of thousands of real `503` responses in one run, captured, not estimated) - the evidence that forced the SSE redesign in step 03.
- **The frozen-leader drill.** A live container freeze/unfreeze, not a thought experiment - pausing the leader replica mid-operation and resuming it later, to check whether it could still incorrectly believe it was allowed to admit buyers. It found a real split-brain gap, fixed with an epoch-based fencing token checked atomically inside the same lock-acquisition script, then verified with both a deterministic regression test and a repeat of the same live freeze/unfreeze drill.
- **Five numbered scenarios against the fulfillment service**, run against real database/broker containers, not simulated: the publisher crashing right after a broker-confirmed publish (checking for a duplicate delivery - found one, and confirmed the idempotent consumer caught it); the consumer crashing after committing locally but before acknowledging the broker (checking safe redelivery); a sustained broker outage while checkouts kept happening (checking that confirmations never depend on the broker being up, and that everything queued got delivered once it came back); a malformed message routed to a dead-letter queue without blocking the valid message behind it; and a fifth "scenario" that was really an explanation, not a test - why no "dual-write loss" baseline was run, because the outbox write and the status write share one database commit, so there's structurally no code path where one could happen without the other.

## 06 - Verification checklist

- CI status was checked via the GitHub API directly at least once, after the HTML Actions page showed a stale "in progress" snapshot for a run that had already finished - a direct illustration of why step 06 insists on the API, not the page.
- A full from-scratch re-verification was run - fresh clone, clean rebuild, a real fresh load-test run, an independent direct database check - specifically because two earlier internal status notes disagreed with each other. Rather than trust either, both were set aside and re-checked from zero.
- The fulfillment service's four real bugs (below) were only found by actually running the new service against real Postgres, Redis, and broker containers end to end - not by reading the code and reasoning that it should work.

## 07 - Case study and resume

**Two early bugs, documented honestly:** a connection-pool exhaustion bug under load (fixed via pool sizing and a proper `503` instead of a bare `500` on transient errors), and a false-failure bug where an overly strict post-commit check flagged successful orders as failed (fixed by checking for order-row existence instead of an exact stock match). Both root-caused, fixed, and given a regression check.

**Four bugs found while verifying the fulfillment service**, written up rather than smoothed over: a consumer callback missing a required argument that crashed on the very first real message; an API response typed to return integers while actually returning a UUID string, failing response validation on every call; two new services colliding on the same container port; and a retry loop that caught one specific connection-error type but not the plain DNS error a broker restart actually raised, which escaped retry handling entirely. All four were fixed, and the fourth specifically led to a defense-in-depth change (automatic container restart added on top of the code fix), not just a patch.

**A known limitation, stated rather than hidden:** after the frozen-leader drill, the load balancer kept routing to the frozen replica for roughly a minute before giving up on it - a real, still-open gap (no upstream health check or timeout configured yet), documented plainly rather than quietly left out of the writeup.

**Resume bullets that name the mechanism and the proof:**
- *"Built a flash-sale checkout backend using row-level locking, idempotency keys, and a Redis-backed virtual waiting room with token-bucket rate limiting to prevent overselling under concurrent load."*
- *"Load-tested full buyer journeys at hundreds of concurrent users, diagnosed a real capacity limit via a targeted stress test, and fixed it with a Server-Sent-Events push architecture - eliminating tens of thousands of errors per run."*
- *"Scaled to multiple replicated instances with Redis-lock leader election, then closed a real split-brain gap (a frozen-then-resumed leader could admit twice) with an epoch-based fencing token, verified with a deterministic regression test and a live failure drill."*
- *"Added a second, independent service decoupled via a transactional outbox and a message broker, proving at-least-once delivery survives broker outages and crash-injected duplicate deliveries without ever creating a duplicate downstream job."*

Each bullet traces back to a specific step above - that's the actual test a bullet has to pass, not whether it sounds impressive on its own.
