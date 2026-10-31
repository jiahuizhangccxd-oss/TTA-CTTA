---
name: repository-self-evolution
description: Adopt one verified upstream improvement only when it makes PaperTrace easier to use or materially improves research, code, experiment, or figure work; avoid new process layers and speculative hardening.
---

# Repository Self Evolution

## Purpose

Make a verified, useful capability change or synchronize its actual consumers.
This is execution-layer maintenance, not a scientific claim or paper revision.

## Required Evidence

Current branches/dev, relevant PRs, exact instructions and Git history proving
usage; canonical files and repository-local deltas; actual checks and permissions.
A repository name or old copied template alone does not establish current use.

## Workflow

1. Inspect before editing. Classify instructions as canonical, local extension,
   duplicate or obsolete, including changes on active integration branches.
2. Change a Skill only if inspection, action, output or validation improves.
   Reuse existing paths and avoid model-version-specific prompting recipes.
3. Discover consumers from references, copies, wrappers, local variants and
   history. Record repository, usage, local delta and action in the PR/report,
   not a new registry. Do not reinstall deliberately removed dependencies.
4. Update references only for direct consumers; sync proven unmodified copies;
   preserve scientific extensions in local variants; remove only proven obsolete
   duplication. Do not replace local data, metrics, source authority or approvals.
   Lack of a current caller, template TODOs, file age or context length is not
   proof of obsolescence. Separate optional reusable assets from mandatory task
   records. Preserve templates, styles, examples, original notes and unique
   scientific guidance; reduce default loading instead of deleting them.
   Before proposing their deletion or lossy replacement, inspect full content,
   dependencies and history, identify any retained equivalent, and obtain the
   author's explicit approval for the named assets. General cleanup permission
   is not permission to discard them. Preserve uncertain cases unchanged.
5. Use a feature branch and PR into dev. Create absent dev from the inspected
   default branch; do not modify main/master or indiscriminately merge history.
6. Review the diff, validate affected behavior and constraints, and merge only
   after all scoped checks pass without blocking conflicts. Otherwise leave the
   change unmerged and state BLOCKED, reason and minimum next action.

## Output

Actual capability/sync changes and a repository table covering validation, dev
status and blockers. Separate discovery from completed synchronization; an
incomplete search cannot establish that all consumers were found.

## Validation

Check changed paths/references, unique instruction ownership and preserved local
deltas. Exercise a representative inspect-act-artifact-validate task when tools
permit and report its exact coverage; static checks are not Host execution.
For a restore, distinguish unchanged historical originals from necessary
compatibility edits and verify the actual template or asset can be used. Review
all deletions explicitly; net line reduction is not evidence of improvement.
Use existing tests, not new dashboards, schemas, manifests or sync frameworks.
