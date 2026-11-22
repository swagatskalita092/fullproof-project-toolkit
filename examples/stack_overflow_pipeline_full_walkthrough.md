# Worked example: a data-correctness project, start to finish (idea → resume)

`flashbuy_full_walkthrough.md` follows a systems/concurrency project through all seven steps. This one follows a different kind of project through the same seven steps - a data pipeline ingesting the Stack Overflow Developer Survey into a layered warehouse - specifically because the risks, decisions, and tests look genuinely different when the invariant is about *correctness of published data* rather than *correctness under concurrent load*. Adapted and anonymized from a real project's documented history across seven build phases; the bugs, findings, and fixes below genuinely happened and were genuinely verified against real infrastructure, though specifics are paraphrased here rather than reproduced verbatim from the original project's own internal docs. Trimmed to what demonstrates the pipeline clearly, not the complete history.

## 01 - Pick the idea

Deliberately paired against two other projects that already proved different things: one proved systems/concurrency depth, another proved full-stack shipping ability. This one was picked to prove a third, distinct skill - data engineering correctness and evolution under a changing data source - not another dashboard or another ETL demo. The differentiator named up front, after an explicit before/after comparison against a bigger architectural swing (streaming ingestion, a full lakehouse): *"the data-engineering equivalent of chaos-testing a checkout flow isn't killing containers for their own sake, it's proving that a bad or partial run can't silently become the official published answer."* The heavier stack was deliberately rejected as manufactured complexity for a dataset that is annual and mostly static - the differentiator didn't need it.

## 02 - Name your risks

Three invariants, written before any schema redesign:

- A bad or partial pipeline run can never become the data readers actually see as published.
- A missing or renamed field, when the data source's shape changes, never gets silently reported as a false zero or default value.
- Every discrepancy between what a run produced and what's expected gets surfaced; none get silently dropped.

Credible failure modes named alongside them: two candidate runs racing to publish and resolving last-write-wins; a truncated source file loading anyway because nothing checked the row count; a genuinely-missing data field reported as "0% yes" instead of "not asked this year," which misrepresents absence as a real answer.

## 03 - Design decisions (provisional, with the rejected alternative)

- **Chosen:** an append-only release/candidate/publish pattern - every run tagged with a release id, a single pointer flipped to the new release only after tests pass, under a database advisory lock. **Rejected:** overwrite-in-place on each run. **Why:** the invariant ("never publish a bad run") is exactly the property a pointer-flip makes provable; overwrite-in-place has no safe failure state mid-run.
- **Chosen:** a `seq`-based monotonicity guard on the publish pointer. **Rejected:** trusting whichever run finishes last. **Why this changed:** not guessed upfront - two competing candidates racing to publish were found to resolve last-write-wins during testing, and the guard was added because of that evidence.
- **Chosen:** the active-release pointer scoped per data-year (a `survey_year` primary key) once a second year of data needed to be supported. **Rejected (caught in design review before code was written, not after):** keeping the original single global pointer and just adding a year column elsewhere. **Why this changed:** a global monotonicity check would have let one year's higher sequence number spuriously supersede a different year's correct, already-published release - a real cross-year bug caught on paper before it could ship.
- **Chosen:** a static dashboard, regenerated from the real published data after each run and committed to the repo. **Rejected:** a live-query dashboard. **Why:** no hosted database existed for a public page to query live, and a cloud warehouse had already been explicitly rejected as unneeded complexity - a static snapshot labeled with its own publish timestamp doesn't pretend to be more live than it is.

## 04 - Build in phases

Seven phases, each independently verified before the next started: semantics, fixtures, and a real data-quality policy → a safe, replayable publish mechanism → CI that actually runs the pipeline against hand-calculated fixtures, not just lints the code → a real failure-injection suite against live infrastructure plus measured baseline runtimes → a second real data-year added, with the schema changes that forced → one small, honest consumer-facing view → a written engineering journal covering every real investigation across the project. Each phase's "done" was a specific checkable claim (a passing test against real infrastructure, a verified commit), not a feeling that the team had moved on.

## 05 - Adversarial testing

Six real failure injections against a live, fully-running stack (database plus orchestrator, not a mock), each targeting a named invariant from step 02:

1. **A malformed, truncated source file.** Initially a real bug: the file loaded anyway, because nothing checked whether the row count had collapsed. Fixed with a new data-quality check that blocks publication when a run's row count falls far below the last published run's - reasoned explicitly against both a legitimate large real year-over-year drop and a tiny test fixture, so the check wouldn't be too strict or too loose.
2. **The loader killed mid-reload.** Rolled back cleanly; the raw table never went empty.
3. **The database killed mid-transform.** Took the orchestrator down with it too (a documented, accepted operational gap - they shared one instance) - but after manual recovery, a genuinely fresh, complete rerun still published the correct data, confirmed by comparing the republished output cell-for-cell against the clean baseline run immediately before it.
4. **A downstream correctness test failed inside a real orchestrated run.** The publish step never ran; the previous good release stayed live.
5. **The process killed right after the publish commit, before the orchestrator recorded success.** This specific race window was missed on this attempt (the kill landed a moment too late to observe the retry path) - already proven directly in an earlier phase, so not a gap, just an inconclusive rerun of an already-answered question.
6. **Two overlapping runs publishing at once.** The pointer stayed on a single, consistent release; the losing run never published - the monotonicity guard from step 03 holding under real concurrent execution, not just the unit test that first proved it.

## 06 - Verification checklist

- **CI status was checked via the API directly**, after the HTML status page showed a stale "in progress" snapshot for a run that had already finished - the exact reason step 06 of the methodology insists on the API, not the page.
- **A committed file was diffed byte-for-byte against its exact drafted source**, not just checked by automated lint/width/test passes - twice, this caught real content bugs that every automated check had missed: a diagram-rebuild that silently dropped two wildcard characters mid-word, and a documentation file whose very last sentence was truncated mid-word. Neither was caught by the passing test suite, the em-dash sweep, or the width checker, because none of those checks look at word-level content.
- **The full test suite was independently re-run against a real database container** after every phase, not trusted from a single report - 25 of 25 passing, repeated across multiple phases and both before and after fixes, not run once and assumed stable.
- **Every "done" claim was checked via a fresh clone and the actual commit hash**, confirming the right commit actually landed on the main branch, not just that a tool reported success.

## 07 - Case study and resume

**One significant, honestly-documented bug, found only because a downstream consumer-facing check forced a look at real per-cell data instead of a passing test suite:** a derived metric had been silently absent from every single published result since the very first phase. A validation pattern designed for one data format couldn't parse a differently-formatted but equally valid value, so every row with that value was dropped before the calculation ran - a passing test suite the entire time, because the original test fixtures never happened to exercise that value format. Root-caused, fixed, and a regression test added using exactly that previously-unexercised format, so the same bug class can't silently ship again.

**A known limitation, stated rather than hidden:** the orchestrator's metadata store shared the same database instance as the warehouse itself, meaning a database failure took down both at once - a real, accepted operational gap, documented plainly in the project's own known-limitations file rather than quietly omitted from the writeup.

**What I'd do differently now:** the cross-year pointer bug (step 03) was caught in design review specifically because someone asked "what happens to the sequence number across two different years" before writing code - the project's honest hindsight note is that this question should have been asked by default for every new dimension added to a previously single-valued model, not reconstructed after the fact once the risk was already visible in a draft design.

**Resume bullets that name the mechanism and the proof:**
- *"Built a release/candidate/publish safety pattern for a data pipeline with a per-dimension monotonicity guard, preventing a bad or partial run from ever becoming the published answer, verified with real crash-injection tests against live infrastructure."*
- *"Extended a single-dataset pipeline to support a second, independently-evolving data year without breaking existing published results, catching a cross-dimension correctness bug in design review before it shipped."*
- *"Found and fixed a silent data-quality bug that had zeroed out a derived metric across every published result since the project's first release, via a consumer-facing check that forced a direct look at real per-cell output instead of relying on a passing test suite."*
- *"Ran six real failure-injection scenarios against a live database/orchestrator stack, each tied to a named correctness invariant, adding a new automated data-quality gate after one injection revealed a truncated file could silently publish."*

Each bullet traces back to a specific step above, same as the other worked example - the question a bullet has to answer is whether it maps to real, verified work, not whether it reads well on its own.
