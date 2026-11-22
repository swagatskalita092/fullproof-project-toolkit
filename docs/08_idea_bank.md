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

## Developer tooling / technical deep-dives
A category worth calling out on its own: reviewer-side accounts of what actually gets a repo pinned in 2026 consistently point at technical depth that's hard to fake with a thin AI-generated wrapper - a compiler, a database, a protocol implementation - over another CRUD app or chatbot demo. The depth has to be real, though; a toy version with no adversarial proof is just a smaller version of the same problem.

- **A toy compiler or interpreter for a real, if small, language subset.** Invariant: every program in a defined valid-input corpus produces the documented correct output, and every program in an invalid corpus is rejected with a clear error - not just "parses the happy path." Differentiator: build an adversarial corpus of edge cases (operator precedence, recursive definitions, malformed input) and prove the implementation holds against all of it, not a demo script.
- **A minimal storage engine** (an LSM-tree or B-tree backed key-value store). Invariant: a crash mid-write never corrupts or loses a previously committed record. Differentiator: prove durability by killing the process mid-write under a fuzzed workload and confirming the write-ahead log replays to a consistent state - not an assumption that `fsync` makes it safe.
- **A protocol implementation that actually interoperates** (a simplified real protocol, or a custom RPC layer tested against a reference client). Invariant: out-of-order, duplicated, or dropped packets never violate the protocol's stated delivery/ordering guarantee. Differentiator: prove it against a real packet-loss/reorder simulation (e.g. `tc netem`), not a clean-localhost demo.
- **A build or dev tool with a correctness property, not just convenience.** Invariant: the same input always produces the same output (a reproducible build or cache), or a cached value is never served after its invalidating input changed. Differentiator: prove reproducibility or invalidation across repeated runs and environments, not "works on my machine."

## Observability / monitoring tooling
A seventh domain worth calling out on its own, grounded in a real account from a well-known engineering blogger (Gergely Orosz, writing up a side project that included its own Prometheus/Grafana monitoring stack): production-grade observability is "typical for a production service, but rarely seen in a side project." That gap is the differentiator - most portfolio projects skip instrumentation entirely, so a project that treats observability as a first-class correctness concern (not an afterthought bolted on for the demo) stands out structurally, independent of the domain it's monitoring.

- **A metrics/tracing pipeline for a system you actually built**, not a toy counter. Invariant: every real request that hits the system is traceable end to end - no request silently vanishes from the trace with no explanation. Differentiator: prove it by deliberately dropping a span or losing a metric sample under load and showing the gap is detected, not silently absorbed.
- **An alerting system with a real false-positive/false-negative budget.** Invariant: a real incident always fires an alert, and a non-incident never does (within a stated, measured rate - not "basically never"). Differentiator: prove both directions with real injected scenarios, not just a threshold you picked and never tested against actual noise.
- **A log-aggregation or structured-logging layer with a correctness property.** Invariant: a log line's field schema can evolve without silently breaking every downstream query that reads it (the same schema-evolution risk the data-correctness domain names, applied to logs instead of a warehouse). Differentiator: prove it by evolving the schema mid-project and showing old and new log shapes both still query correctly.

## How to actually use this list

Pick one, then immediately go write its invariants properly using [02 - Name your risks](02_name_your_risks.md) - the one-line invariant above is a starting point, not the finished analysis. If none of these fit, use the same thinking pattern on your own idea: state it as "what must never happen," not "what features it has."
