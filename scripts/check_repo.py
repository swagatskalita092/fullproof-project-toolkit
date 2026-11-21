#!/usr/bin/env python3
"""
Repo consistency check for project-blueprint.

Companion script to skill/methodology-consistency-check/SKILL.md - makes that
skill's "every link resolves" and "terminology drift" checks runnable, not just
prose. Exits non-zero (and prints what failed) on any real problem, so it can
run in CI the same way this repo tells every portfolio project to have basic CI.

Checks:
  1. Every local markdown link ([text](path)) resolves to a real file.
  2. "known limitation" and "non-goal" aren't used interchangeably (they mean
     different things: an open gap vs. something never intended to be covered).
  3. Every skill/*/SKILL.md has frontmatter with both `name` and `description`.
"""
import glob
import os
import re
import sys

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def check_links(root):
    broken = []
    checked = 0
    for f in glob.glob(os.path.join(root, "**/*.md"), recursive=True):
        with open(f, encoding="utf-8") as fh:
            content = fh.read()
        for m in LINK_RE.finditer(content):
            target = m.group(1)
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            checked += 1
            base = os.path.dirname(f)
            resolved = os.path.normpath(os.path.join(base, target))
            if not os.path.exists(resolved):
                broken.append((f, target))
    return checked, broken


def check_terminology(root):
    # Known-limitation and non-goal are defined as distinct concepts
    # (docs/05, skill/portfolio-project-rigor section 5). Flag any file that
    # explicitly conflates them ("known limitation" described as "never
    # intended to be covered", or "non-goal" described as "not yet fixed").
    problems = []
    conflate_patterns = [
        re.compile(r"known limitation[^.]{0,60}never intended", re.IGNORECASE),
        re.compile(r"non-?goal[^.]{0,60}not (yet )?fixed", re.IGNORECASE),
    ]
    for f in glob.glob(os.path.join(root, "**/*.md"), recursive=True):
        with open(f, encoding="utf-8") as fh:
            content = fh.read()
        for pat in conflate_patterns:
            if pat.search(content):
                problems.append((f, pat.pattern))
    return problems


def check_skill_frontmatter(root):
    missing = []
    for f in glob.glob(os.path.join(root, "skill/*/SKILL.md")):
        with open(f, encoding="utf-8") as fh:
            content = fh.read()
        m = FRONTMATTER_RE.match(content)
        if not m:
            missing.append((f, "no frontmatter block found"))
            continue
        fm = m.group(1)
        if "name:" not in fm:
            missing.append((f, "missing 'name' in frontmatter"))
        if "description:" not in fm:
            missing.append((f, "missing 'description' in frontmatter"))
    return missing


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    ok = True

    checked, broken = check_links(root)
    print(f"[links] checked {checked} local links")
    if broken:
        ok = False
        print(f"[links] FAIL - {len(broken)} broken:")
        for f, t in broken:
            print(f"  {f} -> {t}")
    else:
        print("[links] OK - none broken")

    problems = check_terminology(root)
    if problems:
        ok = False
        print(f"[terminology] FAIL - {len(problems)} possible conflation(s):")
        for f, pat in problems:
            print(f"  {f} matched {pat!r}")
    else:
        print("[terminology] OK - no known-limitation/non-goal conflation found")

    missing = check_skill_frontmatter(root)
    if missing:
        ok = False
        print(f"[skill-frontmatter] FAIL - {len(missing)} issue(s):")
        for f, reason in missing:
            print(f"  {f}: {reason}")
    else:
        print("[skill-frontmatter] OK - every skill has name + description")

    if not ok:
        print("\nREPO CHECK FAILED")
        sys.exit(1)
    print("\nREPO CHECK PASSED")


if __name__ == "__main__":
    main()
