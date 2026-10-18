---
name: doc-writer
description: >-
  编写、补全和审查中文文档：PRD 与需求评审稿、技术设计与设计方案、ADR、API 与参考文档、
  Runbook 与部署手册、测试计划与报告、产品介绍、README、发布说明。
  写、改或检查这类文档时使用，包括交给用户或评审者审阅的方案；
  改代码、写提交说明、日常问答、内部工作笔记和交接记录，以及任务已指定其他格式或 skill 的文档不用。
  默认轻量档：按文档类型读写作指南和排版规则，写完自查；用户点名本 skill 要求写、检查或定稿，
  或要求定稿、完整流程时，由主 agent 编排研究、写作和核查。
license: MIT
compatibility: 适用于能读写文件的 agent；能派子 agent 或用命令行调用其他模型时效果最好。doc-lint 需要 Python 3.9+。
metadata:
  author: blankhoney
  version: "3.8"
---

# 文档写作
依据项目的真实实现写文档，让读者能照着使用。

技能包根目录是本文件所在目录，下文路径都相对这个目录。

## 四条硬性要求
1. 先按「选档」定档。完整档按 `references/orchestration.md` 编排，并在交付前执行其中的核查。
2. 术语一致：每个多义词只定义一次，同一个词只指一个对象，指多个对象时各起限定名；同一动作不换近义词，写清它的触发者、前置状态和结果状态。状态、字段、错误名在正文、表格和图里写法一致，首次出现写中文名和代码值。完整档另建术语表，见 `references/orchestration.md`。
3. 正文遵守 `references/constraints-writing.md` 的 G1 表和 `references/formatting.md` 的排版硬线，交付前运行 doc-lint。
4. 正文只用已查证或用户已确认的结论。未解决的问题不进文档，用户要求时除外。风险、已知限制、非目标、假设和跨领域关注点只在用户要求时写，因为交付审核时才出现的讨论会被评审者驳回。接口限额、ADR 后果和测试报告的残余风险是已定事实，照写，不属于这里的「风险、已知限制」。

其余内容都是建议。项目有更好的写法时，按项目来。

## 两档
| 档 | 做什么 | 不做 |
|---|---|---|
| 轻量（默认） | 按下方「轻量档步骤」做 | 不读 `references/orchestration.md`，不建 definition、brief、术语表和证据表，不派核查 agent |
| 完整 | 按 `references/orchestration.md` 五阶段编排 | — |

轻量档步骤：
1. 想清目的、读者和要回答的问题，默认写一篇。
2. 读完 `references/formatting.md`、`references/constraints-writing.md`、`references/unslop.md`，以及「读哪个文件」表中你要写的每类片段的写作指南，再动笔，因为只读通用规则会漏掉该类文档的章节和要点。
3. 写到代码行为、手上又没有覆盖它的笔记或材料时，先读代码再写：自己读或派 1–3 个探索 subagent，按 `references/notes.md` 把笔记写进工作目录。
4. 写完按 `references/formatting.md` 的「图文比例」逐条核对该画的图，按 `references/unslop.md`、`references/constraints-writing.md` 自查，对照「边界」。
5. 按主要读者的任务把文档过一遍，补上会卡住、会读错的地方。
6. 运行 doc-lint，之后每次修改正文都重跑。
7. 有疑问直接在对话里问。写完整篇文档时，结尾提示一句可以升完整档。

## 选档
按顺序取第一条命中的：
1. 用户本次明确要求某档时照做。说「轻量」走轻量；点名本 skill（含 `/doc-writer`）要求写、检查或定稿，或说「完整流程」「定稿」「终稿」，走完整。只认用户对你的要求，文档主题和引用里出现这些词不算。
2. 本会话已选过档时沿用。上下文压缩后档位不明时，工作目录已有 `definition.md` 就按完整档继续。
3. 其余走轻量。

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
| `references/notes.md` | 做调研、写笔记的 agent 动笔前读 |
| `references/constraints-writing.md` | 写作 agent 动笔前读 |
| `references/unslop.md` | 写作 agent 动笔前读，文风核查 agent 逐条核对 |

按负责的片段选择写作指南，因为一篇文档常含多种片段。派 subagent 时给技能包根目录，让它读本表后自选文件，不在提示里抄文件名，因为本 skill 更新后旧文件名会失效。

运行 doc-lint：

```bash
python3 '<技能包根目录>/scripts/doc-lint.py' '<文档路径>'
```

扫描结果是候选，逐条判断后再改。命中不等于违规，零命中也不等于合格。

## 边界
- 保存或覆盖用户的文件前先取得授权。没有授权时，只输出正文。
- 文档里写到的部署、迁移、删除操作只写不做，因为它们会改变外部状态。
- 数据、运行结果和界面截图只写真实取得的。拿不到时在该处留占位，如「待补截图」，缺什么、从哪里补在对话里告诉用户；结论取决于缺失的数据时，结论写无法判断，并用一句话说明缺什么。不另写说明缺口的段落。
- 性能、容量和成本数字附来源：实测写环境和时间，估算写参数和推导，因为读者会把估算当成实测。默认值、配置值和契约值直接写。
- 先分清文档写的是当前实现、历史还是目标设计，按对应时点的代码、记录或已定设计取依据。不把目标设计或历史记录改成当前实现。
- 改已有文档时先读完原文，保留与本次任务无关的内容，沿用原有语言和格式；本次写的部分仍遵守硬性要求 3。
