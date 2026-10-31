# PaperTrace

**PaperTrace 是面向单篇科研论文的轻量工作区。** 让能读写项目文件的 AI Agent 围绕一个真实问题，直接推进研究设计、代码、实验、图表、论文和审稿返修，而不是反复生成计划和检查表。

```text
当前问题或未决矛盾
→ 选择最有信息量的一步
→ 检查真实产物和结果
→ 修订主张、机制或适用边界
```

可以从零开始，也可以继续已有论文。**不需要先填满模板，也不保证任何期刊录用。**

## 作者手动编辑入口

打开 **[paper/core/00_README.md](paper/core/00_README.md)**：01 执行约定、02 科学问题与 gap、
03 方法、04 实验 setting、05 综述协议、06 文献、07 进展、08 配置与运行入口，均为 Markdown。
编号只是导航；方法论文和综述按当前任务选用。作者可直接编辑；AI 先展示具体 diff，经确认后才写核心文档。
根 `AGENTS.md` 保留为工具自动识别入口；真实训练配置、BibTeX、结果和 PDF 不改变格式。

## 5 步开始使用

### 第 1 步：获取工作区

需要 Python 3.10+。有 GitHub 仓库访问权限时：

```bash
git clone https://github.com/liq22/PaperTrace.git
cd PaperTrace
```

也可以在 GitHub 下载 ZIP，解压后进入 `PaperTrace` 目录；默认 Core 模式不需要 Git。只有使用可选 ARIS 执行后端时才需要 Git clone。

### 第 2 步：初始化 Core

在 `PaperTrace` 目录运行：

```bash
python scripts/setup_papertrace.py --non-interactive
```

初始化程序会建立本地 `.venv`、安装最小依赖并检查项目状态。**Core 是默认模式**，不会下载 ARIS。看到 `PaperTrace 已就绪` 后即可开始；不必先安装其他 Skills。

### 第 3 步：在 Agent 中打开文件夹

用能读取和修改本地文件的 Agent（例如 Codex 或 Claude Code）打开整个 `PaperTrace` 目录，确认它能看到 `README.md`、`AGENTS.md` 和 `paper/`。

直接用自然语言提出任务即可；`00-router` 会在内部选择相关 Skill。你不需要事先学习或手动挑选所有 Skills。没有文件读写工具的纯聊天界面不能替代本地文件修改或实验执行。

### 第 4 步：选择你的起点

**A. 还没有确定研究方向**

将下列内容中的方括号替换成实际情况后发给 Agent：

```text
@初始化入口
研究对象：[对象]；观测数据：[数据/信号]；目标：[任务或待解释现象]。
目前已知：[真实观察、已有材料或研究疑问]。
请从已知事实梳理问题、最强竞争解释和下一步验证。
没有观察到的 failure、实验结果或近邻结论一律保持 unknown；
证据不足时不选择暂定方向，不为填满模板制造创新。
```

预期是一个简洁、可修订的研究判断；需要时更新 `paper/kickstart/core_innovation.md`。**零个候选也合法。** 方向是否正式选定仍由作者决定。

**B. 已经有代码、实验结果或论文草稿**

把材料放在 Agent 可访问的位置，并明确目标文件和本轮任务：

```text
我已有 [代码/实验结果/论文草稿]，位置是 [实际路径]。
本轮目标是：[一个具体问题，例如修复错误、分析结果或重写某节]。
请先读取 README.md、相关项目文件与必要的论文规范，
仅在该任务范围内修改主要产物，完成最相关的验证；
缺少数据或工具时说明缺口，不编造结果或扩大任务。
```

已有项目**不需要重新填写** `new_project_intake.yaml`；也不需要让 PaperTrace 覆盖原项目的数据、论文或配置。请求只读审查、讨论或计划时，明确写“只读，不修改文件”。

### 第 5 步：查看产物并继续下一步

不要只看 Agent 最后的文字总结：打开它实际修改或生成的文件。

| 本轮任务 | 应检查什么 |
|---|---|
| 研究方向 | 当前问题、竞争解释、未知项和下一步是否基于真实材料 |
| 代码 | 源码 diff、目标测试和有无无关重构 |
| 实验或统计 | 实际输出、独立实验单位、比较条件、指标与不确定性 |
| 图表 | 原图是否能打开，数据、单位、标签和 caption 是否一致 |
| 论文 | 改动段落与相邻上下文，数字、引文和结论边界是否保持 |
| 审稿回复 | 每条意见是否对应真实修改、证据与稿件位置 |

首次安装完成后，可单独检查当前项目：

```bash
python scripts/setup_papertrace.py --check-only --profile core
```

代码、实验、TeX 等任务还应运行相应的**最近测试或编译**；不能仅凭脚本存在或 Agent 自述判定工作完成。

## 你可以直接提出这些任务

| 我想做什么 | 可复制的请求 | 主要产物 |
|---|---|---|
| 收敛研究问题 | `比较当前解释与最强替代解释，找出最小决定性验证。` | 当前研究判断 |
| 理解已有代码 | `解释指定模块的输入输出、科学职责和边界；只读，不重构。` | 代码说明 |
| 修复代码 | `复现并修复这个错误，只修改必要源码并运行最近测试。` | 源码与测试结果 |
| 设计实验 | `明确公平 baseline、独立实验单位、指标和可能结果的解释。` | 可执行实验方案 |
| 运行实验 | `执行已确认的比较，返回真实文件、指标和不确定性。` | 实验输出 |
| 分析已有结果 | `基于指定结果计算效应与不确定性，区分观察和推断。` | 分析结果 |
| 梳理文献 | `核验最强近邻，比较方法假设、机制、结果和边界。` | 相关工作或文献综合 |
| 制作论文图 | `基于这些真实结果生成可编辑图表和完整 caption。` | 图表文件 |
| 修改论文 | `依据现有证据改写 Introduction，保留有效主线与全部引用。` | 正文 |
| 去掉防御性写法 | `删除空免责声明和重复 hedge，保留真实限制、负结果与数字。` | 修订文本 |
| 审稿返修 | `逐条处理真实 reviewer comments，先修论文或实验，再写回复。` | 正文修订与回复信 |
| 准备投稿 | `按目标期刊官方要求整理可上传材料，不执行正式投稿。` | 投稿文件 |

**审稿回复模板已恢复：** [Markdown 回复模板](paper/reviews/response_to_reviewers.md) 和 [LaTeX 回复信（含样式与 R1–R3）](.agent/skills/13-reviewer-response/assets/response-letter-latex-template/README.md)。它们是**按需使用的资产**，不是每篇论文都要填写的任务清单。

## 两个常用的论文深度任务

<details>
<summary>展开：撰写或重组章节</summary>

```text
按当前证据整理目标章节：Introduction 明确问题、具体缺口和贡献；
Method 解释设计理由、数学操作与待检验性质；
Results 区分实际观察、机制解释和结论边界。
保留原有有效内容，不虚构实验、近邻文献或方法细节；
直接修改正文，不另建重复写作流程。
```

论证可以按“科学问题 → 答案 → 证据 → 有边界的结论”组织；WHY–WHAT–HOW 是解释工具，不是必须填满的章节标题。[章节写作说明](.agent/references/research_first_paper_loop.md#paper-construction)。

</details>

<details>
<summary>展开：整篇论文诊断与优化</summary>

```text
对已有论文进行整体优化，但保留有效核心。
核对问题、最强近邻、方法机制、强 baseline、实现与实际实验。
区分 planned / implemented / executed / verified / supported；
检查干预是否实际被接收、使用并产生作用，区分实现错误与科学负结果。
只修复当前最重要的 blocker，执行最近验证，根据真实结果修订 claim。
最后给出 Scientific status、What changed、Claim–Evidence、
Critical reviewer risks 和 Next action；缺失结果明确标注。
```

整篇状态报告仅适用于此类请求，不强加给一处代码修改或一段文字润色。[完整说明](.agent/references/research_first_paper_loop.md#paper-optimization-and-scientific-status)。

</details>

## 主要文件在哪里

| 文件或目录 | 用途 |
|---|---|
| [`paper/core/02_RESEARCH.md`](paper/core/02_RESEARCH.md) | 当前研究问题、主张、最大不确定性、作者选择和正文来源 |
| [`paper/draft/main.md`](paper/draft/main.md) | Markdown 阶段的正文 |
| [`paper/kickstart/`](paper/kickstart/) | 可选研究方向材料 |
| [`paper/core/`](paper/core/00_README.md)、`paper/experiments/` | 集中的科研定义，以及实际运行结果和支持关系 |
| [`paper/refs/`](paper/refs/) | 文献与引用 |
| `paper/assets/` | 图表 |
| [`paper/reviews/`](paper/reviews/) | 审稿意见与回复 |
| [`paper/submission/`](paper/submission/) | 可复用投稿材料模板与实际投稿产物 |

当前状态以 `paper/core/02_RESEARCH.md` 为准，正文以它指定的 `active_source` 为准。历史日志不是第二套当前状态。某些模板已预置，但**无需为了看起来完整而填写**；未发生的实验、未查到的文献和未核实的主张保持未知。[工作区说明](paper/README.md)。

## 学术规范与任务边界

完整的论文研究、写作和证据规范只维护在：

@.agent/PAPER_SKILL_CORE.md

[阅读 Paper Skill Core](.agent/PAPER_SKILL_CORE.md) · [执行、Git 与安全规则](paper/core/01_PROJECT_RULES.md)

论文保持一条科学主线，使用本领域准确且统一的术语；结论不能超出已核验的理论、文献与实验。保留真正的不确定性、负结果和必要实现细节；不要把分支、PR、工具调用或 Agent 日志写成科研贡献。**代码任务、实验任务、论文任务和只读评审的产物与权限不同**，不能因为默认 Prompt 就把只读任务变成文件修改。

## 需要更多工具时（可选）

Core 足以使用仓库规则和本机已有工具完成许多任务。确实需要额外的检索、实验、绘图或编译能力时，再在 **Git clone** 的工作区启用 ARIS：

```bash
python scripts/setup_papertrace.py --profile execution
```

ARIS 位于 PaperTrace 的内部执行层，不是另一个用户入口。外部凭证、付费计算和数据外发需要相应权限；缺少工具时应如实说明，不能假装执行成功。[ARIS 使用说明](integrations/aris/README.md)。

## 更多使用说明

[新项目快速指南](QUICKSTART_NEW_PROJECT.md) · [完整工作区说明](paper/README.md) · [Agent 任务规则](paper/core/01_PROJECT_RULES.md) · [Claude 入口](CLAUDE.md)

<details>
<summary>维护者：完整仓库检查（合并 PR 前）</summary>

```bash
python scripts/check_aris_backend.py --profile core
python src/S03_Scripts/validate_project.py
python .agent/scripts/validate_agent_skills.py --skills-dir .agent/skills
python .agent/scripts/validate_agent_skill_wrappers.py
python .agent/scripts/validate_skill_evals.py
python -m unittest discover -s src/S04_Tests -v
```

`validate_skill_evals.py` 未提供 `--results` 时只验证案例定义，不执行 Claude、Codex 或其他模型。开发变更先提交功能分支和 PR，验证通过后合入 `dev`；不要直接改 `master`。

</details>

<details>
<summary>README 维护约定</summary>

README 由项目作者维护和审阅。本次用户明确授权直接重写并合并；本次完成后，Agent 默认将 README 视为只读。后续一般的仓库优化、同步或整理任务只提出建议或 patch，只有作者再次明确要求直接修改 README 才能改动它。

</details>
