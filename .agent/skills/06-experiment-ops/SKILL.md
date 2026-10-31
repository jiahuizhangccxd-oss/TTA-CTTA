---
name: 06-experiment-ops
description: Execute one bounded experiment that tests a named claim or competing mechanism, returning actual run outputs, uncertainty, boundary, and interpretation with minimal reproducibility context.
---

# 06 Experiment Operations

## Purpose

Execute a new or approved run and interpret its actual outputs. Analysis-only work
on completed data belongs to `statistical-analysis`.

## Required Evidence

[Paper Skill Core](../../PAPER_SKILL_CORE.md), the authorized protocol, claim,
independent unit, data/split, intervention, competitive baseline, metrics, budget,
stop rule and required local runtime. Missing semantics blocks the affected run,
not independent authorized work. Reuse existing configuration and approvals;
do not require every final-paper experiment before a valid bounded comparison.

## Workflow

1. Inspect inputs and implementation for leakage, unfair information, wrong
   metadata, unapplied configuration, broken metrics or target-test tuning.
   Distinguish prescribed model fitting, reference/threshold calibration,
   hyperparameter selection and final testing. Read their allowed populations and
   budgets from the actual protocol: "no tuning" is not automatically "no fitting",
   and it does not authorize calibration when that decision is genuinely missing.
2. Execute the bounded protocol with its declared resource limits. Reuse approval
   for the same protocol, queue and remaining budget; an approved training request
   need not be reconfirmed before each item. New costs, exhausted/unknown budgets,
   changed scientific assumptions or disallowed data access pause affected work.
   Do not switch data, checkpoint, device or task to make an invalid run appear
   successful. For a batch, use the inspected generic entry point and approved
   config list; distinguish every planned item as completed, failed, invalid or
   not run. Do not hide a failed command behind a successful shell/tee exit or
   overwrite prior outputs on resume. Stop on a shared protocol fault before
   scaling the error. A valid first comparison is not completion of an authorized
   full queue; continue within its scope and limits.
3. Inspect outputs, counts, metrics and assigned/received/used/behaviorally
   effective treatment where relevant. Distinguish invalid execution, ineffective
   assignment and an untested mechanism; preserve non-use outcomes.
4. Quantify design-appropriate uncertainty and compare with declared support,
   rejection and boundary signatures. Do not add a significance-test battery.
   A pilot without enough independent units stays exploratory or inconclusive;
   do not invent uncertainty or demand an unrelated final-study package first.
5. Preserve adverse outcomes and update the justified claim. Save only the result
   and reproducibility details needed to interpret and rerun it. When manuscript
   revision is also requested, pass the measured result and its interpretation
   to the existing writing Skill; a run-ledger update is not that deliverable.
   Optional autoresearch uses the existing ARIS adapter/allowlist, an explicit
   search space, development signal, budget and stop rule. Preserve all attempts;
   held-out final-test feedback does not silently become a tuning objective.

## Output

Actual result artifacts, metrics, uncertainty, treatment/fairness observations,
interpretation and minimal reproducibility information. Report failed runs as
failed; do not relabel scientifically negative completed runs as invalid.

## Validation

Inspect real outputs and one protocol-relevant sanity check. Successful exit or a
configuration flag alone is insufficient. Do not claim a mechanism was verified
because its implementation ran.
