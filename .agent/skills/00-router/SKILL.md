---
name: 00-router
description: Route a non-trivial PaperTrace request to one internal skill that changes the requested manuscript, code, experiment, figure, submission file, or research decision directly.
---

# 00 Router

## Purpose

Select and execute the smallest action that changes the requested product or
resolves its missing evidence. Routing is internal, not the deliverable.

## Required Evidence

The user request, applicable local instructions, actual target files and available
tools. Read paper state only when source, scope or approval depends on it. Use
[Paper Skill Core](../../PAPER_SKILL_CORE.md) for paper tasks, not routine Git or
unrelated code operations.

## Workflow

1. Inspect the target and identify the actual missing evidence or behavior.
   Before first product-changing work, follow [first-use project alignment](../../../paper/core/01_PROJECT_RULES.md#first-use-project-alignment):
   inspect read-only, propose the project-specific contract and obtain explicit
   confirmation before instruction writes or dependent development. A bundled
   template is not confirmation. Reuse an existing confirmed scope; a read-only
   request proceeds read-only without forcing initialization.
   Once alignment and task authorization both exist, continue the original task.
   Do not stop at AGENTS creation or repeat the same interview. An approval limited
   to instructions does not authorize another product or a training run.
2. Select one primary from `../ROUTING_MATRIX.md`; read its full contract. Add one
   supporting capability only when it performs a needed action.
   When the user names an external/project Skill or a concrete capability is
   missing, use [task-specific selection](../../references/task_specific_skill_selection.md).
   Inspect the actual source and runtime; a repository link is not an installed
   capability. Keep the primary's task and the consuming project's constraints.
3. `@初始化入口` selects `scientific-brainstorming`; an unsupported direction
   remains unselected. Explicit anti-defensive revision selects
   `10-language-polish` with `anti-defensive-writing` support. Unsupported claims
   need `05-claim-evidence`; incomplete scientific argument needs `08-markdown-draft`.
4. Act on the named product unless the request is plan-only or review-only.
   Do not replace an explicit task with a broader audit or full research cycle.
5. Perform the selected Skill's direct validation. Continue the remaining approved
   deliverable when this was only one step; do not expand into unrelated work.
   If an input or tool is unavailable, name the affected action without simulating
   its execution, and complete independently authorized parts that remain useful.

## Output

The actual product or requested decision, its relevant validation and one material
blocker when present. Return revised prose directly for ordinary polish; do not
force routing labels or a whole-paper report into every response.

## Validation

Check that the action, changed files and output match the requested scope and the
selected Skill. Definition checks verify routing metadata only; actual tool and
artifact observations are needed to claim Host behavior.
