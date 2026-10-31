# 07｜文章进展与当前任务缺口

> 作者直接编辑；AI 更新本页须展示实际来源与 diff 并获确认。等待更新不阻塞独立已授权工作。
> 最近核验：2026-10-17。当前是 PaperTrace 通用工作区，尚未绑定真实论文。
> 本文件是人读进展视图；研究事实、作者选择、正文来源和投稿阶段以
> [02_RESEARCH.md](02_RESEARCH.md) 为准。发现冲突时回查权威与原始产物，不从本页反向覆盖作者决定。

## 当前实际情况

- `02_RESEARCH.md` 的研究对象与核心问题尚未填写，正式 claims、contributions 和 required experiments 为空。
- 尚无可据此判断创新性、方法有效性或真实实验完成情况的项目证据。
- 仓库已有的 Prompt、技能、方法/实验模板与仓库测试不构成某篇论文的科学结果。
- 下一项建议：提供实际研究对象、已有材料和本轮目标，从 [分步 Prompt](../prompts/README.md) 中选当前最有价值的一步；已有项目先读取其自身状态和产物。

## 阶段进展视图

下表用于接续工作，不表示必须顺序填满。阶段名不是 `paper_stage` 的新枚举；
综述、纯理论与已有项目按实际贡献调整。只有直接检查产物后才更新相应行，
记录核验日期和证据位置；不使用完成百分比推断科学成熟度。

| 工作 | 负责 skill（顺序交接） | 当前可核验进展 | 下一个可检查的产物 |
|---|---|---|---|
| 当前项目与初步 idea | `01-project-brief` → `scientific-brainstorming` | 未绑定课题；不能选择方向 | 已知事实、竞争解释与候选问题 |
| 文献调研与全文获取 | `03-literature-deep-research` → 外部 `project-paper-curator` | 尚未核验真实题录、全文与深读数量 | 分别报告独立工作、有效 PDF、深读与缺失项 |
| 最近邻定位 | `03-literature-deep-research` | 无原文支持的比较结论 | 公平比较矩阵、原文依据与 gap |
| 正式假设与 motivation | `hypothesis-generation` → `15-figure-table-design` | 未形成可确认的候选 | 机制、反证条件和 motivation 草图供作者选择 |
| 方法、理论与最小仿真 | `method-design` → `experimental-design` → `06-experiment-ops` | 模板存在不代表推导成立或实验运行 | 必要证明、物理/任务可信 PoC、负对照与失效边界 |
| 方法 framework | `15-figure-table-design` | 无项目方法图 | 对照方法核验拓扑的可编辑框图 |
| 真实实验协议与结果模板 | `experimental-design` → `15-figure-table-design` | 未确认数据、协议或预算 | 独立数据源、强基线、TBD 图表和支持/反证模式供审阅 |
| 配置、Shell 与实际运行 | `code-change` → `06-experiment-ops` | 无本文实际运行证据 | 通用实现、配置列表、完整 Shell 与真实输出 |
| 分析与创新主张判断 | `statistical-analysis` → `05-claim-evidence` | 尚不可判定 | 每条主张的效应、不确定性、替代解释与支持边界 |
| 全文、图表与语言 | `08-markdown-draft` → `15-figure-table-design` → `10-language-polish` | 未提供真实稿件与结果图 | 唯一正文、真实数据图、完整 caption 和准确意群 |
| 引文、定点复审与投稿 | `11-reference-audit` → `peer-review` → `09-tex-freeze-formalize` → `12-submission-pack` | 尚未形成可提交材料 | 核验后的正文/引用/材料及真实作者确认 |
| 真实审稿返修 | `13-reviewer-response` | 未提供编辑决定或真实审稿意见 | 意见对应的实际修改、证据位置与回复；待做和已核验完成分开 |

实际文献目标、数据集要求、预算和已有授权从项目协议读取。分步实证研究 Prompt
采用用户指定的 50 篇独立工作和至少两个独立真实数据集；不能凭两个切分或同一论文
的多个版本补足数量。`project-paper-curator` 在提供该 skill 的环境使用，未随本仓默认安装。
需要专项支持时见[按任务选用 Skill](../../.agent/references/task_specific_skill_selection.md)；
读取外部规范、实际执行工具和完成科学核验是不同进展，不能因链接已接入而标记审稿或实验完成。

## 主张与证据

当前没有正式主张，不创建空的 Claim ID 或支持记录。形成真实主张后，只摘录影响下一步
决定的结论并链接既有 [evidence matrix](../experiments/evidence_matrix.md)、推导或原文位置，
不复制完整实验记录。每条摘要包含：**主张与范围 → 证据 → 判断 → 剩余缺口 → 最小区分行动**。

- **Supported**：证据支持写明条件下的主张；列出适用范围和仍未证明的部分。
- **Refuted**：有效结果否定必要预测；保留负结果并修订机制或主张。
- **Inconclusive**：未测、运行无效、信息不足或结果尚不能区分解释；写明原因。

这些解释与既有汇报标签相容：限定支持对应 `SUPPORTED`，较宽主张仍有缺口可写
`PARTIALLY SUPPORTED`，尚未检验为 `UNTESTED`，有效反证为 `CONTRADICTED`。
不增加机器枚举；不把执行成功、显著性不足或漂亮图形自动转换为科学结论。

## 维护约定

维护规则见 [STATUS 指南](../../.agent/references/research_first_paper_loop.md#status-without-duplicate-authority)。
完成会改变研究判断或推进阶段的已授权工作后，先核验主要产物和现有状态，再更新相关摘要。
只读任务不写文件。作者授权仍在原权威位置记录；本页的“完成”不能代替批准。
原始运行、历史决定分别留在现有记录与 Git 历史中，不再添加第二套日志。

在 LQQL_OS submodule 中，这是一份可复用起始页。具体论文的进展维护在该论文项目内，
不要将多篇文章的状态写回共享 PaperTrace。下游已有权威 STATUS 时继续使用它，不另建副本。

## 当前任务 gap（只有存在真实任务时填写）

| Gap 类型与具体缺口 | 原始依据 | 下一项已授权行动 | 验收产物/观察 | 精确阻塞（若有） |
|---|---|---|---|---|

区分 Research、Evidence、Engineering、Access 和 Writing gap；不是每种都必须有。
只保留当前改变判断的事项；结果写回实际代码、输出或正文，再拟议本页摘要。
不要用完成百分比、测试数量或新计划数量证明科学推进；本页不新增批准字段。
