# Worked example: documenting a real bug honestly

Real excerpt from a data pipeline project (ingesting survey data, transforming it through layered models into published analytics), describing one significant bug found and fixed - written the way step 07 of this repo asks for.

## What was wrong

One field - the average of a job-satisfaction rating - had been silently null for every single published row since the very start of the project. A regex meant to validate that the raw value was numeric rejected the real data format (a decimal like "8.0"), so every row with an actual answer was quietly dropped before the average was calculated. Every published cell showed zero real data for this field, and a downstream dashboard was about to label all of it "not asked," which was false - the question had been asked, the code just couldn't parse the real answer format.

## How it was found

Not by a test failing - every existing automated test was green. It was found by building a dashboard that displayed real per-cell data coverage, and noticing the coverage was suspiciously, uniformly zero. Looking at the real data directly surfaced what the passing test suite had missed, because the original hand-written test fixtures never happened to include a decimal-formatted value.

## The fix

Widened the validation regex to accept decimal values. After reprocessing the real data: the large majority of previously-empty cells now had a genuine computed average; the remainder were still correctly null, because those specific cells really did have no answer.

## The regression test

A new test case was added using a decimal-formatted value specifically, so this exact bug class - a validation rule silently rejecting a valid real-world data format - can't ship again unnoticed.

## Why this is in the documentation at all

This bug is more significant than most of the others found in this project, and it's written up in full rather than fixed quietly. A project's credibility comes from exactly this kind of honest account - a real, consequential mistake, how it was actually caught, and what now prevents it from recurring.
