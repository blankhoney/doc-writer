---
name: doc-writer
description: >-
  编写、补全和审查中文文档：PRD 与需求评审稿、技术设计、ADR、API 与参考文档、
  Runbook 与部署手册、测试计划与报告、产品介绍、README、发布说明。
  用户明确要求写、改或检查这类文档时使用；改代码、写提交说明、日常问答不用。
  小任务直接处理；复杂任务由主 agent 编排研究、写作和核查。
license: MIT
compatibility: 适用于能读写文件的 agent；能派子 agent 或用命令行调用其他模型时效果最好。doc-lint 需要 Python 3.9+。
metadata:
  author: blankhoney
  version: "3.4"
---

# 文档写作
依据项目的真实实现写文档，让读者能照着使用。

技能包根目录是本文件所在目录，下文路径都相对这个目录。

## 五条硬性要求
1. 按下节选择流程；需要编排时，执行 `references/orchestration.md`。
2. 按 `references/orchestration.md` 的术语表规则用词。
3. 正文遵守 `references/constraints-writing.md` 的 G1 表和 `references/formatting.md` 的排版硬线，交付前运行 doc-lint。
4. 编排任务交付前执行 `references/orchestration.md` 的核查规则。
5. 正文只用已查证或用户已确认的结论。未解决的问题不进文档，用户要求时除外。风险、已知限制、非目标、假设和跨领域关注点只在用户要求时写，因为交付审核时才出现的讨论会被评审者驳回。接口限额、ADR 后果和测试报告的残余风险是已定事实，照写，不属于这里的「风险、已知限制」。

其余内容都是建议。项目有更好的写法时，按项目来。

## 选择流程
只改一节、补几句或修正个别事实时，直接查证、写、跑 doc-lint，因为小任务无需编排。
其余任务按五阶段执行，见 `references/orchestration.md`。

## 读哪个文件
| 文件 | 谁读、何时读 |
|---|---|
| `references/orchestration.md` | 主 session 和 lead，编排任务开工前读 |
| `references/writing/product.md` | 写 PRD、需求评审稿的片段 |
| `references/writing/tech.md` | 写技术设计、ADR、原理说明的片段 |
| `references/writing/reference.md` | 写 API、函数、配置项参考的片段 |
| `references/writing/ops.md` | 写 Runbook、部署手册、操作步骤、复盘的片段 |
| `references/writing/test.md` | 写测试计划、用例、测试报告的片段 |
| `references/writing/marketing.md` | 写产品介绍、README 开头、发布说明、对比表的片段 |
| `references/formatting.md` | 写作 agent 动笔前读，文风核查 agent 逐条对照 |
| `references/review.md` | lead 梳理时读，写作 agent 动笔前读，需求与范围核查 agent 审查时读 |
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
