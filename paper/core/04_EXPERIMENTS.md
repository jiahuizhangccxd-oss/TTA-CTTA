# 04｜实验设定与比较协议

> **未绑定真实论文；本文件是待作者编辑的模板，不是已批准协议。**
> 作者直接编辑；AI 修改须先展示 diff 并获确认。只填写本次实验必要的部分；编号、示例、空表不产生实验义务。
> 主张与当前判断在 [02](02_RESEARCH.md)，数学机制在 [03](03_METHOD.md)，实际入口在 [08](08_EXECUTION.md)。

## 1. 本项目采用的范围

| 项目 | 本项目确定的内容 |
|---|---|
| 本次需要回答的主张/问题 | unknown；引用 02 中条目，不复制完整主张 |
| 论文类型与本协议适用范围 | unknown；纯理论/综述没有实验时明确不适用 |
| 本次采用的 setting | unknown；从下方选择适用项，不是全部运行 |
| 当前协议与原始配置位置 | unknown |
| 作者对该协议及运行范围的确认依据 | 尚未确认；仅引用真实对话或 PR，不由 AI 自行填写批准 |

## 2. 十六个 setting 维度

“示例”不代表本项目取值。先查原始数据、源码、配置与作者已作决定，再填写最后一列。

| Setting | 要回答的问题 | 应写到什么程度 | 示例（不是默认值） | 本项目取值/位置 |
|---|---|---|---|---|
| Problem | 究竟预测或决策什么？ | 输入、输出、预测时点、类别/单位、可观测真值、用途 | 故障分类 / RUL / 异常检测 | unknown |
| Object | 独立物理对象是什么？ | 设备身份、故障来源、真实/仿真、生命周期边界 | 轴承 / 齿轮箱 / 电池 / 机器人 | unknown |
| Observation | 模型允许看到什么？ | 通道、单位、采样率、长度、缺失模式、可见元数据 | 振动 / 电流 / 多变量时序 | unknown |
| Domain | 什么变化构成域？ | 域变量及组合、哪些训练见过、哪些严格未见 | 转速 × 载荷、设备、站点、时间 | unknown |
| Task regime | 训练、适应和测试如何交互？ | 标签与输入权限、更新时机、状态是否重置 | supervised / DG / UDA / TTA / continual | unknown |
| Independent unit | 什么才是独立统计单位？ | 对象/采集/完整运行/会话层级；聚类结构 | machine、run、physical acquisition | unknown |
| Split | 哪些单位互斥？ | 划分顺序、group ID、时间边界、验证来源、最终测试身份 | train/validation/test 按设备或运行隔离 | unknown |
| Target access | 每阶段允许访问目标域什么？ | 输入、标签、元数据、批量/逐点可见性、更新/选择权限 | no access / unlabeled / few labeled | unknown |
| Preprocessing | 哪些统计量在哪里拟合？ | 单位、重采样/抗混叠、切窗、归一化、缺失值、拟合范围 | training-only normalization | unknown |
| Method | 实际改变哪个机制？ | 指向 03 的最小干预；保持其他差异受控 | representation / constraint / decision | unknown |
| Baselines | 最强有效参照是什么？ | 简单参照、最近邻方法、可访问数据、调参机会和数值专家 | matched classical + closest prior | unknown |
| Loss | 优化目标是什么？ | 公式、各项权重、计算数据、监督来源与梯度方向 | classification / regression / auxiliary | unknown |
| Metrics | 评价什么性质？ | 定义、单位、聚合权重、阈值、主次指标和越大/小越好 | Macro-F1 / MAE / AUROC / latency | unknown |
| Tuning | 如何选择参数与 checkpoint？ | 开发数据、选择指标、候选空间、早停、校准与选择区别 | 源域验证 / 独立校准 | unknown |
| Budget | 可以消耗多少资源？ | 单次与累计 CPU/GPU/API/磁盘预算、重复、已用量、停止条件 | GPU-hours、seeds、search trials | unknown |
| Claim test | 什么结果改变主张？ | 待估效应、竞争解释、支持/反证/不可判定模式及边界 | effect size + mechanism/boundary | unknown |

## 3. 信息权限和更新时机

以下是待选择的协议范例。真正采用哪一种及任何例外由作者明确；不能因名称相似偷换信息权限。

| Setting 示例 | 拟合/适应信息 | 模型选择信息 | 评价时允许更新什么 | 易混淆之处 |
|---|---|---|---|---|
| Supervised held-out | 标注训练集 | 独立验证集 | 默认冻结模型 | 同分布不等于同一采集窗口可泄漏 |
| Source-only / DG | 单/多源数据 | 允许的源域开发划分 | 本示例冻结；目标只用于最终评价 | 用目标统计量拟合已改变这个 DG 协议 |
| UDA | 标注源 + 明确的无标签目标适应集 | 预定且不使用最终标签的规则 | 是否在线继续适应需另定 | 无标签适应集与最终评价集是否同一总体须写清 |
| Few-shot | 规定 support 的标注样本 | 独立 development episode | 按 support 更新 | shot 按物理单位还是窗口计数，query 必须隔离 |
| TTA | 已训练模型 + 规定可见的无标签测试输入 | 开发阶段冻结规则 | 指定参数/统计量；批量或逐点；重置规则 | 不能用目标标签/全流未来输入选择策略 |
| Continual / online | 按时间到达的合法数据和标签 | 预定义因果规则 | 指定更新、回放容量、标签延迟 | 必须说明先测后学还是其他明确协议 |
| Healthy-reference anomaly | 合法健康 fit/calibration 数据 | 校准规则 | 是否固定阈值需声明 | 拟合正常参考不自动等于标签调参；最终测试反馈不得选阈值 |
| Open-set / open-world | 明确 known/unknown 身份与可见标签 | 独立未知类开发条件（若允许） | 预定义拒识/增类规则 | 不能看最终 unknown 类后重定阈值与类别 |
| Generative | 训练观测和允许的条件 | 独立验证规则 | 固定采样/条件权限 | 生成质量、任务效用与物理一致性不能用同一指标代替 |
| Agent evaluation | 固定模型、工具、知识、数值专家和 episode 观测 | 开发 episode | 可见历史与允许记忆；按协议重置 | 工具/Token 预算、隐藏标签与干预是否被实际使用 |

## 4. Split、归一化和时间因果性

用 $u$ 表示真正需要隔离的物理或采集单位，$d$ 表示域，$w$ 表示窗口。
先按本项目定义划分独立单位，再切窗；具体隔离要求来自所研究的泛化目标，不能把所有研究强制成同一种划分。

若协议要求训练与测试对象隔离，应满足 $U_{train}\cap U_{test}=\varnothing$。
还须明确 train–validation 是否同样按对象隔离，不能仅验证窗口索引不同。

| 核对项 | 本项目规定与实际文件 |
|---|---|
| 原始数据源、版本、单位 ID 与合法使用范围 | unknown |
| 切分发生在切窗前还是后、窗口重叠、stride | unknown |
| 多通道/多模态同一事件是否落入同一 group | unknown |
| 归一化/插补/特征选择/阈值统计量的拟合范围 | unknown |
| 训练、验证、校准、最终测试的角色是否独立 | unknown |
| 在线观测顺序、预测时刻、更新时刻、可见未来长度 | unknown |
| Few-shot support/query、episode 重复与物理对象复用 | unknown |

## 5. Notation、loss 和任务输出

以下公式仅为写作示例；实际公式与源码逐项对齐，不自动选择算法。

| 任务 | 示例定义 | 必须进一步明确 |
|---|---|---|
| 分类 | $f_\theta(x)\in\mathbb{R}^{K}$，$\mathcal{L}_{cls}=-\frac1N\sum_i\log p_\theta(y_i\mid x_i)$ | 类别顺序、label dtype、class weight、样本/域权重 |
| 回归/RUL | $\hat y_i=f_\theta(x_i)$，$\mathcal{L}_{reg}=\frac1N\sum_i(\hat y_i-y_i)^2$ | 目标单位、截断、预测时点；训练 MSE 不等于评价 MAE |
| 辅助目标 | $\mathcal{L}=\mathcal{L}_{task}+\lambda\mathcal{L}_{aux}$ | 辅助项来源、允许信息、梯度、权重如何选；证明不是额外预算优势 |
| 异常检测 | $s(x)$ 与校准阈值 $\tau$ | 训练是否仅健康、分数方向、阈值来源、点/窗口/事件评价 |
| 生成/Agent/纯理论 | 按问题单独定义 | 不强行套用分类 loss；需要的是目标、约束、测量或命题 |

复杂条件分布、时频变换和推导写在 03；此处只规定如何比较。Pipeline 记为：
**原始单位 → split → 合法预处理拟合 → 训练/适应 → 校准/选择 → 冻结规则 → 评价 → 分析**。
它是信息依赖关系，不是另一个执行程序。实际调用只使用 08 指定的既有入口。

## 6. 公平比较与结果判定

| 项目 | 本项目约定 |
|---|---|
| 待估效应（相对哪个 baseline、什么单位/条件） | unknown |
| 简单强参照与最近邻原始实现/版本 | unknown |
| 相同数据、预处理、信息访问与选择机会 | unknown |
| 等容量/等预算/等数值专家对照的必要范围 | unknown |
| 主要指标、次要指标、聚合与单位 | unknown |
| 重复来源：设备/数据划分/初始化/episode | unknown |
| 不确定性：何种独立单位、区间或分层分析 | unknown |
| 支持、反证、不可判定与实现失败的区分 | unknown |
| 哪项边界或机制比较确实能改变主张 | unknown |

随机种子重复不能自动替代独立设备或采集。无足够独立单位时明确推断范围，不机械添加显著性检验。
有效负结果保留；不因不支持论文就重标为 invalid。不以单个漂亮均值声称机制已成立。

## 7. 运行范围与停止

预算、数据、信息访问和配置列表必须有可追溯的实际确认。完整队列已批准时按相同范围继续，不逐项重问。
协议分别明确源域拟合、独立校准、超参数搜索和最终测试的权限，一次确认可覆盖完整队列；“零调参”不自动禁止方法定义中的拟合，也不允许隐含选择。
仅暂停受实际缺口影响的运行；不切换到假数据后称正式实验完成。
达到既定预算、完成本次判别或发现共享协议错误时停止相应循环；不得无限技术重试、追加消融或重新规划。

## 参考

[NeurIPS Paper Checklist](https://nips.cc/public/guides/PaperChecklist) 提供划分、参数选择、统计不确定性、计算资源与复现信息的报告要求。
本模板不代表任何 setting 已获批准，不保证具体论文的科学设计充分。
