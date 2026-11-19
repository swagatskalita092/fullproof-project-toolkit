# 09 - Drafting a research paper (same honesty rules, academic format)

This repo is mostly about engineering projects, but the same underlying discipline - name the real claim, prove it, document honestly, never fabricate a number - applies directly to writing up research. This step is for turning real experimental work into a paper or report that holds up under a skeptical reviewer, the same way the rest of this repo is about holding up under a skeptical interviewer.

## Before writing: have you actually got a result?

Don't start writing the paper to "figure out" what you found. Run the experiment, get the real numbers, and only then start writing - a paper drafted before the result exists tends to subtly shape the experiment to match the narrative already being written, instead of the other way around.

## Structure (standard, and for a reason)

- **Abstract**: the actual finding in 3-4 sentences, not a teaser. A reader should be able to decide if this paper is relevant to them from the abstract alone.
- **Introduction / motivation**: the real problem and why it matters, with the actual research question stated as a falsifiable claim - something that could, in principle, have come out false.
- **Related work**: what's already known, stated accurately - not a list of citations to look thorough, but the actual prior findings your work builds on or contradicts. Read the papers you cite; don't cite based on an abstract or a secondhand summary.
- **Method**: detailed enough that someone else could actually reproduce it - the dataset, the exact procedure, the parameters, the environment. If a reviewer (or you, in six months) can't reproduce it from this section alone, it's not detailed enough.
- **Results**: the real numbers, including the ones that don't support your hypothesis as cleanly as you'd like. Report method alongside every figure - sample size, how it was measured, what conditions - the same "no bare numbers" rule as step 07 of this repo.
- **Discussion / limitations**: state plainly what this does and doesn't show, what could confound the result, and what you'd need to test to be more confident. A paper that states its own limitations clearly is more credible, not less - the same principle as documenting known limitations in an engineering project.
- **Conclusion**: what you actually found, not what you hoped to find, and a specific, honest statement of what would need to happen next.

## The honesty rules, carried over directly

- **No fabricated or rounded numbers, ever** - every figure must trace back to something you actually ran or measured, with its method stated.
- **Don't overclaim from a small or convenient sample.** State the actual sample size and conditions next to every claim, and let the reader judge how much weight it can bear.
- **Report negative or inconclusive results honestly** rather than omitting the runs that didn't support the hypothesis - cherry-picking a result is exactly the kind of thing this repo's whole philosophy exists to avoid, in a paper just as much as a project.
- **Separate what you observed from what you're speculating about** - use clearly different language for "the data shows X" versus "this might suggest Y, though testing Z would be needed to confirm it."
- **If you used an AI tool to help draft, analyze, or code**, say so plainly wherever your institution or venue requires disclosure - don't let a convenient omission become a credibility problem later.

## Step by step, in practice

1. Write the falsifiable research question before running anything.
2. Run the real experiment, capture the real results, including surprising or inconvenient ones.
3. Write the Method section first, while the exact procedure is still fresh - it's the section most often under-detailed when written from memory later.
4. Write Results directly from your captured data, not from memory of what you expected to find.
5. Write Discussion/Limitations honestly before writing the Abstract - the abstract should summarize what the paper actually shows, not the other way around.
6. Have someone else (an advisor, a peer, or a careful second read of your own) try to reproduce your Method section from the paper alone, and fix anything they couldn't follow.
