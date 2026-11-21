# Changelog

All notable changes to this repo. Dates are when the change was committed.

## [1.0.0] - 2026-11-21

Initial stable release. Everything below shipped in the run-up to this tag.

### Added
- The core methodology: nine docs (`docs/01` through `docs/09`), each ending in a "step by step, in practice" checklist - idea selection, naming risks, design decisions, phased builds, adversarial testing, independent verification, case study and resume writing, an idea bank, and research-paper drafting.
- Four fillable templates (`templates/`) and three real worked examples (`examples/`) drawn from actual, independently verified projects.
- Twelve importable Claude skills (`skill/`): the whole pipeline as one umbrella skill, eight focused skills (one per step), a router (`start-here`), a self-audit (`project-self-audit`), and a maintainer-facing consistency check (`methodology-consistency-check`).
- A hand-authored, animated hero banner, section-divider graphic, and a risk→test→evidence diagram (`docs/assets/`) - built and visually verified (via Playwright screenshots) before shipping, in the same thin-line/pulsing-node visual language throughout.
- A full end-to-end worked example (`examples/flashbuy_full_walkthrough.md`) applying all nine steps to a single real project front-to-back, alongside the three single-step excerpts.
- A real, runnable repo-consistency script (`scripts/check_repo.py`) checking for broken local links, terminology drift, and missing skill frontmatter - wired into GitHub Actions (`.github/workflows/check.yml`) so it runs on every push and PR.
- `CONTRIBUTING.md` and badges (license, skill count, doc count, PRs welcome).

### Research-backed additions
- A sixth idea-bank domain, *developer tooling / technical deep-dives*, added after verifying a real source on what gets a repo pinned vs. read as generic AI-wrapper noise.
- A "what I'd do differently now" hindsight-reflection section (case study template, `docs/07`, and the relevant skills), added after verifying a real source on what separates a junior portfolio from a senior-reading one - kept distinct from "what's still open" (hindsight judgment vs. a known gap).
- Claims from sources that turned out to be dead links or unrelated profile pages were explicitly not added - this repo holds its own research additions to the same no-fabricated-claim standard it asks of a project's README.

### Fixed
- An early commit picked up an unwanted co-authorship trailer from a generic default; amended and force-pushed so the repo's history shows only its actual author.
- A hero-banner SVG border animation (`stroke-dasharray`) was set shorter than the actual path perimeter, producing a broken dashed border instead of a clean draw-in - caught via a Playwright screenshot before shipping, fixed by correcting the value.
- The hero banner's text block was shifted up slightly after a layout review found too much empty space above it.
