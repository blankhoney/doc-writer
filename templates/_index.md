# 文档类型模板索引

> L1 层模板文件。准备阶段确定类型后完整读取对应模板，包含变体、条件、类型验证与适用分支，不裁成阶段片段。
> 选型及固定/定制边界见[准备入口](../runtime/prepare.md)；维护模板时见[模板规范](../docs/modules/5.2-document-templates.md) §5.2.8。

## 工程生命周期文档

| 类型 | 文件 | 默认变体 | 变体数 | 文风 |
|------|------|---------|--------|------|
| PRD | [prd.md](prd.md) | Lean | 4 | 陈述句；需求写成可验证条件，不写实现细节 |
| 技术设计 | [tech-design.md](tech-design.md) | Lean | 4 | 论证式；结论先行，每个取舍带依据 |
| API 文档 | [api-doc.md](api-doc.md) | 端点参考 | 3 | 契约式；现在时，字段、错误码照实写 |
| Changelog | [changelog.md](changelog.md) | Keep a Changelog | 3 | 面向使用者的影响；一条一事，以动作开头 |
| 测试报告 | [test-report.md](test-report.md) | CI 报告 | 3 | 数据式；结论先行，失败与未测如实写 |
| 部署/Runbook | [deploy-runbook.md](deploy-runbook.md) | Deploy Guide | 4 | 祈使句步骤；每步带验证信号，警告放在动作前 |
| ADR | [adr.md](adr.md) | Nygard | 5 | 决策式；"我们将……"，保留决策时的语境 |

**章节名怎么用**：模板表格里的章节名是内容槽位，不是必须照抄的标题。只有外部标准规定的名称照原样写：Nygard ADR 的 Context / Decision / Consequences、MADR 4.0 的节名、Keep a Changelog 的 6 个分类。技术设计、ADR、测试报告、PRD 这类论证文档，可定制章节的标题写成结论句（"选用单体架构"，不写"架构选型"）；Reference、How-to 等查阅和操作类文档保留名词或祈使句标题。规则见 [C1e 金字塔结构](../docs/modules/constraints-common.md)。

技术设计在同一类型内选架构方案／程序详细设计任务分支，再选原有变体；分支入口见该模板，不增加类型。

## 知识传递文档（Diátaxis）

项目介绍与现有架构说明的独立文档按理解任务选 Explanation，不因读者负责验收就选变更或测试报告。Quickstart 指最快用上真实主要功能：已有会话或工具基础、只想完成一次任务时选 How-to 任务食谱；需要引导学习才选 Tutorial 最短路径，不另建类型。

| 类型 | 文件 | 默认变体 | 变体数 | 文风 |
|------|------|---------|--------|------|
| Tutorial | [tutorial.md](tutorial.md) | 最短路径 | 3 | 第二人称引导；每步有预期结果，不展开原理 |
| How-to Guide | [how-to.md](how-to.md) | 任务食谱 | 3 | 祈使句；假设读者有基础，直达目标 |
| Reference | [reference.md](reference.md) | 键卡片 | 4 | 中性描述；结构对应代码，不给建议 |
| Explanation | [explanation.md](explanation.md) | 概念解释 | 3 | 陈述与论证；可比较和表态，不给操作步骤 |

## 项目首页

仓库根目录的 README 选本类型；它把读者分流到上面各类文档，不替代它们。

| 类型 | 文件 | 默认变体 | 变体数 | 文风 |
|------|------|---------|--------|------|
| README | [readme.md](readme.md) | 工具与库 | 3 | 面向首次访问者；首段陈述，步骤祈使，声明有依据 |

## 扩展

新增文档类型按[模板指导](../docs/modules/5.2-document-templates.md) §5.2.10 执行。
