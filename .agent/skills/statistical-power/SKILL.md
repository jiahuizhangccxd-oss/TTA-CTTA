---
name: statistical-power
description: Estimate sample size, detectable effect, or simulation power only when a real design decision requires it, using a defensible effect scale and the same model planned for analysis.
---

# Statistical Power

## Purpose

Resolve a real sample-size, power or detectable-effect decision.

## Required Evidence

[Paper Skill Core](../../PAPER_SKILL_CORE.md), independent unit, planned analysis,
meaningful effect scale, uncertainty in that effect and applicable budget/design
constraints.

## Workflow

1. Specify the decision and match the calculation to the actual planned model.
2. Prefer a scientifically meaningful effect or conservative prior/pilot basis;
   label conventional assumptions explicitly and do not pick optimistic values.
3. Include applicable error criterion, allocation, pairing, clustering, dropout
   and multiplicity. Use closed-form calculation when sufficient, simulation only
   when the design requires it.
4. Examine plausible effect ranges if one estimate misleads. Return the design
   implication; do not calculate observed power to replace analysis of collected data.

## Output

The calculation, assumptions, required units or detectable effect, uncertainty and
design decision. Produce a curve or script only when useful or actually executed.

## Validation

Check unit independence, effect basis and agreement with the planned analysis.
Do not require power for every deterministic or fixed-data comparison. Missing
critical assumptions stay explicit rather than being guessed.
