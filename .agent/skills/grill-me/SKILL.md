---
name: grill-me
description: Explicit-only read-only interview that pressure-tests a research idea, protocol, manuscript architecture, venue decision, or implementation plan one consequential question at a time.
license: MIT
compatibility: PaperTrace direct-capability mode; stateless and read-only.
metadata:
  version: '2.1.0'
  source_repository: https://github.com/mattpocock/skills
  source_commit: 391a2701dd948f94f56a39f7533f8eea9a859c87
  owner: PaperTrace maintainers
  task_type: core
  writes: false
---

# Grill Me

## Purpose

Resolve consequential assumptions through an explicitly requested, read-only
interview. Challenge the proposal, not the person; never implement the resulting plan.

## Required Evidence

The proposal, current user answers and relevant inspected facts. For a scientific
or manuscript decision, read [Paper Skill Core](../../PAPER_SKILL_CORE.md). Do not
require scientific context for an unrelated implementation plan.

## Workflow

1. Choose the highest-impact unresolved decision.
2. Ask one concrete question and explain the main trade-off.
3. After the answer, state its implication; verify an external fact only when it
   changes the decision. Resolve contradictions before moving on.
4. Stop when the position is actionable or the user ends the interview. Do not
   turn an explicit interview into a recurring reviewer loop.

## Output

One question and brief recommendation per turn; a concise decision brief on
completion. The brief records choices and uncertainty, not authorizes actions.

## Validation

Check conclusions against answers and evidence, and preserve unresolved facts.
No file edits, experiments, commits, approvals or submission. Existing MIT
attribution and LICENSE.txt remain applicable.
