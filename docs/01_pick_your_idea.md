# 01 - Pick your idea

The idea matters more than people admit. A weak idea executed perfectly is still a weak project.

## The saturation check

Before scoping anything, stress-test the idea itself: would hundreds of other candidates plausibly submit the identical pitch? "Wrap an LLM," "build a CRUD app with auth," "make a clone of a famous app" are all common shapes right now, regardless of how well they're built.

The trendy shape isn't automatically disqualifying. A familiar project (a CRUD app, a checkout flow, an API wrapper) is not weak just because it's common - a conventional problem built with real depth (real concurrency handling, real authorization boundaries, real failure analysis) is often stronger interview material than a novel-sounding idea with shallow execution.

The actual test: **name the differentiator before building, not after.** Ask honestly - what does this prove that a shallow, generic version of the same idea wouldn't? If the answer is nothing beyond gluing two tools together, the idea needs a sharper angle or a replacement, not more features.

## Getting a second opinion, done properly

Asking another person or another AI for an opinion is useful - but only if you use it as a source of objections, not a verdict to defer to. The order matters:

1. **Write your own criteria and your own initial assessment first.** Know what you think before you ask.
2. **Ask specifically for counterexamples, hidden assumptions, and the strongest reason to reject the idea** - not "is this a good idea," which invites a persuasive verdict instead of useful scrutiny.
3. **Check any factual claims it makes against real evidence** rather than accepting them because they sound authoritative.
4. **Record what changed your decision and why** - if nothing changed, say that too, rather than treating the response as validation just because it came from somewhere else.

Two models (or two people) can share the same blind spot and confidently repeat the same conventional advice. A second opinion is a check on completeness, not independent proof of correctness.

## A worked example

See [`examples/document_exchange_phase0.md`](../examples/document_exchange_phase0.md) - a real case where an initial idea (a self-hosted LLM-serving gateway) was rejected specifically because the honest answer to "what does this prove" was "not much beyond what everyone else's version proves," and a second idea was scoped from scratch using a grounded second-opinion prompt.

Next: [02 - Name your risks](02_name_your_risks.md).

## Step by step, in practice

1. Write one sentence: what would this project do, and who's it for (even if the "who" is just you)?
2. Write one sentence: what's the shallow, 30-minute version of this idea that a hundred other people would also build?
3. Write one sentence: what does your version prove that the shallow version doesn't? If you can't answer this honestly, go back to step 2 with a narrower or different idea.
4. List 2-3 project ideas you're actually considering, each with its own answer to step 3. Compare them side by side rather than falling in love with the first one.
5. Write your own criteria for "this is worth building" before asking anyone else's opinion.
6. If using a second opinion (AI or human): ask for objections and the strongest reason to reject the idea, not "is this good."
7. Write down what changed your mind, or that nothing did, and why.

See [`docs/08_idea_bank.md`](08_idea_bank.md) if you don't have an idea at all yet.
