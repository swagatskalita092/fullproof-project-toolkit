# 02 - Name your risks

Before you lock an architecture, write down what must stay true for the project to actually be correct, and how it could plausibly fail. Not "what testing technique should I use" - start from the risk, not the technique.

## What must stay true (the invariants)

These are the properties that, if violated, mean the project has actually failed, not just that something looks ugly. For a payments feature: "a payment is never processed twice for the same user action." For a multi-tenant system: "a user from one account can never read another account's data." For a checkout flow: "inventory is never sold below zero."

Write these as plain, falsifiable sentences. If you can't state the invariant, you don't yet understand the risk you're trying to protect against.

## Credible ways this fails in practice

For each invariant, name the realistic way it actually breaks - not a contrived scenario, the boring, common one. A duplicate payment callback, a race between two requests updating the same row, a background job that captures stale state before finishing after something changed, a cache that doesn't get invalidated when the source of truth changes. These are the actual shapes bugs take in real systems, and naming them up front is what turns "I tested it" into "I tested the thing that was actually likely to go wrong."

## Why this comes before the entity model

An architecture designed without naming the risks first tends to bolt security/correctness on as an afterthought - a permissions check added to an endpoint that was already built assuming it wasn't needed, a cache added for performance without anyone asking what happens when the underlying data changes. Naming the risk first means the entity model gets built to serve it, not the other way around.

## A worked example

See [`examples/document_exchange_phase0.md`](../examples/document_exchange_phase0.md) for a full real instance: four invariants named first (tenant isolation, instant revocation, an untamperable audit log, no bypass of the access check), the credible failure mode for each one, and only then an entity model built specifically to hold those invariants.

Next: [03 - Design decisions](03_design_decisions.md).
