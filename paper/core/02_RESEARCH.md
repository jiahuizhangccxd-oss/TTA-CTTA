# 02｜科学问题、Research Gap 与当前判断

> 作者直接编辑本文件；AI 先展示路径、理由与最小 diff，经本次或既有明确确认后再写入。
> `TODO`/`unknown` 表示尚未确定，不是失败，也不要求先填满全文才能工作。

日常只改 **Value** 或下方科学条目；`Field` 是稳定字段名，`Type=text` 保留自然语言，
`Type=json` 仅用于布尔值、数字、列表和空对象。长说明可在表下补充并从字段引用。
机器校验只核对结构和引用，不认证作者同意、不证明研究结论。

## 基本信息

| Field | Value | Type |
|---|---|---|
| schema_version | 1 | json |
| project_name | TODO | text |
| paper_title | TODO | text |
| short_title | TODO | text |
| language | English | text |
| paper_stage | idea | text |
| active_source | markdown | text |
| target_venue | {} | json |
| authors | [] | json |
| compliance | {} | json |

## draft_source · Markdown 正文入口

| Field | Value | Type |
|---|---|---|
| draft_source.path | paper/draft/main.md | text |

## formal_source · TeX 正文入口

| Field | Value | Type |
|---|---|---|
| formal_source.path | paper/tex/main.tex | text |

## freeze · 正式化状态

| Field | Value | Type |
|---|---|---|
| freeze.frozen | false | json |

## idea_selection · 作者方向决定

| Field | Value | Type |
|---|---|---|
| idea_selection.selected_idea_id | TODO | text |
| idea_selection.approved | false | json |
| idea_selection.approved_by | [] | json |
| idea_selection.approved_at | TODO | text |

## problem_definition · 研究对象与问题

| Field | Value | Type |
|---|---|---|
| problem_definition.object | TODO | text |
| problem_definition.environment | TODO | text |
| problem_definition.observation | TODO | text |
| problem_definition.task_or_decision | TODO | text |
| problem_definition.failure_or_contradiction | TODO | text |
| problem_definition.desired_understanding | TODO | text |

## research_state · 当前科学判断

| Field | Value | Type |
|---|---|---|
| research_state.central_question | TODO | text |
| research_state.current_claim_at_risk | TODO | text |
| research_state.strongest_support | TODO | text |
| research_state.favored_explanation | TODO | text |
| research_state.strongest_competing_explanation | TODO | text |
| research_state.largest_unresolved_uncertainty | TODO | text |
| research_state.current_novelty_risk | TODO | text |
| research_state.most_informative_next_action | TODO | text |
| research_state.possible_outcomes_and_decisions | TODO | text |
| research_state.stopping_condition | TODO | text |

## artifacts · 现有产物位置

| Field | Value | Type |
|---|---|---|
| artifacts.method_spec | paper/core/03_METHOD.md | text |
| artifacts.figures | paper/assets/figures/ | text |
| artifacts.tables | paper/assets/tables/ | text |
| artifacts.bibliography | paper/refs/references.bib | text |
| artifacts.evidence_matrix | paper/experiments/evidence_matrix.md | text |
| artifacts.run_ledger | paper/experiments/run_ledger.md | text |
| artifacts.research_log | paper/logs/research_log.md | text |
| artifacts.paper_log | paper/logs/paper_log.md | text |

## human_gates · 不可代填的作者确认

| Field | Value | Type |
|---|---|---|
| human_gates.markdown_freeze_approved | false | json |
| human_gates.submission_approved_by_all_authors | false | json |

## main_claims · 正式主张

| claim_id | text | status | evidence_state | hypothesis_provenance | boundary |
| --- | --- | --- | --- | --- | --- |

空表表示尚无正式条目。不要为了模板完整创建假 claim、实验或组件。

## main_contributions · 贡献

| contribution_id | text | supporting_claims |
| --- | --- | --- |

空表表示尚无正式条目。不要为了模板完整创建假 claim、实验或组件。

## required_experiments · 必要比较

| experiment_id | supports_claims | description |
| --- | --- | --- |

空表表示尚无正式条目。不要为了模板完整创建假 claim、实验或组件。

## 如何填写 Research Gap（不是流程缺口）

先核验：具体问题与条件、最近邻原作、其已解决范围、仍未解决的边界、能够区分解释的观察。
`current_novelty_risk` 写最近邻可能否定什么贡献；`largest_unresolved_uncertainty` 写当前证据缺口；
`most_informative_next_action` 写一个能改变判断的行动；`possible_outcomes_and_decisions` 写支持、反证或不可判定后怎么做。
缺代码、未下载 PDF、无 GPU 是任务/访问缺口，不自动构成 Research Gap。
不存在实测 failure 时保留 unknown；不能为了启动流程制造失败现象或选定方向。

综述将“竞争解释”用于已有综述或更简单综合框架；创新来自原文支持的新认识，不强套分类实验。
主张、方向批准和正文入口只在此处维护；07 仅是可读摘要。实验条件在 04，综述条件在 05。
这里记录批准不证明批准真实性；AI 只能抄录真实作者决定，不能自行把 false 改成 true。

## 固定字段的可用值

`paper_stage` 保留已有取值：idea、outline、markdown_draft、tex_formalization、submission_ready、submitted、revision、accepted。
这描述当前正文/投稿状态，不强迫依次执行全部流程。`active_source` 为 markdown 或 tex，路径均相对仓库根目录。
只有真实作者确认后的 Markdown → TeX 正式化才能把相应 freeze 与 human_gates 字段写为 true；
拟定投稿包不自动代表所有作者批准。作者名单、venue 和合规信息只在实际需要时填写。
