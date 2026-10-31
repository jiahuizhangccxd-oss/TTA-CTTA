---
name: statistical-analysis
description: Analyze actual experimental data with the smallest statistical model needed to answer the estimand, respect the independent unit, quantify uncertainty, and bound the paper claim without mechanical significance testing.
---

# Statistical Analysis

## Purpose

Analyze collected data to answer a defined estimand, not to manufacture significance.

## Required Evidence

[Paper Skill Core](../../PAPER_SKILL_CORE.md), actual data and protocol, independent
unit, pairing/clustering, missingness, outcome and comparison. Do not infer them
from filenames or desired conclusions.

## Workflow

1. Inspect observed counts, distributions and relevant quality issues.
2. Choose the simplest model matching the design: description, paired or
   independent comparison, regression or hierarchical analysis as required.
3. Inspect assumptions that could invalidate the result. Use bootstrap,
   permutation, robust, non-parametric or Bayesian methods only when justified;
   do not switch methods after seeing significance.
4. Compute magnitude and design-appropriate uncertainty. Add multiplicity,
   sensitivity or missing-data analysis only when the actual claim depends on it.
5. Save the requested analysis output and update only stale result references.
   Separate observation, inference, mechanism interpretation and open hypothesis.

## Output

Actual estimates, uncertainty, model rationale, relevant diagnostics and claim
boundary. State supported, weakened, refuted or unresolved without a reporting-style
quota or fabricated numbers.

## Validation

Check the computation and true independent units. Non-significance is not no effect;
significance is not practical importance. Only an actually executed analysis can
supply numerical evidence; a planned script or self-report cannot.
