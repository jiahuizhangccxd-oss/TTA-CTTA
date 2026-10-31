# 01｜项目执行约定

Read [README.md](../../README.md) before acting. It defines the task boundary, the
academic-writing entry point and the author-maintained README boundary. After the
current one-time authorized update, treat README as read-only: propose a patch for
the author to review and apply. Modify README directly only if the author explicitly
overrides that maintenance rule and requests a direct README edit.

PaperTrace provides `00-router` as its normal entry and `grill-me` as an explicit,
read-only interview. Other Skills and optional ARIS capabilities remain internal.

## Core-document editing and human confirmation

All author-facing core documents live in `paper/core/00_*.md` through `08_*.md`.
The root AGENTS.md is only a discovery entry; the execution rules have one owner here.
Authors may edit these documents directly. Before any AI write to a core document,
show the concrete file, rationale and minimal diff; obtain confirmation for that
change, or reuse an existing confirmation covering the exact content and scope.
Do not treat template presence, silence, a check passing or an AI-authored approval
field as consent. Do not create an unapproved draft/backup in core as a workaround.
Batch related diffs into one review instead of asking for every line. Re-read before
writing; changed scientific scope or a conflicting author edit requires a revised diff.

This protects core definitions, not every operation in the repository. Continue
independently authorized code, experiment and manuscript work while a core-document
proposal awaits confirmation. Return real outputs and proposed progress text without
silently updating core. Do not invent a new approval registry or block the original
task solely because a progress summary is awaiting approval. An accepted result is
not automatically a confirmed change to protocol, budget, direction or claim strength.

## First-use project alignment

Before the first product-changing work (code, experiment or manuscript) in a
consuming project, inspect its actual files and applicable instructions read-only,
then agree the project-specific working
contract with the user. Follow this section even when a request bypasses the
router. Installing Core or finding a template AGENTS.md is not user confirmation.
An existing, explicitly confirmed contract for the same project and scope is
reused; ask only about a material change or a real unresolved gap.

For a new PaperTrace workspace, author edits belong in this numbered document;
keep root AGENTS.md as the discovery pointer. For an existing downstream project,
retain its established instruction location instead of imposing an automatic migration.

- Identify the target repository/root, existing instruction filename and scope,
  main products, current architecture, protected files and validation commands.
  Reuse the project's convention (normally AGENTS.md); do not create a competing
  agent.md, replace local rules with this template, or infer permission from a
  missing file. Existing instructions remain effective during alignment.
- Summarize the goal, bounded work, editable/protected paths, development approach
  and relevant validation using known facts. Ask only questions whose answers
  change that proposal; unknown scientific or resource decisions remain unknown.
  Do not require an intake form, a fixed interview or a new registry.
- For code projects, inspect existing implementation and framework conventions
  first. Propose the smallest cohesive change, reuse before adding abstractions,
  and avoid unrelated restructuring. For PyTorch or similar projects, discuss
  the applicable model/data/training/evaluation responsibilities and interfaces,
  tensor shapes, device/dtype, split and leakage boundaries, randomness and
  checkpoint compatibility. Include only contracts relevant to the actual task;
  do not invent modules or impose PyTorch on non-code projects. Distinguish
  software tests from real experiments, and agree necessary runtime, dependency
  and compute constraints without treating alignment as permission to install
  packages, start training, spend money or publish results.
- Present the exact target instruction path and proposed content in conversation;
  for an existing file show a minimal diff that preserves unrelated rules. Ask
  the user to explicitly confirm this proposal before creating or changing the
  project instruction file or performing dependent initialization or product work.
  A general request to begin, silence, installation success, file existence or
  agreement to discuss is not approval of an unseen proposal. Reuse an explicit
  approval already given for that exact proposal; do not ask a second time.
- Until confirmation, do not write the target file, a draft/backup beside it or
  other initialization artifacts. Rejection, cancellation, unavailable interaction
  or non-interactive execution leaves project instructions unchanged. Continue
  independently authorized read-only help; read-only reviews and plans never
  require writing AGENTS.md first. If alignment is declined, pause only work
  that depends on it, report the missing decision and do not keep prompting.
- After confirmation, re-read the target to ensure the approved diff still applies,
  write only that change and inspect the resulting diff. A conflicting edit or
  changed scope needs an updated proposal, not an overwrite. Existing confirmed
  content makes repeated entry a no-op; no second approval log or completion flag
  is needed. Subsequent work follows the agreed scope and current authorization.

Confirmation of instructions and authorization of a concrete task are separate.
When both already cover the original requested work, continue that work after
alignment; initialization alone is not its completion. An instruction-only
approval remains instruction-only. Do not repeat a confirmed interview or infer
permission to train, publish or spend from an AGENTS edit.

## Execution layer

Inspect available context -> identify missing evidence -> act -> validate.
Respect the requested product and scope. A plan or report is completion only when
that is the requested product; otherwise change the actual code, analysis, figure,
manuscript or submission files. Do not run an action whose possible outcomes cannot
change the decision or requested product.

Within the confirmed project scope, explain and perform reversible implementation
work without another approval round. Risk is determined by scientific semantics,
resource use and external effects, not by the number of changed files. A request
to plan then execute is not plan-only: finish the bounded plan and execute its
already authorized parts. A smallest coherent step is an execution unit, not a
reason to abandon the rest of the requested deliverable.

Reuse existing authorization for the same operation, protocol, resource budget and
scope. Ask only for a decision that actually changes them or resolves a necessary
unknown. Keep a substantial proposal to goal, observed cause, scope, action,
acceptance and rollback, using existing task context rather than a new registry.
Do not invent prerequisites, reviewer rounds or document quotas. Stop repeating
checks when there is no relevant change or decision-changing information.

Classify the task before acting:

- Code-only work changes implementation, tests or necessary technical documentation.
  Preserve scientific semantics, but do not force manuscript-style prose rules onto
  source code or implementation notes.
- Experimental work produces or interprets actual measurements. Keep implemented,
  executed, verified and scientifically supported distinct.
- Paper work follows Paper Skill Core and the consuming repository's scientific
  authority. Repository operations and Agent work logs do not become manuscript prose.
- Review-only or plan-only requests remain read-only unless the user explicitly
  authorizes edits.

For mixed tasks, complete the necessary implementation or experiment first, then
change manuscript claims only to the extent supported by the resulting evidence.

Read the selected SKILL.md in full and only the relevant supporting references.
Use one primary Skill and, when needed, one supporting capability. Reuse before
refactoring; refactor before rewriting. Do not add role-play, thinking incantations,
repeated context, reviewer loops or an alternate workflow controller.

Use the tools actually available. Check installed APIs or current official
documentation for version-sensitive behavior; do not bind these rules to a model
version. Missing access, tools or runtime is reported, not replaced by an
unrequested backend or a claim that an action ran.

## Paper layer

Before any academic drafting, revision, translation, caption writing, experimental
interpretation or review, read [Paper Skill Core](../../.agent/PAPER_SKILL_CORE.md), even
for a direct request without an explicit Skill or language-polish instruction.
Paper-related Skills must reference it; it owns shared evidence, scientific
abstraction, manuscript language and final reviewer QA rules. The selected Skill
owns its local evidence requirements, action, product and direct validation.

Keep one scientific main line, consistent terminology, precise descriptions and
explicit logic; conclusions must not exceed evidence. Remove empty defensive or
Agent-process prose, not real uncertainty, negative results or necessary limits.

[The research loop](../../.agent/references/research_first_paper_loop.md) provides
on-demand scientific reasoning, experiment and whole-paper status guidance, not
another controller. Its examples do not override Paper Skill Core or create
mandatory stages, reviewer repetitions or document quotas.

Read `paper/core/02_RESEARCH.md` only when the task depends on research state, active source
or an author decision. It remains PaperTrace's current-state authority; intake is
one-time input and the two existing logs are history, not synchronized state.
Respect an explicitly different downstream authority. Do not import a downstream
paper's scientific facts, constraints or decisions into the template.

## Implementation and safety

Preserve data, label, split, transform, objective, metric, units, checkpoint and
protocol semantics. On inconsistency, stop the affected operation and dependent
inferences, not every independent task. Repair an identified implementation error
within the approved scientific contract and verify it; a repair requiring a new
scientific definition needs the author's decision. Never silently substitute
another data source, protocol or scientific problem to obtain a successful run.

Identify a blocker by its actual source: platform/access, missing scientific
input, implementation failure or an applicable instruction. State the affected
action and the minimum missing decision once. Continue independently authorized,
useful work; do not manufacture busywork or rerun a known blocked action. An
unavailable full experiment cannot be relabelled as a completed smoke test, and
an unavailable host cannot be replaced by invented execution records.

Add abstractions only for real current needs and when a direct implementation is
insufficient. Handle observed failures, common user mistakes and high-impact data,
cost or publication risks; do not build infrastructure around hypothetical cases.
Comments explain assumptions, units, shapes and non-obvious choices, not the code
in other words.

Use Python for computation, data, models, statistics, figures, necessary artifacts
and relevant tests. Do not use it for prose scores, ordinary Markdown scanning,
wrapping Git, status-report generation or silent input repair. Do not create custom
hashes, digests, receipts, ledgers or integrity chains. Native Git history and
understandable commands/results are sufficient; preserve valid existing evidence.

Routine local reads, reversible edits and tests need no safety detour. Use the
current explicit authorization for the same action and scope. Obtain authorization
for unapproved paid compute, sensitive-data egress, destructive writes, publication
or submission. Never expose secrets or fabricate evidence.

## Git and synchronization

Before editing, inspect the target branch, working changes, relevant open PRs and
applicable local instructions. Classify source content as canonical, local
extension, duplicate or obsolete using actual files and history, not repo names.

For modernization/sync, branch from `dev`; create `dev` from the inspected default
branch only when it is absent. Do not write `main/master`, force-push, reset local
work, delete unrelated branches or bypass a failed gate. Preserve effective pending
changes and local scientific extensions. Update direct references, replace proven
unmodified copies, and edit local variants surgically. Do not reinstall a framework
that a repository deliberately removed. The repository-self-evolution Skill owns
the bounded sync procedure; no global sync registry or new state machine is needed.

Merge a PR into `dev` only after diff review, relevant validation, preserved local
constraints and no blocking conflict. Otherwise report BLOCKED, its reason and the
minimum next action. A merge is not scientific evidence.

## Validation and completion

Inspect actual outputs, not only exit codes or self-reported completion. Run the
closest test, source check, numerical check, asset inspection or compile; do not
repeat it without a relevant change. Run the existing full suite once for final PR
review using the commands in README.md. Case-definition validation is not Host
execution or proof of scientific correctness.

Use one final focused reviewer QA for substantial paper revisions. Separate
read-only independent review from revision, and do not start another reviewer loop.
Keep execution details in the development response, not manuscript prose. Report
the actual change, direct validation and material remaining blocker. Whole-paper
status summaries are on demand, not mandatory for a paragraph edit or code fix.
For research-progress requests, distinguish the actual product change, its direct
verification, its effect on the research question and what remains untested. A
valid negative result or eliminated explanation can advance research; test counts,
plans and PRs alone cannot establish that a paper's hypothesis is supported.

ARIS stays optional and behind the existing adapter/allowlist. Do not run its
installer or expose its Skills directly. Core remains usable without it.
