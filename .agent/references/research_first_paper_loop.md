# Research-First Paper Loop

This is the default reasoning contract for PaperTrace research, code, experiment,
figure, manuscript, review, and revision work. It combines the Research-First
Agent and Adaptive Research Paper Agent principles without turning them into a
fixed stage pipeline. Load only the section needed by the current task.

For an explicitly requested staged study, the
[standalone prompts](../../paper/prompts/README.md) provide copyable tasks with
existing Skill ownership. They are an on-demand research path, not a second router
or mandatory sequence for unrelated work.

## Highest authority

At every iteration:

1. state the strongest current claim that matters to the paper;
2. identify the largest unresolved uncertainty that threatens it;
3. list the strongest competing explanations;
4. choose the smallest coherent action that most directly distinguishes them;
5. define before execution what each plausible outcome would mean;
6. obtain real evidence through literature, theory, code, experiment, statistics,
   figure inspection, or manuscript revision;
7. update the claim, mechanism, boundary, novelty judgment, or next decision;
8. stop when the action no longer has material scientific value.

Do not continue merely because a workflow has a next stage.

Before acting, answer:

```text
Q1. What is the key uncertainty blocking the research decision?
Q2. What is the smallest action that directly reduces it?
Q3. Could any plausible outcome change the scientific judgment or next action?
```

If Q3 is no, do not perform the action.

A useful decision heuristic is:

$$
a^* = \arg\max_{a\in\mathcal A}
\frac{\mathbb E[\Delta U_{\mathrm{sci}}(a)]}{C(a)},
$$

where $\Delta U_{\mathrm{sci}}$ is the expected reduction in the current key
scientific uncertainty and $C(a)$ is time, compute, code, and cognitive cost. The
formula guides judgment; it does not create a scoring bureaucracy.

## Adaptive research state

Maintain only the state needed to choose the next action:

```text
Central question:
Current claim:
Evidence supporting it:
Strongest competing explanation:
Largest unresolved uncertainty:
Current novelty risk:
Most informative next action:
Stopping condition:
```

Do not write an Introduction merely because the state is incomplete. Return to the
smallest relevant literature, theory, code, experiment, or analysis action.

## Paper optimization and scientific status

For a whole-paper optimization request, understand the paper before editing it.
Read the selected Skill in full, then inspect the relevant current brief,
STATUS/GOAL if present, manuscript, closest prior work, theory, implementation,
configs, results, figures, and reviewer comments. Check branch and active PR when
repository edits are involved. These are sources to consult as needed, not a
requirement to scan every directory or load every previous prompt.

Establish the scientific question as a testable question, not “propose method X.”
For empirical method work, trace:

```text
Scientific question -> Testable claim -> Prior work / Gap
-> Theory or mechanism -> Method -> Strong baseline
-> Controlled experiment -> Evidence -> Conclusion
```

Use the links appropriate to the actual contribution; a theoretical or resource
paper must not acquire invented experiments or a mechanistic story to fill this
chain. For every core claim identify required evidence, existing evidence, and the
remaining gap. The current Abstract and Contributions are claims to check, not
proof that the work is novel or complete.

### Evidence-based stage reporting

Use the supplied S0–S7 vocabulary to describe scientific maturity when useful:

| Stage | Meaning | Evidence to inspect |
|---|---|---|
| S0 | Idea | An open direction; unresolved assumptions remain explicit. |
| S1 | Problem formulation | A defined question, scope, and testable claims. |
| S2 | Method implemented | Inspectable implementation of the stated method; code existence is not a result. |
| S3 | Baseline established | Correct, reasonably tuned baselines under the declared comparison protocol. |
| S4 | Core experiment completed | Actual outputs from a valid core comparison, including null or negative outcomes. |
| S5 | Claims experimentally supported | Claim-specific experimental support within the evaluated scope. |
| S6 | Full manuscript | A coherent manuscript whose statements agree with its evidence. |
| S7 | Submission-ready | The applicable scientific, reproducibility, manuscript, and submission blockers are resolved. |

These are descriptive labels, not required sequential gates or a new enum for
`02_RESEARCH.md.paper_stage`. Identify mixed maturity and inapplicable stages rather
than assigning a misleading percentage. A complete draft can coexist with an
untested core claim; S4 does not imply S5. Preserve the project's existing source
and publication-stage semantics.

Keep execution and evidential states separate:

```text
planned      an action is specified
implemented  code or a method exists
executed     it actually ran; report success, failure, or invalidity separately
verified     the relevant output/protocol/property was directly checked
supported    the evidence justifies the particular scientific claim
```

None of these labels automatically implies the next. A verified script is not a
verified mechanism, and a completed invalid comparison does not support a claim.

### STATUS without duplicate authority

Update an existing `STATUS.md` when the task calls for scientific-status work. If
none exists and a persistent summary is requested or useful for the current
whole-paper task, `paper/core/07_PROGRESS.md` may be created. Do not pre-create an empty
STATUS template or require one for ordinary work.

In PaperTrace, `paper/core/02_RESEARCH.md` remains the current-state authority; STATUS is a
human-readable evidence summary, not a second source of author decisions, active
source, or publication stage. Reuse the existing evidence matrix and actual result
paths rather than copying full records. Where a downstream project explicitly
uses STATUS as its authority, respect that choice instead of imposing another
independently maintained state file. Do not silently migrate project state.

The supplied [progress page](../../paper/core/07_PROGRESS.md) records the template's actual
uninitialized research condition. When adapting it to a paper, replace only the
relevant observations after inspecting project evidence; a copied template is not
completed research. During authorized staged work, refresh the affected summary
after a decision-changing result or completed milestone, not after every prose edit.
Date the observation and link existing evidence. Read-only requests remain read-only.
Shared submodule copies provide prompts/templates; each paper maintains its own
progress in its project, respecting any established downstream authority.

A requested summary must make these matters recoverable:

```text
Scientific question; core claims; novelty boundary; theory status;
implementation status; baseline status; experimental evidence;
unsupported claims; current blockers; next highest-value action.
```

For each relevant claim use a compact table:

| Claim | Evidence/source | Status | Risk or remaining gap | Next discriminating test |
|---|---|---|---|---|

The reporting labels are `SUPPORTED`, `PARTIALLY SUPPORTED`, `UNTESTED`, and
`CONTRADICTED`. They do not replace hypothesis provenance or existing record
formats. Missing or invalid evidence is not automatically contradictory evidence;
identify the reason. Preserve negative findings and do not mark a claim complete
merely because its code is implemented.

When the requested pipeline uses Supported / Refuted / Inconclusive, report a
supported claim with its scope, map effective counterevidence to Refuted, and state
why untested or insufficient evidence is Inconclusive. Partial support leaves the
broader claim unresolved; do not silently change existing evidence-record enums.

### Execute the blocker; report the scientific change

Within the requested scope, prioritize a critical scientific blocker, missing
evidence, an unfair comparison, or missing implementation before manuscript
consistency and cosmetic refinement. Complete the smallest action that can change
one judgment. Do not repeatedly ask permission for routine local work, but retain
explicit approval boundaries for costly, destructive, private-data, or external
actions. When tools, data, or runtime are unavailable, state exactly what was and
was not executed.

After a substantial revision, pressure-test the actual changes for closest-prior
misrepresentation, unnecessary complexity, weak baselines, unfair comparison,
unsupported mechanism/causal claims, unrealistic assumptions, simpler competing
explanations, cross-section contradictions, and reproducibility gaps. This is a
focused self-check, not an automatically commissioned independent review or a
reviewer-count requirement. Repair substantive rejection risks without defensive
writing.

For whole-paper optimization or an explicit status review, return:

```text
Scientific status: stage, question, contribution, strongest evidence, largest risk
What changed: the substantive change to the research decision or direct product
Claim–Evidence table: only the claims relevant to this task
Critical reviewer risks: evidence-based rejection risks, not hypothetical objections
Next action: at most three priorities; action -> judgment resolved -> product -> pass/fail
```

Do not invent three actions when only one matters. Plans, prompts, TODOs, empty
scripts, unrun configs, citation counts, polished figures, commits, and PR counts
are not scientific evidence. Distinguish implementation or writing progress from
a newly verified claim, stronger evidence, a resolved contradiction, an established
strong baseline, a clarified novelty boundary, or a removed submission blocker.
A requested status report is a valid product; it does not substitute for executing
the blocker when optimization, rather than status-only work, was requested.

## Non-negotiable rules

1. Evidence before narrative.
2. Problem before method.
3. Failure before novelty.
4. Mechanism before module.
5. Theory must constrain, predict, explain, or delimit.
6. Every major claim needs theoretical, experimental, or verified-literature
   support.
7. Negative, null, unstable, and contradictory results remain evidence.
8. Exploratory findings are not confirmatory evidence.
9. Facts, inferences, and hypotheses must remain distinct.
10. Do not fabricate citations, results, statistics, novelty, author decisions, or
    implementation behavior.
11. Scientific semantics precede infrastructure.
12. Do not create rigor theatre through hashes, receipts, ledgers, exhaustive
    validators, reviewer quotas, or CI volume.

## Problem definition

A research question should make the boundary explicit:

```text
Q = (Object, Environment, Observation, Task, Failure, Desired understanding)
```

Ask:

- What object or relation is being studied?
- Under which environments and interventions?
- What is observed and at what independent unit?
- What task or decision is evaluated?
- What failure or unexplained behavior motivates the work?
- What new understanding should survive if the preferred method does not win?

## Scientific semantics and fail-fast

Prioritize the actual computation chain:

```text
data
-> metadata
-> split and protocol
-> transforms
-> objective
-> model inputs/outputs
-> metric
-> result
```

For dataset, label, metadata, sampling rate, window, stride, split, transform,
objective, metric, model, checkpoint, or protocol inconsistencies:

```text
detect semantic inconsistency
-> clear error
-> stop
```

Do not guess, silently repair, infer intent, switch tasks, or fall back to a
different scientific problem. Recover only from operational failures that leave
the experiment meaning unchanged.

## Literature and novelty falsification

The first purpose of literature search is to try to invalidate the novelty claim,
not to collect support for a preferred gap.

Search for:

- foundational and recent representative work;
- the closest direct prior art;
- equivalent, historical, and neighboring-field terminology;
- the same mechanism under another name;
- theoretical equivalents;
- conference, journal, preprint, benchmark, and reproduction versions;
- work reporting the same failure or boundary;
- evidence that directly weakens the proposed novelty.

For load-bearing sources, record only what changes the decision:

```text
Citation and verified source
Research question
Method and core assumption
Main result
Known limitation
Exact overlap with our work
Remaining distinction
Evidence that the distinction matters
```

The output should state:

```text
Strongest prior art against novelty:
Exact overlap:
Difference that remains:
Evidence that the difference matters:
Novelty verdict: invalid / weak / defensible / strong
Required repositioning:
```

Search snippets do not replace original-source verification. A low paper count or
missing exact keyword is not a scientific gap.

## Claim tree and hypothesis provenance

Prefer one central claim and the smallest claim tree needed by the paper:

```text
C1: the baseline exhibits a defined failure.
C2: the failure is associated with mechanism Z.
C3: intervention M changes mechanism Z.
C4: the expected observable behavior changes accordingly.
C5: the advantage weakens when assumption A is broken.
```

Include only claims the paper actually needs. Mark evidence state as:

```text
literature-supported
 theory-supported
 exploratory evidence
 independent confirmation
 post-hoc interpretation
 unsupported
```

For each major hypothesis record provenance:

```text
H0: proposed before observing the relevant result
H1: inspired by exploratory evidence
H2: independently confirmed by new evidence
H3: still a post-hoc interpretation
```

Do not rewrite H1 or H3 as if it had always been H0. Exploratory findings may be
reported honestly; a central claim that depends on them should receive an
independent confirmation test.

## Counterexample-first theory

Theory starts from the real experiment:

```text
E = (D, P, f_theta, L, M)
```

where `D` is data and environments, `P` is protocol/split/transform, `f_theta` is
the model, `L` is the objective, and `M` is the evaluation quantity.

Before strengthening a proposition:

1. actively search for a counterexample;
2. identify the minimum assumption needed to exclude it;
3. remove assumptions not used by the reasoning;
4. check whether the remaining assumptions hold in the experiment;
5. derive an observable prediction and failure condition.

The theory chain must close:

```text
Assumptions -> Claim -> Observable prediction -> Experiment
```

A theoretical contribution should provide a checkable definition, decomposition,
condition, bound, invariant, identifiability result, consistency result, failure
condition, or testable design principle. Otherwise call it analysis,
interpretation, hypothesis, or empirical observation. Do not label intuition as a
theorem.

Check that a theorem states more than its definitions or an algebraic restatement,
that its proof uses the stated assumptions, and that the result applies to the
actual algorithm. Retain theory that constrains, explains, predicts, or delimits
the method; do not add formalism solely to make the manuscript look rigorous.

## Failure-driven method loop

Do not ask what module can be added. Ask what failure must be explained or
changed.

```text
observation
-> competing mechanism hypotheses
-> minimal intervention
-> controlled comparison
-> mechanism check
-> keep, simplify, reject, or revise
```

For each iteration:

```text
Observed failure:
Competing explanations:
Proposed intervention:
Why it targets the mechanism:
Simplest alternative:
Expected signature:
Actual result:
Decision:
```

A component earns its place only when it has one scientific role, a simpler
plausible alternative, a deletion or replacement test, and an observable
signature. If a simpler version performs equivalently, prefer the simpler version
or reduce the contribution claim.

## Claim-driven experiment design

Every experiment must answer one claim or one major uncertainty:

```text
Claim:
Competing explanation:
Required evidence:
Experiment:
Possible outcomes:
Decision under each outcome:
```

Define the experimental unit before statistics:

```text
What is the experimental unit?
Which observations are dependent?
At what level is train/test separation defined?
At what level should uncertainty be estimated?
```

Windows, frames, patches, folds, and repeated measurements are not automatically
independent replicates.

Comparison fairness includes:

```text
Data access
Target information
Metadata access
Pretraining
Search/tuning budget
Compute budget
Evaluation protocol
```

Any asymmetry must be disclosed and cannot support an unconditional superiority
claim.

Use only the baseline set required by the question: naive, canonical, strong
recent, closest prior art, method without the key mechanism, and simplest valid
alternative. Do not add weak baselines merely to fill a table.

### Competitive baselines

Establish how well an ordinary or closest-prior method performs after correct
implementation and reasonable optimization before interpreting proposed-method
gains. Inspect preprocessing, data/split, objective, training/inference protocol,
information access, hyperparameter selection, and the actual tuning budget.
Equal but inadequate budgets do not establish a strong baseline. Use validation
rather than the held-out test for selection; compare with an appropriate
reference or task-specific sanity check where available, and disclose unresolved
reproduction gaps. Do not tune indefinitely or until a preferred method wins.

The comparison should establish an increment over a competitive baseline, not
merely a large gain over a weak one. A baseline is not “established” because a
config or an unexecuted implementation exists.

Ablation should answer whether the mechanism or complexity is necessary. Prefer:

```text
full method
vs key mechanism removed
vs simplest valid alternative
```

### Treatment validity

For agent, retrieval, modular, and other multi-stage experiments, distinguish:

```text
assigned intervention -> received intervention -> used intervention
-> behaviorally effective intervention
```

A configuration flag establishes assignment, not delivery, use, or behavioral
effect. Before interpreting an effect, check that the intended condition was
instantiated, the component was reachable and operational, the groups differed
in the intended factor, and fixed variables remained comparable. Where relevant,
inspect whether the model received and used the supplied information or mechanism.
Use the actual outputs and a bounded direct check, not a new monitoring system.

Separate two sources of misleading results:

| Failure class | Examples | Consequence |
|---|---|---|
| Hard bugs | Wrong data/labels/splits, unapplied config, unexecuted component, incorrect metric/preprocessing, failed invocation. | Repair or report the invalid execution before making the intended scientific comparison. |
| Soft bugs | Reachable but unused mechanism, ineffective instructions, unequal useful information or resources, weak tuning, fallback-dominated behavior, negligible behavioral intervention. | Measure the intended contrast and explain what the observed behavior does and does not test. |

Behavioral effect is not the same as improved task performance. Report non-use,
null effects, and deterioration; do not discard them to retain only successful
interventions. An unused component does not test the benefit of using that
component, but may reveal a failure of the assigned strategy. Distinguish that
finding from a broken implementation and from evidence against the intended
mechanism.

Keep outcome, mechanism, and boundary evidence separate: performance answers
whether an effect exists; mechanism-specific observations or interventions address
why; boundary comparisons address where it disappears or reverses. Do not require
all experiment types when the paper does not make all three kinds of claim.

## Experiment stop rule

Do not run an experiment merely because papers usually contain it. Run it only
when at least one plausible outcome could change:

- claim confidence;
- mechanism discrimination;
- method choice;
- theoretical interpretation;
- applicability boundary;
- novelty judgment;
- a major reviewer-critical conclusion.

If all plausible outcomes leave the research decision unchanged, stop that
experiment.

## Statistics and interpretation

Statistics serve the estimand and independent unit. Use repeated runs,
uncertainty, confidence intervals, effect sizes, paired analysis, bootstrap,
non-parametric methods, multiplicity correction, Bayesian analysis, or power only
when they improve the actual inference.

Do not add a p-value because it looks rigorous. Do not choose the analysis after
seeing which method produces the preferred result.

Interpret results as:

```text
Observation
-> quantitative evidence
-> mechanism interpretation
-> relation to hypothesis
-> remaining uncertainty
```

Always separate:

```text
Fact: directly supported by data.
Inference: derived from facts and assumptions.
Hypothesis: requires new evidence.
```

## Code, abstraction, and validation

Research code must make it easy to answer:

```text
Where did the data come from?
What transformations were applied?
What model and objective ran?
What protocol and split were used?
What result was produced?
```

Before adding a validator, wrapper, fallback, cache, factory, registry, schema,
test, CI rule, or metadata field, ask:

1. Does it solve a real observed/current problem?
2. Could the current scientific conclusion be wrong without it?
3. Is there a simpler direct implementation?

If the first two answers are no, do not add it. If the third is yes, use the
simpler option. Abstract only after at least two real current use cases exist and
only when the abstraction does not hide data flow or mathematical semantics.

Python is for numerical work, data processing, signal processing, simulation,
training, inference, statistics, plotting, necessary file generation, and tests
of scientific semantics. It is not a generic wrapper, text checker, report
generator, silent input repair layer, or hypothetical-validator framework.

Do not proactively create custom hashes, checksums, digests, receipts, ledgers,
or integrity chains. An upstream official checksum may be used only to verify a
real download, or when actual corruption has occurred, or when the user explicitly
requests content verification. Git already records code history.

Keep paper-specific methods, experiments, configs, and analyses separate from
shared data/model/trainer/benchmark infrastructure. Do not silently change a
shared framework or submodule's scientific contract to accommodate one paper.
Keep interfaces and comments clear enough to explain the actual data and objective.

## Paper construction

Systematically organize the paper only after the central question, main claim,
and key evidence are sufficiently stable.

### Argument structure, not a research workflow

Use the smallest complete argument:

```text
scientific question -> proposed answer -> evidence -> bounded conclusion
```

WHY–WHAT–HOW helps explain a problem or method, but does not by itself establish
what was learned. Expand it when the argument needs the missing links:

```text
WHY -> GAP -> WHAT -> HOW -> EVIDENCE -> CLAIM
```

| Part | Reader's question | Required content |
|---|---|---|
| WHY | Why does this question matter? | Concrete phenomenon, need, failure, or scientific uncertainty. |
| GAP | What remains unresolved? | Verified limits of existing knowledge under explicit conditions; not merely an unused module combination. |
| WHAT | What answer or idea is proposed? | Specific question, hypothesis, explanation, method, or mathematical object, as appropriate to the study. |
| HOW | How is the idea made testable? | Mechanism, assumptions, formulation, implementation, and comparison. |
| EVIDENCE | What supports or challenges it? | Actual observations, proofs under stated assumptions, controlled comparisons, or verified literature. |
| CLAIM | What can now be concluded, and why does it matter? | Knowledge gained, scope, remaining alternatives, and scientific or engineering implication. |

This is reader-facing argument order, not the chronology of discovery or a fixed
execution pipeline. Preserve hypothesis provenance. A proposed explanation is not
an established answer, and a failed prediction can still yield useful knowledge.
Do not require a new theorem, mathematical object, mechanistic hypothesis, or
experiment in every paper. Use the evidence appropriate to the contribution.

### Preserve the valid core

Revise only an identified scientific, logical, or evidential weakness. Retain valid
content, make the minimum necessary revision, and check consistency. Do not rename
concepts, invent terminology, restructure sound sections, or expand the study just
to make it appear more complete. Add no defensive prose for hypothetical reviewer
objections; preserve qualifications that resolve a real ambiguity.

Separate the scientific question, contribution, methodological realization, and
implementation. Likewise distinguish the general principle, default implementation,
and experimental configuration. Dataset values, one classifier, or a software
interface belong in the conceptual definition only when essential to the method.
State which choices are essential, optional, or specific to the experiments.

Contributions explain what is learned or made possible: a formulation,
representation, mechanism, learning or identification principle, theoretical
result, empirical phenomenon, boundary, or benchmark/resource contribution. A
feature list, first use of a model, or extensive experiments is not automatically
novel. Tie each contribution to evidence; do not replace a missing contribution
with stronger verbs or remove all substance to declare the paper finished.

### Section-specific logic

Do not repeat all six parts in every section or use WHY/WHAT/HOW as mandatory
manuscript headings. Apply only the structure that serves the section's job.

| Section | Argument order |
|---|---|
| Abstract | Problem and specific gap -> approach and scope -> actual principal finding -> bounded implication. |
| Introduction | Real problem -> existing capability and assumptions -> unresolved failure or contradiction -> scientific question -> key insight -> supported contributions. |
| Related Work | Compare relevant assumptions, mechanisms, information access, results, and limitations -> exact overlap -> meaningful remaining distinction. |
| Method | Local difficulty -> component's scientific role -> inputs, operations, outputs, objective, and essential implementation -> justified property or testable prediction. |
| Theory, when needed | Question -> definitions and assumptions -> statement -> proof -> observable consequence -> counterexample or validity boundary. |
| Experiments | Question and competing explanation -> quantity to estimate -> protocol and fair comparison -> actual result -> conclusion supported. |
| Results | Main observation -> quantitative comparison and uncertainty -> interpretation -> corroborating or conflicting result -> remaining uncertainty. |
| Discussion | Explain or qualify the findings -> consider alternative explanations and prior work -> identify failure conditions and separate method/data/experiment/theory/scope limitations -> implication. |
| Conclusion | Answer the original question with the knowledge actually gained; do not add untested superiority, causality, or universality claims. |

Keep the Abstract a complete scientific argument, not a compressed Method section.
The Introduction narrows from a field-level need to the paper-level question;
where relevant, show how existing research directions leave an unresolved
intersection. Keep detailed datasets, hyperparameters, experiment identifiers, and
numerical comparisons in later sections rather than reproducing the protocol.
Organize Related Work by questions, methodological families, or capabilities:
what is solved -> how -> what remains unresolved -> why the distinction matters.
The gap must emerge from that comparison, not from an unsupported final sentence.

Results and Discussion may be combined when appropriate; do not duplicate the
same table description or explanation merely to fill both sections. Before results
exist, keep missing findings explicit in the working draft, not as invented
numbers or expected outcomes written in the past tense.

### Paragraph and method logic

Give each paragraph one intellectual job. State its point early, provide the
reasoning or source/result that supports it, and explain the consequence when
needed. This is not a fixed sentence count. Preserve unique definitions,
mechanisms, examples, equations, citations, negative findings, and boundaries.

Connect adjacent paragraphs through a previous conclusion, remaining problem,
new concept or evidence, and local consequence where needed. If paragraphs can be
freely swapped without changing the argument, inspect their roles; do not merely
add more “however,” “moreover,” or “therefore.”

For a method component, ask internally:

```text
WHY: Which specific difficulty requires an intervention?
WHAT: What does this component change or preserve?
HOW: What are its inputs, operations, outputs, and mathematical objective?
PROPERTY: What follows by proof, what is intended, and what still needs testing?
```

An equation should define a computation or support an argument. Explain its
symbols, assumptions, and connection to the next operation; do not introduce
symbols simply to restate prose. Methods explain mechanism, not software
architecture. Factories, registries, caches, managers, hashes, manifests, and
logging stay out of the manuscript unless they are the research object.

For example, introducing an alignment loss does not establish that condition
information decreases while fault information is preserved. If that is only the
design intention, say so and identify the comparison that tests it. Do not present
$I(Z;C)\downarrow$ and $I(Z;Y)\uparrow$ as established properties without suitable
assumptions and proof or an appropriate empirical analysis. Accuracy improvement
or a visually separated embedding alone does not establish disentanglement or a
causal mechanism.

### Writing an experiment as an argument

Reuse the existing experiment notes; do not create a second registry or require
new metadata fields. E1, E2, and similar labels are optional reader-facing labels,
not a required experiment count. For each necessary experiment, make these
answers recoverable from the text, table, and caption:

```text
Purpose (WHY): Which question or competing explanation is being tested?
Target (WHAT): Which quantity, population/conditions, and comparison answer it?
Protocol (HOW): What information, split, controls, budget, and analysis are used?
Outcome meaning: What would improvement, no change, or deterioration imply?
Result: What was actually observed, with relevant uncertainty and result source?
Conclusion: What does it support, what remains unresolved, and under which scope?
```

The outcome meanings belong to the prospective design when specified before the
experiment. Do not retroactively label an exploratory analysis as predeclared.
Separate completed findings from planned experiments and post-hoc interpretation.

The estimand is the quantity the study intends to estimate, not merely a metric
name or the number returned by one run. For an illustrative fixed predictor $f$
and a specified held-out-condition distribution $P_{\mathrm u}$, distinguish:

$$
R_{\mathrm u}(f)
= \mathbb E_{(X,Y)\sim P_{\mathrm u}}[\ell(f(X),Y)],
$$

$$
G_{\mathrm{shift}}(f)
= R_{\mathrm u}(f)-R_{\mathrm s}(f),
\qquad
\Delta_{\mathrm u}
= R_{\mathrm u}(f_{\mathrm{base}})-R_{\mathrm u}(f_{\mathrm{new}}).
$$

Here $R_{\mathrm s}$ is risk on a specified held-out seen-condition distribution,
using the same task and loss. $R_{\mathrm u}$ measures unseen-condition predictive
risk; $G_{\mathrm{shift}}$ measures the seen-to-unseen risk difference for the same
predictor; $\Delta_{\mathrm u}$ compares two predictors on the same unseen target
and is positive when the new predictor has lower risk. A sample estimate
$\widehat R$ is not the population quantity $R$.

Do not substitute the shift difference for unseen-condition performance: a small
difference can coexist with poor performance in both settings. It is also not the
usual population-risk minus empirical-training-risk generalization gap. No
subtraction is required unless it answers the research question. Define domain
weighting and averaging over training randomness when relevant, and do not infer
performance on every unseen condition from one held-out suite.

For uncertainty, identify the independent unit and what the variation represents.
Random-seed dispersion does not by itself measure uncertainty across machines or
operating conditions; overlapping windows are not independent replicates. Select
task-relevant metrics rather than requiring Accuracy, F1, and AUROC for every task.
State the aggregation, units, and whether a reported improvement is a percentage
point difference or a relative percentage.

### Generalization and adaptation must remain separate

When the paper concerns unseen conditions, define what was unseen and when.
A source-only generalization experiment keeps the evaluated target conditions
unavailable for fitting, target-specific normalization, model selection, and
checkpoint selection; ordinary inference with a frozen source-fitted predictor
and preprocessing is allowed. Access to unlabeled target data for adaptation,
labeled target data for fine-tuning, or parameter/statistic updates at test time
changes the information-access protocol and must be reported separately.

For example, E1 may test source-only unseen-condition performance, E2 a matched
component deletion or replacement, and E3 a predicted failure boundary. Retain
only the experiments required by the actual claims. A target-adaptation study can
be a separately labeled extension; its results must not be pooled with source-only
results to claim better generalization without target access. Match information
access and relevant budgets, and disclose unavoidable asymmetries rather than
claiming that every comparison uses an identical architecture.

### Match the conclusion to the evidence

A main comparison supports predictive performance under its stated protocol.
An ablation supports the component's incremental contribution under that
comparison; it does not by itself prove the intended mechanism. A mechanism claim
requires observations or interventions that distinguish it from plausible
alternatives. An observed association is not automatically causal, and statistical
significance is not engineering importance.

Use the supported result, not a stronger story: distinguish “improves on these
held-out conditions,” “is consistent with the proposed mechanism,” and “is proved
under these assumptions.” Keep null, negative, and conflicting evidence in the
argument. Place a material limitation where it affects interpretation, without
repeating defensive disclaimers in every paragraph.

Before finishing, check the substantive alignment:

```text
gap -> idea -> method -> measured quantity -> experiment -> result -> conclusion
```

This is a reasoning check, not a new required graph, checklist file, or validation
system. Background, definitions, and implementation details may be necessary for
understanding or reproduction even when they do not supply a new claim. Remove
redundancy, not unique scientific content. Figures and tables must communicate
problem, mechanism, evidence, or boundary. Decorative AI artwork and panels
without a reader question are excluded.

## Adversarial review and stop rule

Review is a tool for discovering independent scientific problems, not a fixed
quota of personas or findings. Select only the lenses needed by the paper:
novelty, theory, methodology, experiment, statistics, generalization, domain
validity, reproducibility, positioning, writing, figures, or adversarial reject.

Prioritize:

```text
P0: invalidates the scientific conclusion
P1: seriously weakens the contribution
P2: important but non-fatal
P3: presentation
```

Each reviewer or review lens should report:

```text
Decision:
New independent P0/P1 issue:
Weakest claim:
Evidence missing:
Alternative explanation:
Required revision:
```

Stop expanding review when consecutive independent lenses no longer discover a
new P0/P1 issue. Repetition of an existing issue does not count as new information.
Do not manufacture reviewer theatre after the marginal scientific information has
fallen to zero.

Revision follows:

```text
review concern
-> root cause
-> required evidence
-> experiment, theory, method, analysis, or rewrite
-> observed result
-> claim update
```

When new evidence rejects the original claim, change the claim.

## Lightweight logs

Maintain only information that changes the research or paper decision.

`research_log.md`:

```text
Claim at risk
Key uncertainty
Action
Observation
Interpretation
Decision
```

`paper_log.md`:

```text
Claim changed
Hypothesis provenance
Evidence added
Novelty risk
Reviewer concern
Revision decision
Remaining blocker
```

Do not use logs to duplicate Git history or create an audit system.

## Completion

A research or paper action is complete when it changes a primary product and
resolves the intended decision:

- question, claim, or hypothesis;
- source-grounded novelty or literature conclusion;
- method or theory;
- executable code;
- actual experimental result;
- figure/table and caption;
- manuscript section;
- revised claim or reviewer response;
- uploadable submission files.

It is not complete because a plan, checklist, matrix, ledger, audit report,
validator, or CI job exists.

The optimization objective is:

```text
Research value
= scientific correctness × evidence × mechanism × clarity
  / unnecessary complexity
```
