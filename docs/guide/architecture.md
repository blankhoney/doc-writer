# 架构与写作方法

## 主 agent 只编排

主 session 定义文档、派 lead、读一行摘要、做取舍。每篇文档一个 lead，读代码、写正文、核查由 lead 派给 subagent，因为细节塞满主上下文后成稿质量会下降。每个阶段的产出写成文件，下一阶段只读文件。

## 六个阶段

| 阶段 | 产出 | 执行者 |
|---|---|---|
| 定义 | `definition.md` | 主 session |
| 研究 | `notes/<主题>.md`，每条附 `文件:行号`；`edges.md` 记发现的边界、竞争、风险和疑问 | lead 派 4–6 个并发 subagent |
| 解决 | `resolutions.md`：每条边界查清成事实或决定、删除，或记进 `questions.md`，交付时一次提问 | lead 派一个分诊 subagent |
| 梳理 | `brief.md`、`glossary.md`、产品梳理或架构与数据模型 | lead |
| 写作 | 文档正文 | 新上下文的写作 subagent，长文可按章节派多个，由 lead 合稿 |
| 核查 | `evidence/事实与一致.md`、`evidence/需求与范围.md`、`evidence/文风与排版.md` | 3 个并行的核查 agent，只写证据表不改文档；lead 按表统一修改 |

各阶段的提示模板见 `skills/doc-writer/references/orchestration.md`。

## 按片段类型选写作指南

一篇文档常含多种片段。写作 agent 只读自己负责的片段对应的指南，上下文里只有用得上的规则：

| 片段 | 指南 |
|---|---|
| PRD、需求评审稿 | `references/writing/product.md` |
| 技术设计、ADR、原理说明 | `references/writing/tech.md` |
| API、函数、配置项参考 | `references/writing/reference.md` |
| Runbook、部署手册、操作步骤、复盘 | `references/writing/ops.md` |
| 测试计划、用例、测试报告 | `references/writing/test.md` |
| 产品介绍、README 开头、发布说明 | `references/writing/marketing.md` |

所有片段另读 `references/formatting.md`（排版与结构）、`references/review.md`、`references/constraints-writing.md` 和 `references/unslop.md`。

## 解决、比例与呈现

`references/review.md` 规定解决、写作和核查共用的标准：重点审核项，每条边界和风险是否该现在决定，写多重（写成结论或删除），以及图的选用。段落、句长和图文比例见 `references/formatting.md`。

## G1 与 doc-lint

`references/constraints-writing.md` 的 G1 表列出禁用句式、修饰词和抽象大词。`scripts/doc-lint.py` 从 G1 读取词表，检查中文格式（标点、空格、括号），并给出排版候选（超长段落、正文加粗、句内罗列、首先其次串连、步骤非祈使句）。脚本只读，只标候选，语义判断由模型和人完成。

## unslop

`references/unslop.md` 补充 G1 之外靠人判断的写作毛病：说感受不说机制、同义词轮换、凑三、修辞腔等。写作 agent 动笔前读，文风与排版核查 agent 逐条核对。
