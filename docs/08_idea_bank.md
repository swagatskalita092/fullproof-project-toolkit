# 08 - Idea bank

A starting list for "I want to build something but don't have an idea yet." Every entry here is deliberately described by **the invariant it would need to prove**, not just a feature list - because per [01 - Pick your idea](01_pick_your_idea.md), the feature list is exactly the part that's common. Pick a domain you have some real interest in, not just whatever looks most impressive - you'll actually finish and defend the one you're genuinely curious about.

Use this as a starting point, not a menu to copy verbatim - the moment you narrow one of these to your own specific angle and stack, run it through [01](01_pick_your_idea.md) properly.

## Systems / concurrency
- **A booking or reservation system under contention** (seats, slots, limited inventory). Invariant: never double-book the same slot under concurrent requests. Differentiator: prove it with real concurrent load, not just a unique constraint you assume works.
- **A distributed rate limiter.** Invariant: the limit holds even when enforcement is spread across multiple instances with no shared memory. Differentiator: prove it under real multi-instance load, including a node joining/leaving mid-test.
- **An event-delivery pipeline between two services** (outbox pattern, message broker). Invariant: at-least-once delivery never becomes a duplicate side effect. Differentiator: prove it by actually crashing the publisher and consumer at the worst possible moments.

## Data correctness
- **A data pipeline with a safe publish/rollback mechanism.** Invariant: a bad or partial run can never become the "official" published answer. Differentiator: prove a crash mid-run leaves the previous good version live, not a half-finished one.
- **A schema-evolution-safe ingestion pipeline** (same pipeline, data source changes shape over time - new fields, removed fields, renamed columns). Invariant: a missing field never gets silently reported as a false "zero" or default value.
- **A reconciliation job between two systems of record** (e.g. an internal ledger vs. a payment provider's records). Invariant: every discrepancy gets surfaced, none get silently dropped.

## Security / authorization
- **Multi-tenant access control with real revocation** (see `examples/document_exchange_phase0.md` in this repo for a full worked scoping of this one). Invariant: once access is revoked, it's actually gone everywhere, immediately.
- **An audit-log system that survives a compromised admin account.** Invariant: the log can't be altered or deleted through the application, even by a privileged account.
- **A secrets-rotation system.** Invariant: a credential rotation never causes a window where either the old or new credential briefly doesn't work.

## Reliability / infrastructure
- **A caching layer with correct invalidation.** Invariant: a cached value is never served after the source of truth has changed in a way that matters. Differentiator: most cache projects never actually test invalidation under concurrent writes.
- **A job queue with real retry/backoff and poison-message handling.** Invariant: a permanently-failing job can't block everything behind it, and a transient failure doesn't get abandoned too early.
- **A deployment/rollback pipeline with a real health-check gate.** Invariant: a bad deploy never fully replaces a good one before health checks pass.

## AI/ML-adjacent (use with the saturation check especially carefully here - this is the most crowded category in 2026)
- **An evaluation/regression-testing harness for LLM outputs** (not another chatbot - tooling that catches when a prompt or model change silently makes outputs worse). Invariant: a quality regression gets caught before it ships, not after a user complains.
- **A cost/latency observability layer for an AI feature already in production.** Invariant: every dollar and every millisecond is attributed to a real, traceable request, not estimated.

## How to actually use this list

Pick one, then immediately go write its invariants properly using [02 - Name your risks](02_name_your_risks.md) - the one-line invariant above is a starting point, not the finished analysis. If none of these fit, use the same thinking pattern on your own idea: state it as "what must never happen," not "what features it has."
