---
name: experimental-design
description: Design the smallest fair experiment that reduces a named scientific uncertainty by fixing the estimand, independent unit, competing explanation, information access, outcome meanings, and stopping rule before the run.
---

# Experimental Design

## Purpose

Specify the smallest experiment whose outcomes can change the claim or method.

## Required Evidence

[Paper Skill Core](../../PAPER_SKILL_CORE.md), the claim, strongest alternative,
local data/protocol, available independent units, baseline implementation and
resource limits.

## Workflow

1. State required evidence and the decision under each possible outcome.
2. Define estimand, true independent unit and the confound that could mimic the
   effect. Windows, folds and seeds do not automatically add independent units.
3. Select only informative baselines, including the closest or simplest valid
   alternative. Establish correct implementation and reasonable tuning, not just
   equal but inadequate budgets.
4. Declare intervention/control, fixed variables, data/metadata/pretraining/target
   access, tuning/compute budget, metric, uncertainty and stopping rule. Disclose
   unavoidable asymmetries instead of claiming unconditional superiority.
5. Specify a bounded treatment-validity check where relevant. Mechanism and
   boundary measurements are required only for those claims. Use pairing,
   randomization, blocking, power or sensitivity calculations only when justified.
6. Produce the actual protocol/config/layout required by the request. Keep
   design separate from execution and observed results.
   For a staged empirical study, ground the blueprint in original nearest-work
   protocols, including PDF pages and original figure/table references. When at
   least two datasets are requested, verify independent origins or populations;
   two splits or renamed versions of one source do not meet that requirement.
   Split at the machine, subject or recording level before forming correlated
   windows when that is the independent unit.
7. When a results blueprint is requested, give complete table rows/columns and
   figure panels, axes, comparisons, captions and uncertainty fields. Unrun values
   remain `TBD`; state both supporting and falsifying patterns without invented
   ranks or significance. Complete the reviewable protocol, figure blueprint and
   budget before asking for any required author decision. Reuse approval already
   given for the same scope; a design-only request does not authorize batch runs.

## Output

A fair, executable protocol with outcome interpretations, rejection conditions
and necessary boundaries. Do not fill a model-by-dataset-by-seed grid or create
multiple logs for completeness.

## Validation

Check independent-unit and information-access semantics, baseline competitiveness,
treatment observability and whether each condition changes a scientific judgment.
Undefined semantics is an explicit blocker, not an invitation to guess.
