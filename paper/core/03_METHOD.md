# 03｜方法机制、数学定义与可证伪预测

> 作者直接编辑本文件；AI 先展示路径、理由与最小 diff，经本次或既有明确确认后再写入。
> `TODO`/`unknown` 表示尚未确定，不是失败，也不要求先填满全文才能工作。

日常只改 **Value** 或下方科学条目；`Field` 是稳定字段名，`Type=text` 保留自然语言，
`Type=json` 仅用于布尔值、数字、列表和空对象。长说明可在表下补充并从字段引用。
机器校验只核对结构和引用，不认证作者同意、不证明研究结论。

## 基本信息

| Field | Value | Type |
|---|---|---|
| schema_version | 1 | json |
| method_id | METH-001 | text |
| status | draft | text |
| supports_claims | [] | json |

## origin · 方法来源

| Field | Value | Type |
|---|---|---|
| origin.type | direct_problem | text |
| origin.source_idea_id | TODO | text |

## failure · 真实问题与竞争解释

| Field | Value | Type |
|---|---|---|
| failure.observed_failure_or_contradiction | TODO | text |
| failure.why_it_matters | TODO | text |
| failure.favored_explanation | TODO | text |
| failure.strongest_competing_explanation | TODO | text |

## scientific_job · 科学职责

| Field | Value | Type |
|---|---|---|
| scientific_job.research_question | TODO | text |
| scientific_job.target_decision | TODO | text |
| scientific_job.unit_of_analysis | TODO | text |
| scientific_job.input_object | TODO | text |
| scientific_job.output_object | TODO | text |
| scientific_job.operating_regime | TODO | text |

## mechanism · 最小机制与预测

| Field | Value | Type |
|---|---|---|
| mechanism.changed_object | TODO | text |
| mechanism.minimal_intervention | TODO | text |
| mechanism.theory_status | hypothesis | text |
| mechanism.assumptions | [] | json |
| mechanism.testable_implication | TODO | text |
| mechanism.expected_signature | TODO | text |
| mechanism.rejection_signature | TODO | text |
| mechanism.boundary_signature | TODO | text |

## evaluation_contract · 决定性比较

| Field | Value | Type |
|---|---|---|
| evaluation_contract.decisive_comparison | TODO | text |
| evaluation_contract.baseline_fairness | TODO | text |
| evaluation_contract.primary_metric | TODO | text |
| evaluation_contract.property_metric | TODO | text |
| evaluation_contract.boundary_test | TODO | text |

## implementation_notes · 实现位置

| Field | Value | Type |
|---|---|---|
| implementation_notes.source_modules | [] | json |
| implementation_notes.config_paths | [] | json |
| implementation_notes.reproducibility_notes | [] | json |

## components · 实际必要组件

| component_id | scientific_role | strongest_alternative | deletion_test |
| --- | --- | --- | --- |

空表表示尚无正式条目。不要为了模板完整创建假 claim、实验或组件。

## 数学定义与设计理由（按实际需要填写）

明确 $x,y,d,u,\theta$ 等符号的对象、shape、单位与可见范围，定义最小改变和为何需要它。
写出实际映射、目标函数或命题；说明假设如何约束推导、何种反例会推翻结论。
复杂推导可以写在此处或引用既有正文，不要求额外建立一个推导框架。
`hypothesis`、`analysis`、`proposition` 分开；实现了计算路径不代表证明了机制。

每个组件说明 scientific_role、strongest_alternative 与 deletion_test；没有必要组件就保留空表。
纯理论用证明与反例承担责任；不适用的实验字段说明理由，不能编造实测结果。
综述一般不需要本页，保持 draft 不应阻止 05/06 与正文推进。

`status` 使用 draft 或 ready；ready 表示方法定义已足够明确供协议核对，不表示假设已被实验支持。
`origin.type` 使用 direct_problem 或 promoted_idea；后者引用真实 IDEA 条目。
未知假设保持未知，不把“非显著”写成等效或不存在效果。
