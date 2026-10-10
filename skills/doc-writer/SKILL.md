---
name: doc-writer
description: >-
  编写、补全和审查中文文档：PRD 与需求评审稿、技术设计、ADR、API 与参考文档、
  Runbook 与部署手册、测试计划与报告、产品介绍、README、发布说明。
  用户明确要求写、改或检查这类文档时使用；改代码、写提交说明、日常问答不用。
  主 agent 分阶段编排，派子 agent 研究代码与资料、写作、审查和对齐。
license: MIT
compatibility: 适用于能读写文件的 agent；能派子 agent 或用命令行调用其他模型时效果最好。doc-lint 需要 Python 3.9+。
metadata:
  author: blankhoney
  version: "3.0"
---

# 文档写作
本 skill 帮你依据项目的真实实现，写出读者拿来就能用的文档。
主 agent 只做编排：定义文档、派发任务、汇总一行摘要、做取舍。
读代码、查资料、写正文、审查交给子 agent，因为细节塞满主上下文后，成稿质量会下降。

技能包根目录是本文件所在目录，下文路径都相对这个目录。

## 四条硬性要求
1. 按六个阶段编排，每个阶段的产出写成文件，下一阶段只读文件。
2. 术语一致：每个多义词在术语表里定义一次，全文只用一个名字。
3. 正文遵守 `references/constraints-writing.md` 的 G1 表，交付前运行 doc-lint。
4. 交付前做范围与比例审查，标准见 `references/review.md`。

其余内容都是建议。项目有更好的写法时，按项目来。

## 六个阶段
各阶段交接的文件和子 agent 提示见 `references/orchestration.md`。

1. **定义**：写清文档做什么、给谁看、回答哪些问题、范围多大。简单请求默认写一篇，因为多篇文档容易互相矛盾。
2. **研究**：并发派 4–6 个子 agent 读代码和资料，笔记每条附 `文件:行号`。产品类先研究用户、场景和痛点，再看代码。
3. **梳理**：派新子 agent 写 brief 和术语表。产品类再出产品梳理，技术类再出架构与数据模型。
4. **写作**：派新上下文的写作 agent，只读梳理材料和对应的写作指南。长文可按章节派多个 lead，lead 可再派小子 agent 补研。
5. **审查**：派不继承写作上下文的审核 agent，做范围与比例审查，直接改文档。
6. **对齐**：派新子 agent 核对术语、名称、事实与代码一致，多篇之间无矛盾，再运行 doc-lint。

## 读哪个文件
| 文件 | 谁读、何时读 |
|---|---|
| `references/orchestration.md` | 主 agent，开工前读一次 |
| `references/writing/product.md` | 写 PRD、需求评审稿的片段 |
| `references/writing/tech.md` | 写技术设计、ADR、原理说明的片段 |
| `references/writing/reference.md` | 写 API、函数、配置项参考的片段 |
| `references/writing/ops.md` | 写 Runbook、部署手册、操作步骤、复盘的片段 |
| `references/writing/test.md` | 写测试计划、用例、测试报告的片段 |
| `references/writing/marketing.md` | 写产品介绍、README 开头、发布说明、对比表的片段 |
| `references/review.md` | 写作 agent 和审核 agent 都读 |
| `references/constraints-writing.md` | 写作 agent 动笔前读 |
| `references/unslop.md` | 写作 agent 动笔前读，对齐 agent 逐条核对 |

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
