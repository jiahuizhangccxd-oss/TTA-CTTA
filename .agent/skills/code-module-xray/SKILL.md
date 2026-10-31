---
name: code-module-xray
description: Explain one existing code subsystem accurately enough to support a concrete implementation, debugging, experiment, or manuscript decision; route requested code changes to code-change.
---

# Code Module X-ray

## Purpose

Explain one subsystem sufficiently for the requested decision; do not refactor it.

## Required Evidence

The decision, public entry, relevant caller/configuration and closest test. Runtime
intent not established by inspected code remains unknown.

## Workflow

1. Trace one representative input-output path.
2. Explain role, shapes/units, assumptions, scientific versus engineering
   parameters, side effects and relevant failure behavior.
3. Identify the smallest check resolving any consequential runtime uncertainty.
4. Update an existing module map only when requested or genuinely reusable.
   Implementation requests route to code-change, not another explanation pass.

## Output

A bounded explanation of behavior, conditions, uncertainties and the decision it
enables. No whole-repository tour or generated architecture inventory.

## Validation

Use direct source inspection or one relevant import/test/dry run. Distinguish
verified execution from inferred behavior; do not run a full project validator
for an unrelated local explanation.
