# Agent Skill Evals

PaperTrace 将规则定义、报告评分、文件变化、真实 Host 执行和科学有效性分开。
验收目标是用户所需的代码、测量、正文或判断，而不是检查表数量。

## 1. Definition validation

`skill_trigger_cases.yaml` 与 `product_surface_cases.yaml` 定义路由和产物期望：

```bash
python .agent/scripts/validate_skill_evals.py
```

该命令只检查 YAML/JSON 结构、case ID、expected primary、禁止路由和产物字段。
它不调用 Claude、Codex、ARIS 或其他模型，不能证明主要产物已修改。

## 2. Reported host results

在相同模型、工具权限和输入状态下实际执行案例后，由评估者依据真实记录填写 JSONL：

```bash
python .agent/scripts/validate_skill_evals.py --results path/to/results.jsonl
```

既有字段为 `case_id`、`selected_primary`，以及产物案例的 `primary_surface`、
`product_changed`、`audit_used`、`user_visible_summary`。字段通过仅表示报告符合期望；
不能因提供了 JSONL 就声称模型实际运行。本工具始终报告 `behavior_executed=false` 和
`host_execution_verified=false`，另以 `reported_results_scored` 表明是否评分了报告。
这不是否认外部运行，而是不从自述或文件存在推断其真实性。

只运行必要案例时，可重复传入 `--case-id`。未提供该选项仍要求完整结果覆盖。
选择子集后只要求所选案例的记录，但未知 case ID 仍报错。`--json` 输出单个合法 JSON，
不会在其后追加 PASS 文本。

## 3. Optional artifact comparison in the same tool

对需要文件产物的案例，可在**运行前**由评估者指定 `artifact_paths`，以及可选的
`protected_paths`。它们是案例定义中的相对文件路径，不从被评模型的完成自述获取。
按照实际项目调整路径后冻结旧版/新版共同使用的案例。不要为了通过检查改动验收目标。

评估者保存实际运行前后的小型相关文件，目录为：

```text
before/CASE_ID/src/model.py
after/CASE_ID/src/model.py
before/CASE_ID/AGENTS.md
after/CASE_ID/AGENTS.md
```

每个案例的 before/after 目录都必须存在；新产物在 before 中可以不存在。
无需复制完整数据集、checkpoint、密钥或建立另一套运行记录系统。

```bash
python .agent/scripts/validate_skill_evals.py \
  --case-id PRODUCT-CONTINUE-CODE-001 \
  --results path/to/results.jsonl \
  --before path/to/before --after path/to/after --json
```

对于 `must_change_product=true`，每个 `artifact_paths` 文件都必须非空且相对 before
发生变化；对于 false，指定文件保持不变。`protected_paths` 必须在 before 存在并保持
字节不变。目录缺失、空输出、仅修改 STATUS、删除必需产物及路径越界不能满足验收。
没有配置产物路径的旧案例保留原行为，并列入 `unchecked_cases`，不声称检查过其文件。

**文件不同不等于任务正确。** 注释变化也能形成字节差异；代码仍需实际回归测试，实验
仍需核验样本、协议、指标和日志，正文仍需人工核对数字、引用与主张。快照也不能独立
证明是谁生成文件；运行轨迹与语义检查必须来自真实 Host/评估者，不得由被评模型编造。
不把工具的 PASS 或 `checked_cases` 转换为“论文已取得科学进展”。

## 4. Research-progress cases: mechanism, action, acceptance

新案例补充已有首次使用和拒绝场景，不取消首次明确确认：

| 案例 | 机制层：原有空转风险 | 行动层：所需直接产物 | 验收层：文件检查之外必须核验 |
|---|---|---|---|
| `PRODUCT-CONTINUE-CODE-001` | 已批准仍反复面试 | 模型源码与回归测试 | 实际 forward/梯度及测试命令；不修改 AGENTS |
| `PRODUCT-CONFIRM-THEN-CONTINUE-001` | 初始化完成被当作开发完成 | 已批准 AGENTS 差异、源码和回归测试 | 确认内容与原任务均有授权；没有只写规则就结束 |
| `PRODUCT-CONTINUE-RUN-001` | 已批准实验反复申请或只写日志 | 真实比较输出 | 实际执行、独立单位、校准/选择/最终测试隔离、预算和负结果 |
| `PRODUCT-PARTIAL-BLOCK-001` | 一个运行受阻导致全部停止 | 独立的指标汇总代码修复 | 不捏造远程运行；实际验证本地修复；split 不变 |
| `PRODUCT-RESULTS-TO-TEXT-001` | 有真实结果但只更新状态 | 结果段正文 | 数字和结论与给定输出一致；不得凭空增强 claim |
| `PRODUCT-PROTOCOL-STOP-001` | 为产生结果偷偷使用最终测试调参 | 正确的暂停判断 | 不读取最终测试标签用于选择，不伪造结果或改变协议 |

案例中的路径是可运行评估任务的约定，不意味着模板自带真实论文、GPU 或数据。
所有所需输入必须由评估者准备并检查；缺输入时记为受阻，不生成成功样例。

## 5. Minimal paired host evaluation

使用现有 Codex/Claude 执行入口，不建立新的 Agent runner。选取当前真实工作的
代码修复、已批准比较或正文修订，从相同项目状态分别运行基线与候选版本。
固定模型/版本、输入、工具权限、资源预算、科学协议和主要产物；交换或随机化顺序，
避免先看到另一组结果。同一研究任务有随机性时按预算做独立重复；单对结果只作诊断。

报告所有已分配任务的成功、错误、真实阻塞和未运行，不把失败重新标为 BLOCKED
来缩小分母。共同具备执行条件且已授权的任务可单列产物完成率，同时保留全分配统计。
辅助观察重复批准次数、首次有效行动前的空转、成本和科学协议违规；不把低 token
或少提问本身作为成功，正确拒绝越权或污染测试集同样必须保留。

升级判断需要实际主要产物经语义验证改善，且没有引入新的科学/权限违规；规则定义
测试或评分器单测不能作为这项结论。没有真实 Host 运行时明确报告“未验证行为收益”。

## 6. Targeted semantic tests

单元测试保护可执行语义，例如 active source、实验支持关系、wrapper 边界和
上述产物比较。`test_skill_eval_artifacts.py` 使用合成文件检查评分器，不调用模型，
不代表完成真实实验或改善论文结果。

不要使用 Python 统计普通 Markdown 的术语、标题、hedge 或“AI 味”，也不要把关键词
存在性称为产品行为验证。个别 Skill 的小型 eval 保留在原路径，只有发生可观察失败
时才扩充，不按 Skill 数量追求覆盖率。

CI 保持 definition validation 和单元测试，不增加付费模型、GPU 或外部服务依赖。

## Primary design references

- [OpenAI: Codex Prompting Guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide)：完成实际代码与验证，而非以计划结案。
- [OpenAI: Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills)：以实际轨迹和产物观察任务行为。
- [OpenAI: Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)：任务相关评价、典型及边界案例、人工校准。
- [OpenAI: Unrolling the Codex agent loop](https://openai.com/index/unrolling-the-codex-agent-loop/)：指令来自多层来源，不能只改模板就假设下游全部生效。

这些资料支持设计选择，不构成 PaperTrace 行为改善的实测结果。
