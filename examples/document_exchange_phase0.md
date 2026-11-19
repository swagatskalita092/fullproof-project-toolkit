# Worked example: picking an idea, then naming risks before any code

This is a real planning pass, done before any code was written, for a project that in the end wasn't built - the planning itself is the point of this example, not the outcome.

## The idea that got rejected

The first idea floated for this project was a self-hosted LLM-serving gateway - host an open-source model, add request batching, a caching layer, and load-test it. It was rejected for a specific, named reason: the honest answer to "what does this prove that a generic version of this idea wouldn't" was "not much" - self-hosting an LLM is an extremely common 2026 portfolio shape regardless of how much polish is applied to it, and the rigor being proposed (load testing, chaos testing) didn't change what the project was fundamentally demonstrating.

## Getting a second opinion, and using it properly

A grounded prompt was written for a second AI model: the real existing projects already built, the real tech stack, explicit constraints (a tight timeline, specific skills not yet learned), and an explicit "here's why the LLM idea doesn't work, don't suggest variations of it." The response came back with three ranked ideas and reasoning for each. The response wasn't taken as a verdict - each suggestion was checked against the real constraints (one option would have required learning an entire new stack from zero, which the second opinion underweighted against an already-tight calendar) before picking one.

## The idea that was chosen

A secure, multi-tenant document-sharing platform - proving that access, once revoked, actually stays revoked, across every code path, not just that a login wall exists.

## Naming the risks, before any entity model

**What must stay true:**
1. A tenant can never read another tenant's documents or metadata, through any code path - the main API, a background job, an export, or admin tooling.
2. Once a grant is revoked, no further access succeeds for that principal - including a download already in progress.
3. The audit log is an accurate, append-only record - no application-level actor, including an admin, can alter or delete an entry.
4. A document's bytes are only ever reachable through a live grant check at the moment of access - never a cached or previously-issued path.

**Credible ways this fails in practice** (the realistic, boring causes, not contrived edge cases):
- A new endpoint or query forgets to scope by tenant - the single most common real-world cause of cross-tenant data leaks.
- A pooled DB connection or async worker carries stale tenant context into a different request than the one that set it.
- A revoke updates the grants table, but a request already in flight loaded the old permission before the update landed.
- A background export job captures a permission snapshot when it starts, finishes after a revoke, and delivers anyway.
- A previously issued access artifact (a link, a cached response) stays valid after the grant that created it is gone.
- A privileged account tampers with or deletes audit log rows to cover its own overreach.

## Design decisions, made provisional with stated revisit triggers

**Tenant isolation:** PostgreSQL Row-Level Security plus an app-layer filter, deliberately redundant - the app-layer filter catches most cases cheaply, RLS is the layer that has to hold even when the app-layer filter is missing or wrong. *Revisit if RLS's session-variable propagation proves unreliable under whatever connection-pooling/async setup gets used.*

**Downloads proxied through the app, not direct signed URLs.** Trades raw download speed for an instant, provable revocation guarantee - a signed URL already handed out can't be un-handed-out, a proxied check can enforce the grant on every request. *Revisit only if a real measured latency problem shows up under load that direct serving would meaningfully fix.*

**No permission caching** until a real measured need appears - every access check hits the real grants table at the moment of serving bytes.

**Background jobs re-check permission at delivery time, not job-start time.**

**Audit log append-only enforced at the database privilege level** - the app's own DB role lacks UPDATE/DELETE privilege on that table entirely, so even a compromised admin account can't erase the record through the app.

## Entity model, built to hold the invariants above

Organization -> Workspace -> Member/Reviewer -> Document -> Grant -> AuditLog.

## The adversarial test plan this scoping produced

1. Remove the app-layer tenant filter on one endpoint; confirm RLS alone still blocks cross-tenant access. *(Invariant 1)*
2. Simulate a pooled DB connection reused across two tenants' requests; confirm no leakage. *(Invariant 1)*
3. Revoke access mid-session; confirm an in-flight download is cut off immediately. *(Invariant 2)*
4. Start a background export before a revoke, let it finish after; confirm it respects the state at delivery time. *(Invariant 2)*
5. Attempt to reuse a previously valid access path after revocation; confirm it's rejected. *(Invariant 2, 4)*
6. Attempt to delete or alter an audit log row via a compromised admin account; confirm the database privilege model blocks it outright. *(Invariant 3)*

This project wasn't ultimately built - the person planning it decided their real goal was a different kind of project (this repo, in fact). The scoping work above is reused here because it's a genuine, complete example of steps 01-03 and the start of 05, done properly, even though the product itself never got past this stage.
