# 08｜配置、运行入口与复现

> 作者直接编辑；AI 修改先提 diff 并确认。此页是入口说明，不是第二份机器配置。
> 科学设定以 [04](04_EXPERIMENTS.md) 或 [05](05_REVIEW.md) 为准；规则以 [01](01_PROJECT_RULES.md) 为准。

## 本项目实际入口（先检查，再填写）

| 内容 | 实际路径/命令 | 修改与验证边界 |
|---|---|---|
| 开发入口 | unknown | 不因历史项目存在 main.py 就假设本仓也存在 |
| 用户接口/包 | unknown | 复用已存在接口，项目不需要时不创建 |
| 机器配置 | unknown | YAML/JSON/TOML/Python 保持运行格式；本页只链接，不重复参数值 |
| 任务/模型/数据模块 | unknown | 说明职责和最小调用路径，不新增 parallel runner |
| Python/依赖环境 | unknown | 记录实际解释器与版本；不擅自升级系统环境 |
| 数据与 checkpoint | unknown | 指向真实位置；不复制秘密、完整数据或权重到 core |
| 最近回归测试 | unknown | 针对影响行为，而不是固定全仓检查 |
| 已批准运行队列 | unknown | 配置列表、单次与总预算只引用原授权/协议 |
| 结果、图源与唯一正文 | unknown | 保留既有位置，不用日志替代产物 |
| 集成目标与发布权限 | unknown | Git 权限不等于科学批准或对外发表许可 |

使用 `phmfactory`、Lightning、main.py 等必须以实际项目为依据；不把领域示例当作安装依赖或启动命令。
只有用户确认选择后才填具体入口。运行时配置与人读协议矛盾时定位差异，不自动重写任一方；
已授权工程错误可以修复，科学语义变化需作者决定。

## PyTorch/时序项目的按需核对

只检查受本次变更影响的 tensor 维度语义、dtype/device、标签/loss、梯度、train/eval 与 checkpoint。
采样率、物理量纲、FFT 维度、重采样抗混叠、切窗 group 和归一化拟合范围保持一致。
CPU 合成输入通过不是 GPU 或真实诊断实验通过。缺设备仅影响依赖它的测试，不制造整项目阻塞。
不通过异常吞没、无条件 CPU fallback、替换数据/checkpoint 或隐藏默认值制造成功。
协议预先规定的降级可以实现，但必须显式记录发生条件，不能改变论文任务而不说明。

## PaperTrace 自身已存在的工具

以下是模板工具，不是下游论文的训练命令。在仓库根目录运行：

```bash
python scripts/setup_papertrace.py --check-only --profile core
python src/S03_Scripts/validate_project.py
```

前者检查 Core 环境，后者检查 Markdown 科研记录与实际存在的关联记录；不会自动执行论文实验。
开发集成仍使用根 README 的现有测试；普通段落修改或文献核验不必每次运行完整套件。

## 交付判断

Engineering：源码和最近验证；Experiment：合法真实输出与比较；Science：主张支持、反证或边界；
Manuscript：真实正文与图表。文件格式转换、Git 合并、测试数量不是论文科学贡献。
