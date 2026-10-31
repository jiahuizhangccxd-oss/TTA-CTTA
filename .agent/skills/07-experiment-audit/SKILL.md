---
name: 07-experiment-audit
description: Independently inspect a named completed experiment only when explicitly requested, and report the few validity problems that would change the result, interpretation, or next research decision.
---

# 07 Experiment Review

## Purpose

Review whether one reported result supports its intended conclusion. Remain
read-only unless revision is separately requested.

## Required Evidence

[Paper Skill Core](../../PAPER_SKILL_CORE.md), the claimed result, actual protocol,
implementation, data/split, baseline, outputs, metrics and uncertainty.

## Workflow

1. Identify the conclusion and inspect only its load-bearing evidence.
2. Check leakage, comparison fairness, independent unit, treatment delivery/use,
   metric correctness and implementation-method agreement.
3. Reproduce a critical calculation only when needed to decide validity.
4. Report new conclusion-changing findings once, with the smallest correction or
   decisive rerun. Do not create a comprehensive audit package or reviewer loop.

## Output

The conclusion still justified, located validity findings, necessary correction
and whether the evidence is currently usable in the paper.

## Validation

Anchor each finding to inspected evidence or a reproducible counterexample.
Distinguish unavailable evidence from demonstrated invalidity; do not claim
independence while modifying the experiment being reviewed.
