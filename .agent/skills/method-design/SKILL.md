---
name: method-design
description: Design the smallest method needed to reduce a key scientific uncertainty, starting from an observed failure and competing explanations and ending in a falsifiable comparison, boundary, and implementable specification.
---

# Method Design

## Purpose

Design the minimum method needed by the question, not a complete architecture
for its own sake.

## Required Evidence

[Paper Skill Core](../../PAPER_SKILL_CORE.md), the observed failure or unresolved
contradiction, competing explanations, closest alternative and local method/data
constraints.

## Workflow

1. Identify the smallest intervention and changed scientific object.
2. State definitions, assumptions, operation, expected/rejection signature and
   failure boundary. Separate general principle from implementation and config.
3. Seek counterexamples and remove assumptions unused by the reasoning. Retain
   formal theory only when its proof and scientific role are substantive.
   Fulfil existing proof obligations or explicitly narrow the affected claim;
   numerical checks and simulation do not establish a general theorem. Keep
   analytical proof, implementation agreement and empirical evidence separate.
4. Retain components only with a distinct role, simpler alternative and a
   meaningful deletion/replacement comparison. Do not convert software structure
   into a contribution.
5. Define fair information/budget access, metrics and possible outcomes needed by
   the claimed properties. Avoid tests that cannot change the method decision.
   For simulation proof of concept, specify the physical/task-generating mechanism,
   parameter basis, known truth, controlled variables, negative controls and model
   mismatch needed to distinguish explanations. Do not tune the generator to favor
   the proposed method; simulation support alone does not establish real-data transfer.
6. Write the existing local specification; use 03_METHOD.md only where that
   is the project's established representation. Do not add code or runs unless
   the request includes them.

## Output

An implementable scientific specification, minimal assumptions, comparison and
boundary. No mandatory schema, promotion labels or empty formalism.

## Validation

Check consistency of problem, mechanism, intervention, assumptions, implementation
meaning and decisive evidence. The simpler scientifically equivalent method wins;
a filled specification is not empirical support.
