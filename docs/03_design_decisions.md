# 03 - Design decisions

Write down the architecture and the specific tradeoffs chosen, each with the alternative that was rejected and why - before building the harder parts.

## Record decisions as provisional, not locked

Hold these as provisional, not permanently fixed. Some decisions genuinely need a small implementation experiment before they can be made well, and writing "decided" on a guess just to look decisive rewards defending that guess later instead of updating it when you learn more.

For each real decision, write down:
- **What was chosen.**
- **What was rejected, and why.**
- **What would make you revisit it.** A real trigger, not "if I feel like it" - e.g. "revisit if latency under load makes this untenable," not a vague hedge.

A good decision entry reads like: *"Proxying downloads through the app instead of using direct signed URLs - trades raw speed for an instant, provable revocation guarantee. Revisit if latency under load makes this untenable."* One sentence like that is worth more in an interview than an architecture diagram, because it shows a decision was made deliberately, for a stated reason, not defaulted into.

## Why this matters more than it looks like it does

Changing a foundational decision after the first real phase is built is a rewrite, not a patch. This is the cheapest phase to get right and the most expensive to get wrong later, even though it produces no visible progress - resist the pull to skip straight to code.

## Template

Use [`templates/design_decisions_template.md`](../templates/design_decisions_template.md) to fill this in for your own project.

## A worked example

[`examples/document_exchange_phase0.md`](../examples/document_exchange_phase0.md) has five real decisions recorded this way, each with its rejected alternative and revisit trigger, for a secure document-sharing project that was scoped (but not built) using this exact process.

Next: [04 - Build in phases](04_build_in_phases.md).
