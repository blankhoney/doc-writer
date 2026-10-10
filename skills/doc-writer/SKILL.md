---
name: doc-writer
description: >-
  编写、补全和审查中文文档：PRD 与需求评审稿、技术设计、ADR、API 与参考文档、
  Runbook 与部署手册、测试计划与报告、产品介绍、README、发布说明。
  写、改或检查这类文档时使用；改代码、写提交说明、日常问答不用。
  默认轻量档：只用写作规则和调研；用户点名本 skill 要求定稿或完整流程时，
  由主 agent 编排研究、写作和核查。
license: MIT
compatibility: 适用于能读写文件的 agent；能派子 agent 或用命令行调用其他模型时效果最好。doc-lint 需要 Python 3.9+。
metadata:
  author: blankhoney
  version: "3.5"
---

# 文档写作
依据项目的真实实现写文档，让读者能照着使用。

技能包根目录是本文件所在目录，下文路径都相对这个目录。

## 四条硬性要求
1. 先按「选档」定档。完整档按 `references/orchestration.md` 编排，并在交付前执行其中的核查。
2. 术语一致：每个多义词只定义一次，同一个词只指一个对象，指多个对象时各起限定名；同一动作不换近义词。完整档另建术语表，见 `references/orchestration.md`。
3. 正文遵守 `references/constraints-writing.md` 的 G1 表和 `references/formatting.md` 的排版硬线，交付前运行 doc-lint。
4. 正文只用已查证或用户已确认的结论。未解决的问题不进文档，用户要求时除外。风险、已知限制、非目标、假设和跨领域关注点只在用户要求时写，因为交付审核时才出现的讨论会被评审者驳回。接口限额、ADR 后果和测试报告的残余风险是已定事实，照写，不属于这里的「风险、已知限制」。

其余内容都是建议。项目有更好的写法时，按项目来。

## 两档
| 档 | 做什么 | 不做 |
|---|---|---|
| 轻量（默认） | 用全部写作规则和对应的写作指南。需要新调研时，自己读代码或派 1–3 个探索 subagent，笔记一行一条：`主题 \| 结论 \| 依据`；材料够就直接写。写完运行 doc-lint，按 `references/unslop.md`、`references/formatting.md`、`references/constraints-writing.md` 自查。有疑问直接在对话里问 | 不读 `references/orchestration.md`，不建 definition、brief、术语表和证据表，不派核查 agent |
| 完整 | 按 `references/orchestration.md` 五阶段编排 | — |

## 选档
按顺序取第一条命中的：
1. 用户本次明确要求某档时照做。说「轻量」走轻量；点名本 skill 要求写或定稿，或说「完整流程」「定稿」「终稿」，走完整。只认用户对你的要求，文档主题和引用里出现这些词不算。
2. 本会话已选过档时沿用。工作目录已有 `definition.md` 时按完整档继续，因为上下文压缩后会丢失档位。
3. 其余走轻量。拿不准时也走轻量，写完提示一句可以升完整档。

审查请求在轻量档运行 doc-lint 并自查文风；用户点明要核对的内容照做，可派 1 个 subagent 查。完整档跑三项核查。
从轻量升到完整时，已有笔记和正文接着用，做法见 `references/orchestration.md`。

## 读哪个文件
| 文件 | 谁读、何时读 |
|---|---|
| `references/orchestration.md` | 完整档的主 session 和 lead，开工前读 |
| `references/writing/product.md` | 写 PRD、需求评审稿的片段 |
| `references/writing/tech.md` | 写技术设计、ADR、原理说明的片段 |
| `references/writing/reference.md` | 写 API、函数、配置项参考的片段 |
| `references/writing/ops.md` | 写 Runbook、部署手册、操作步骤、复盘的片段 |
| `references/writing/test.md` | 写测试计划、用例、测试报告的片段 |
| `references/writing/marketing.md` | 写产品介绍、README 开头、发布说明、对比表的片段 |
| `references/formatting.md` | 写作 agent 动笔前读，文风核查 agent 逐条对照 |
| `references/review.md` | 写作前读；完整档的 lead 梳理时、需求与范围核查时读 |
| `references/constraints-writing.md` | 写作 agent 动笔前读 |
| `references/unslop.md` | 写作 agent 动笔前读，文风核查 agent 逐条核对 |

按负责的片段选择写作指南，因为一篇文档常含多种片段。

运行 doc-lint：

```bash
python3 '<技能包根目录>/scripts/doc-lint.py' '<文档路径>'
```

扫描结果是候选，逐条判断后再改。命中不等于违规，零命中也不等于合格。

## 边界
- 保存或覆盖用户的文件前先取得授权。没有授权时，只输出正文。
- 文档里写到的部署、迁移、删除操作只写不做，因为它们会改变外部状态。
- 数据、运行结果和界面截图只写真实取得的。拿不到时写明缺什么、从哪里补。
