---
name: code-change
description: Implement, repair, refactor, or optimize one bounded code behavior while preserving the stated scientific problem, using fail-fast semantics and the closest relevant test.
---

# Code Change

## Purpose

Change the requested executable behavior. Explanations or module maps are not a
substitute for source modification.

## Required Evidence

The expected/observed behavior, applicable local instructions, target source,
callers, relevant configuration and closest test. Inspect scientific contracts
only where the patch affects them. Reuse the confirmed development scope and
actual runtime; do not reinstall dependencies or reopen alignment for a routine
repair that preserves the contract.

## Workflow

1. Reproduce the defect or establish the smallest real baseline.
2. Trace the relevant input-output path and verify affected shapes, units,
   data/split, objective, metric or configuration semantics.
   For a PyTorch task, inspect only affected contracts: tensor dimension meaning,
   dtype/device, labels/loss, gradient flow, train/eval state and checkpoint keys.
   `eval()` and gradient disabling solve different problems; inference mode does
   not itself set evaluation mode. Preserve the project's trainer and framework.
   For signal/data changes, also inspect sampling rate, physical units, window
   grouping and the allowed population for fitted normalization/calibration.
   Do not require these checks for pure prose or unrelated code work.
3. Apply the smallest coherent patch, reusing existing functions and interfaces.
   Do not introduce a wrapper chain or substitute a scientific input on failure.
   For a multi-experiment runner, keep scientific operations generic and express
   experimental variants in config/YAML. A requested shell script lists those
   configurations and calls the verified existing CLI; do not dispatch on E1/E2/E3
   labels inside Python. Check argument quoting, failure propagation and a real
   small end-to-end path before describing the full run as executable.
4. Add a regression for the observed/common/high-impact defect when needed.
5. Run the closest test and inspect output and diff. Comments explain non-obvious
   assumptions and decisions, not a development diary. A small forward/backward
   check tests implementation, not diagnosis accuracy or a mechanism. Missing GPU
   access limits that validation; do not silently change an experimental device.

## Output

Changed source, observed before/after behavior, actual validation and any material
remaining blocker. Preserve unrelated local changes and scientific behavior.

## Validation

Check the requested behavior and relevant numerical/interface invariants. Keep
failed executions visible. Run the full suite only at final PR review; no custom
integrity records, prose metrics or tests for hypothetical combinations.
