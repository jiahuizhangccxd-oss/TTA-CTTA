---
name: 15-figure-table-design
description: Plan, generate, revise, or explicitly audit one scientific figure or table, including requested Nature-style figures, by fixing the reader question, data comparison, message, and interpretation boundary before styling.
---

# 15 Figure and Table Design

## Purpose

Produce a figure/table and caption that answer a scientific reader question.

## Required Evidence

[Paper Skill Core](../../PAPER_SKILL_CORE.md), the source data or defined mechanism,
comparison, units, uncertainty, requested format and interpretation boundary.

## Workflow

1. State one evidence-supported message and choose the simplest honest encoding.
   When `nature-figure` is requested or a concrete panel/export problem needs
   its expertise, select the relevant support through
   [task-specific selection](../../references/task_specific_skill_selection.md).
   Reuse the project's source and plotting backend. Read-only figure review needs
   neither a backend choice nor permission to redraw.
2. For creation or revision, change the actual editable asset and self-contained
   caption. For explicit audit, inspect the supplied asset and report located
   findings without redrawing it or changing its source.
3. Keep schematic illustration distinct from quantitative evidence and preserve
   uncertainty, negative results and domain-specific meaning.
   If GPT Image is requested, use it for a motivation/framework composition draft
   only when available; verify its topology against the actual method before
   rebuilding precise editable objects. Quantitative results come from real data
   and plotting code. The available scientific-visualization support includes a
   Nature style preset; a preset does not establish current journal compliance.
   Visio/Illustrator requests require actual format and editability checks; an SVG
   export or embedded bitmap alone is not proof of native-object round-trip use.
4. For planning-only work, specify panels and missing data instead of fabricating
   results. Do not add panels or export formats merely for completeness.

## Output

The requested asset/caption, bounded plan or explicit-review findings. A manifest
row is not a generated figure.

## Validation

Open the asset and check values, labels, units, legend, readability and claim
strength. Correct data/message errors before styling. A visual cluster or
attribution pattern does not by itself establish a mechanism or causal effect.
For multi-panel figures, inspect panel roles, shared scales, final-size alignment
and collisions as relevant. If using an upstream QA script, inspect its actual
dependencies, execute it on the delivered artifact and resolve material findings;
reading its guidance or passing a style preset does not mean the check ran.
