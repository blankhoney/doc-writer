# doc-writer 使用文档

doc-writer 是遵循 Agent Skills 规范的写作技能，按项目的真实实现编写、补全和审查中文文档。它由主 session 分六个阶段编排，每篇文档一个 lead，lead 派 subagent 读代码、写作和核查。

## 快速上手

1. 把仓库里的 `skills/doc-writer/` 整个复制到 agent 的技能目录，目录名保持 `doc-writer`；或运行 `npx skills add blankhoney/doc-writer`。
2. 重新打开会话，确认 agent 能列出 `doc-writer`。
3. 在项目会话中提出写作请求，例如：

   ```text
   用 doc-writer 根据当前项目的代码，为评审者写一份调度器的技术设计，保存到 docs/scheduler-design.md。
   ```

你会得到一篇文档，以及三五行交付说明：写了什么、依据哪些代码、删减了什么、还有哪些没核对。

## 安装结构

```text
doc-writer/
├── SKILL.md
├── LICENSE
├── scripts/doc-lint.py
└── references/
    ├── orchestration.md
    ├── formatting.md
    ├── review.md
    ├── constraints-writing.md
    ├── unslop.md
    └── writing/{product,tech,reference,ops,test,marketing}.md
```

仓库根目录的 `tests/`、`evals/`、`docs/` 供维护使用，不需要安装。

## 继续阅读

| 你要做什么 | 阅读入口 |
|---|---|
| 提供材料、保存、修改已有文档、只审查不改写、单独运行 doc-lint | [使用指南](usage.md) |
| 了解六个阶段、写作指南、核查和 doc-lint 的分工 | [架构与写作方法](architecture.md) |
| 修改 skill 本身 | [贡献指南](../../CONTRIBUTING.md) |
