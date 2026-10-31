# `paper/` 工作区

作者从 [core/00_README.md](core/00_README.md) 编辑编号 Markdown；AI 修改核心文档须经明确确认。

`paper/` 服务一篇论文。当前状态、正文和历史记录分开维护；未使用的阶段文件不需要预先创建。

## 唯一职责

| 内容 | 位置 |
|---|---|
| 当前研究问题、主张风险、最大不确定性和下一动作 | `paper/core/02_RESEARCH.md -> research_state` |
| 方向批准 | `paper/core/02_RESEARCH.md -> idea_selection` |
| 当前正文 | `02_RESEARCH.md.active_source` 指向的文件 |
| 人读文章进展、证据摘要和下一步 | [07_PROGRESS.md](core/07_PROGRESS.md)，依据上述权威与真实产物更新 |
| 研究决策历史 | `paper/logs/research_log.md` |
| 论文主张与正文变更历史 | `paper/logs/paper_log.md` |

`new_project_intake.yaml` 只用于首次输入，不与 `02_RESEARCH.md` 持续同步。Git 已记录文件修改，不再维护 change log、freeze log 或第二套决策日志。

`core/07_PROGRESS.md` 应用户要求提供可持续维护的进展视图。它不复制作者批准、正文入口或
publication-stage 字段；模板初始状态不能当成某篇论文的研究进度。

## 单独使用分步 Prompt

从 [分步 Prompt 索引](prompts/README.md) 选择当前任务，复制主 Skill 说明、代码块与实际材料给
GPT Pro，或让本地 Codex 读取同一文件执行。每个任务标明已有 skill，不必加载整套流程。
Prompt 中的检索、仿真、真实实验、写作与投稿有各自的交付和停止边界；预期图表不冒充结果。

完整使用本工作区时，以这里的 `02_RESEARCH.md` 和 `core/07_PROGRESS.md` 维护一篇文章；只借用 Prompt
时，沿用现有论文仓的正文、配置、证据和状态权威，不强制复制整套 `paper/`。
若已有权威 STATUS，直接维护它；若新建进展页，只复制需要的结构并用真实材料初始化。
LQQL_OS 的 PaperTrace submodule 提供共享能力和模板，具体文章产物保存在文章项目中。

## 默认工作方式

在 `idea`、`outline` 和 `markdown_draft` 阶段，`paper/draft/main.md` 是 active source。只有形成真实内容后才创建对应记录：

```text
候选方向        paper/kickstart/idea_candidates.yaml
方法规格        paper/core/03_METHOD.md
关键文献        paper/core/06_LITERATURE.md
实验运行        paper/experiments/run_ledger.md
claim 支持      paper/experiments/evidence_matrix.md
图表            paper/assets/
正式 TeX        paper/tex/
审稿返修        paper/reviews/
投稿材料        paper/submission/
```

这些路径不存在或为空均表示“当前不需要”，不是缺失进度。不要创建 C1、E1、R1、RUN-1、F1 或空章节来填满模板。

## 研究闭环

```text
问题或失败
→ 最强竞争解释
→ 最小区分动作
→ 真实结果
→ 更新 claim、机制或边界
→ 需要时写入正文
```

方法进入 `ready` 时才要求 failure、最小 intervention、预测、拒绝条件、公平比较和 boundary test 闭合。正向 evidence 只能引用 completed run 或核验过的原文。负结果必须保留。

## Markdown 与 TeX

Markdown 正文稳定并经作者确认后，创建 `paper/tex/`，将 `active_source` 切换为 `tex`，并设置 `freeze.frozen=true`。转换后不再独立维护第二份正式正文。

## Review 与投稿

Review 是显式任务。只保留会改变结论或修订顺序的 P0/P1；连续视角不再产生新问题时停止扩展。Review 和 submission 文件由相应 Skill 在真实任务发生时生成，不保留空白评分表或通用 checklist。

## 验证

```bash
python src/S03_Scripts/validate_project.py
```

Validator 检查 active source、现有 scientific records 及必要的跨文件引用；它不要求完整生命周期骨架。
