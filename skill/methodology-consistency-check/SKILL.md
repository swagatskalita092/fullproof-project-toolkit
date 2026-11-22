---
name: methodology-consistency-check
description: Use when adding, editing, or reviewing a skill or doc in this repo (Fullproof Project Toolkit) itself - checks that the repo's own methodology doesn't contradict itself, and that cross-references actually resolve. For maintaining the repo, not for auditing someone's project (use project-self-audit for that).
---

# Methodology consistency check

This repo's own credibility depends on it following its own rules: no claim without evidence, no contradiction papered over. This skill is the check that the methodology itself still holds together after a change - run it whenever a doc or skill is added or edited, not just once.

## What to actually check

1. **Every link resolves.** Every `docs/NN_*.md`, `skill/*/SKILL.md`, `templates/*.md`, and `examples/*.md` path referenced anywhere (README, docs, skills) has to point at a file that actually exists, at the path given. A broken relative link is an easy, embarrassing thing for a visitor to hit first - check it with an actual file-existence check, not by eye.
2. **Terminology means the same thing everywhere.** "Invariant," "provisional decision," "adversarial test," "known limitation" vs. "non-goal" - each has a specific meaning established in docs 02-07. If a skill uses one of these terms in a way that drifts from the doc's definition (e.g. a skill that treats "known limitation" and "non-goal" as interchangeable, when step 05 of the umbrella skill explicitly distinguishes them), that's a real inconsistency, not a style nitpick.
3. **No skill contradicts another skill or its own source doc.** Each focused skill is supposed to be a distilled version of its matching doc - if a doc says something is provisional and the matching skill implies it should be locked early, or two skills give conflicting guidance on the same step, that's the actual failure mode this check exists to catch.
4. **New content doesn't quietly weaken an existing rule.** Check additions against the core non-negotiables: no fabricated/rounded numbers, no claim without traceable evidence, provisional decisions stay provisional, document bugs honestly. A new section that drifts toward "this is fine to estimate" or "this can be asserted without a test" is a regression even if it reads smoothly.
5. **The umbrella skill (`portfolio-project-rigor`) and the split skills stay in sync.** If a split skill gains real new guidance (like a new corroborated addition), check whether the umbrella skill's matching section should get the same addition - they're meant to be the same content at two grain sizes, not two independently-evolving versions.

## A runnable companion exists

`scripts/check_repo.py` makes the link-resolution and terminology-drift checks above actually runnable, not just a procedure to eyeball - `python3 scripts/check_repo.py .` from the repo root, and `.github/workflows/check.yml` runs it on every push/PR. Run it first; use the prose checks above (skill contradictions, umbrella/split sync) for what a script can't catch.

## How to report it

List what was actually checked (which files, which terms, which skill pairs) and what was found - a broken link with its exact path and where it's referenced, a specific terminology drift with both locations quoted, or "checked N links and M skill/doc pairs, found nothing" if genuinely clean. Don't report "looks consistent" without naming what was actually compared - that's the same rubber-stamp failure mode this whole repo is built to avoid, just pointed at the repo's own content instead of someone else's project.
