# 架构与写作方法

## 主 agent 只编排

主 agent 定义文档、派发任务、读一行摘要、做取舍。读代码、写正文、审查交给子 agent，因为细节塞满主上下文后成稿质量会下降。每个阶段的产出写成文件，下一阶段只读文件。

## 六个阶段

| 阶段 | 产出 | 执行者 |
|---|---|---|
| 定义 | `definition.md` | 主 agent |
| 研究 | `notes/<主题>.md`，每条附 `文件:行号` | 4–6 个并发子 agent |
| 梳理 | `brief.md`、`glossary.md`、产品梳理或架构与数据模型 | 新子 agent |
| 写作 | 文档正文 | 新上下文的写作 agent，长文可分章节派多个 lead |
| 审查 | `review-table.md` | 不继承写作上下文的审核 agent |
| 对齐 | `align-report.md` | 新子 agent |

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

## 范围与比例审查

`references/review.md` 规定写作和审查共用的标准：重点审核项，每条风险和建议是否该现在决定，写多重（保留、降为已知限制、删除），图表的选用，图文平衡，段落和句子长度。

## G1 与 doc-lint

`references/constraints-writing.md` 的 G1 表列出禁用句式、修饰词和抽象大词。`scripts/doc-lint.py` 从 G1 读取词表，并检查中文格式（标点、空格、括号）。脚本只读，只标候选，语义判断由模型和人完成。

## unslop

`references/unslop.md` 补充 G1 之外靠人判断的写作毛病：说感受不说机制、同义词轮换、凑三、修辞腔等。写作 agent 动笔前读，对齐 agent 逐条核对。
