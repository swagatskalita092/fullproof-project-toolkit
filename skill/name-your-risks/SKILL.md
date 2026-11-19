---
name: name-your-risks
description: Use before designing the architecture of a project whose point is correctness, security, or reliability - identifies what must stay true and how it credibly fails, before any entity model exists.
---

# Name your risks

Before locking an architecture, write down what must stay true for the project to actually be correct, and how it could plausibly fail. Start from the risk, not the technique.

**Invariants:** plain, falsifiable sentences of the form "this has failed if ___ becomes possible." For a multi-tenant system: "a user from one account can never read another account's data." For a checkout flow: "inventory is never sold below zero."

**Credible failure modes:** for each invariant, name the realistic, boring way it actually breaks - a forgotten filter on a new endpoint, a race between two requests, a cache that doesn't invalidate, a background job acting on stale state. These are the real shapes bugs take, and naming them up front turns "I tested it" into "I tested the thing that was actually likely to go wrong."

**Why this comes first:** an architecture designed without naming the risks tends to bolt correctness on as an afterthought. Naming the risk first means the entity model gets built to serve it, not the other way around.

**In practice:** finish "this project has failed if ___" at least twice. Rank the invariants by how bad a violation would be - the worst ones get the most adversarial testing later. Only then sketch the entity model, checking each piece against the list.
