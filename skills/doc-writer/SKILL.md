---
name: doc-writer
description: >-
  编写、补全和审查中文文档：PRD 与需求评审稿、技术设计、ADR、API 与参考文档、
  Runbook 与部署手册、测试计划与报告、产品介绍、README、发布说明。
  用户明确要求写、改或检查这类文档时使用；改代码、写提交说明、日常问答不用。
  主 agent 分阶段编排，派子 agent 研究代码与资料、写作和核查。
license: MIT
compatibility: 适用于能读写文件的 agent；能派子 agent 或用命令行调用其他模型时效果最好。doc-lint 需要 Python 3.9+。
metadata:
  author: blankhoney
  version: "3.2"
---

# 文档写作
本 skill 帮你依据项目的真实实现，写出读者拿来就能用的文档。
编排分三层：主 session 定义文档集并汇总，每篇文档一个 lead，lead 派 subagent 读代码、查资料、补研。
细节留在下层，主上下文只收文件路径和一行摘要，因为原文塞满上下文后，成稿质量会下降。

技能包根目录是本文件所在目录，下文路径都相对这个目录。

## 五条硬性要求
1. 按六个阶段编排，每个阶段的产出写成文件，下一阶段只读文件。派出的 agent 没有全部返回，不进入下一阶段。
2. 术语一致：每个多义词在术语表里定义一次，全文只用一个名字。
3. 正文遵守 `references/constraints-writing.md` 的 G1 表和 `references/formatting.md` 的排版硬线，交付前运行 doc-lint。
4. 交付前派 3 个独立核查 agent，只写证据表不改文档；lead 按证据表统一修改，主 session 读完证据表才交付。
5. 正文只用已查证或用户已确认的结论。未解决的问题不进文档，用户要求时除外；风险、已知限制和非目标只在用户要求时写，因为交付审核时才出现的讨论会被评审者驳回。

其余内容都是建议。项目有更好的写法时，按项目来。

## 六个阶段
各阶段交接的文件、提示和核查证据表见 `references/orchestration.md`。

1. **定义**：主 session 写清文档做什么、给谁看、回答哪些问题、范围多大，以及前提。简单请求默认写一篇，因为多篇文档容易互相矛盾。
2. **研究**：lead 并发派 4–6 个探索 subagent 读代码和资料，笔记每条附 `文件:行号`，发现的边界、竞争、风险和疑问另记到 `edges.md`。lead 不自己读代码。
3. **解决**：lead 派一个分诊 subagent 处理 `edges.md` 的每一条，产出 `resolutions.md`。提问前先查是否已有取舍；必须由人决定的记进 `questions.md`，不阻塞写作，交付时一次问用户。
4. **梳理**：lead 写 brief 和术语表。产品类再出产品梳理，技术类再出架构与数据模型。
5. **写作**：lead 派新上下文的写作 subagent，只读梳理材料和对应的写作指南。机制、流程、数据和示例照常写透，只是不写没有结论的讨论。长文按章节派多个，lead 合稿。
6. **核查**：并行派事实与一致、需求与范围、文风与排版 3 个核查 agent，只写证据表；lead 统一修改。

## 读哪个文件
| 文件 | 谁读、何时读 |
|---|---|
| `references/orchestration.md` | 主 session 和 lead，开工前读一次 |
| `references/writing/product.md` | 写 PRD、需求评审稿的片段 |
| `references/writing/tech.md` | 写技术设计、ADR、原理说明的片段 |
| `references/writing/reference.md` | 写 API、函数、配置项参考的片段 |
| `references/writing/ops.md` | 写 Runbook、部署手册、操作步骤、复盘的片段 |
| `references/writing/test.md` | 写测试计划、用例、测试报告的片段 |
| `references/writing/marketing.md` | 写产品介绍、README 开头、发布说明、对比表的片段 |
| `references/formatting.md` | 写作 agent 动笔前读，文风核查 agent 逐条对照 |
| `references/review.md` | 解决阶段的分诊 subagent 判断条目时读，写作 agent 动笔前读，需求与范围核查 agent 审查时读 |
| `references/constraints-writing.md` | 写作 agent 动笔前读 |
| `references/unslop.md` | 写作 agent 动笔前读，文风核查 agent 逐条核对 |

一篇文档常含多种片段，例如 README 的开头是产品介绍，安装节是操作步骤。
写作 agent 只读自己负责的片段对应的指南，这样上下文里只有用得上的规则。

运行 doc-lint：

```bash
python3 '<技能包根目录>/scripts/doc-lint.py' '<文档路径>'
```

扫描结果是候选，逐条判断后再改。命中不等于违规，零命中也不等于合格。

## 边界
- 保存或覆盖用户的文件前先取得授权。没有授权时，只输出正文。
- 文档里写到的部署、迁移、删除操作只写不做，因为它们会改变外部状态。
- 数据、运行结果和界面截图只写真实取得的。拿不到时写明缺什么、从哪里补。
