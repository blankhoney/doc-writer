<div align="center">

<img src="docs/images/doc-writer-logo.png" alt="doc-writer 黑白笔记本与笔标志" width="96" height="96">

# doc-writer

**依据项目真实实现编写和审查中文正式文档的 Agent Skill**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/version-4.0-green?style=flat-square)](skills/doc-writer/SKILL.md)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-8A2BE2?style=flat-square)](https://agentskills.io)
[![Works with](https://img.shields.io/badge/works%20with-Claude%20Code%20%7C%20Codex%20%7C%20Cursor-orange?style=flat-square)](#安装)
[![GitHub stars](https://img.shields.io/github/stars/blankhoney/doc-writer?style=flat-square)](https://github.com/blankhoney/doc-writer/stargazers)

[English](README.md) · **简体中文**

[安装](#安装) · [用法](#用法) · [能写什么](#能写哪些文档) · [工作方式](#完整档怎样工作) · [文档](#文档)

</div>

---

doc-writer 让 agent 先读代码、配置和已有决策，再写 PRD、技术设计、API、ADR、Runbook、测试报告、README 等 12 类文档。写完用 doc-lint 扫描套话和排版问题，由模型逐条判断。

它遵循 [Agent Skills](https://agentskills.io) 规范，Claude Code、Codex 等能读文件的 agent 都能用。

| 特点 | 说明 |
|---|---|
| 事实来自项目 | 代码、配置、已有决策和运行记录支撑对应描述；缺的信息写成占位，并在对话里告诉你缺什么 |
| 按文档类型写 | 产品、技术、参考、运维、测试、营销六份写作指南，各有标准章节和反模式 |
| 两档 | 默认轻量档自己写、自己查；完整档由主 session 编排研究、写作和三项核查 |
| 只在该用时启用 | 写调研笔记、会话交接、待办、注释、提交说明和日常问答时不启用 |

## 安装

用 [skills](https://github.com/vercel-labs/skills) 命令行安装。它会识别本机的 agent（Codex、Cursor、Gemini CLI、GitHub Copilot、Claude Code 等），把技能放进各自的技能目录：

```bash
npx skills add blankhoney/doc-writer        # 装到当前项目
npx skills add blankhoney/doc-writer -g     # 装到个人目录，所有项目可用
```

不用 Node 时，把仓库里的 `skills/doc-writer/` 复制到 agent 的技能目录，目录名保持 `doc-writer`（与 `SKILL.md` 的 `name` 一致）。技能目录位置见各 agent 的文档。

装好后开一个新会话，确认 agent 能列出 `doc-writer`。已经加载过旧版本的会话可能继续使用旧内容，更新后也要开新会话。

doc-lint 需要 Python 3.9 或更高版本，只用标准库。没有 Python 时照常写作和检查，交付说明里会注明扫描未执行。

## 用法

在目标项目的会话里直接描述要写的文档。支持斜杠命令的客户端也可以用 `/doc-writer` 开头。

```text
用 doc-writer 轻量写：根据当前项目的 README.md，为新加入项目的工程师编写快速开始，保存到 docs/quickstart.md。
```

请求里写了路径才会保存；没写时只在对话里输出正文。

<details>
<summary>更多示例请求</summary>

只在对话里输出：

```text
用 doc-writer 轻量写：根据以下材料，写一份给项目贡献者的代码提交流程指南，只在对话中输出：开发者创建功能分支并提交合并请求；合并请求需要说明改动目的；自动化测试通过且一名维护者审核通过后，由维护者合并。
```

只检查、不改写（完整档，三项独立核查；只想快速查文风就加「轻量」）：

```text
用 doc-writer 检查 docs/architecture.md 的结构、术语和实现描述，列出具体位置及修改建议，不修改文件。
```

</details>

### 两档

| 档 | 何时进入 | 做什么 |
|---|---|---|
| 轻量（默认） | 助手自行调用，或你说「轻量」 | 读通用规则和对应类型的写作指南；涉及代码行为时先读代码；写完按图文比例和文风自查，运行 doc-lint。有疑问直接在对话里问 |
| 完整 | 你点名 doc-writer（或输入 `/doc-writer`）要它写、检查或定稿，或说「完整流程」「定稿」「终稿」 | 五阶段编排和三项独立核查 |

只点名写 README、发布说明这类短文档时，仍走轻量。

档位在本次会话内保持，直到你切换。可以先用轻量讨论设计，定了再切完整；轻量档的笔记和初稿会接着用。

### 什么时候启用

| 会启用 | 不会启用 |
|---|---|
| 写或补全 PRD、技术设计、ADR、API、Runbook、测试计划与报告、产品介绍、README、发布说明 | 任务已给定格式、模板，或指定了其他 skill |
| 审查已有的这类文档 | 调研笔记、卡片、日常工作记录、会话交接、状态和待办 |
| 写交给你或评审者审阅的方案 | 改代码、写注释和提交说明；在对话里回答问题 |

点名本技能时，右栏的情况也照用。

## 能写哪些文档

| 任务 | 文档类型 |
|---|---|
| 明确功能目标与验收条件 | PRD |
| 设计方案并说明取舍 | 技术设计（架构方案或程序详细设计） |
| 说明接口调用方式 | API 文档 |
| 说明版本变更对使用者的影响 | Changelog |
| 汇报测试结果或安排测试 | 测试报告 |
| 编写部署和值班操作 | 部署／Runbook |
| 记录已有决策 | ADR |
| 引导学习或完成具体任务 | Tutorial、How-to |
| 查询契约或理解机制 | Reference、Explanation |
| 写仓库首页 | README |

一篇文档常含多种片段：README 开头是产品介绍，安装一节是操作步骤。写作时按片段选指南，指南在 `skills/doc-writer/references/writing/` 下，分为 `product`、`tech`、`reference`、`ops`、`test`、`marketing` 六份。

## 完整档怎样工作

主 session 兼任 lead，负责定义、梳理和统筹修改；读代码、写正文和核查交给子 agent。每个阶段的产出写成文件，下一阶段只读文件，所以长文档不会挤满主 session 的上下文。

```mermaid
flowchart LR
    A[定义<br/>目的、读者、问题] --> B[研究<br/>子 agent 读代码写笔记]
    B --> C[梳理<br/>处理冲突，写 brief 和术语表]
    C --> D[写作<br/>新上下文按大纲写正文]
    D --> E[核查<br/>三个 agent 并行]
    E -->|证据表| F[主 session 汇总修改]
```

1. **定义**：写下目的、读者、要回答的问题、范围，并逐条保存你的原话。
2. **研究**：子 agent 读代码，按主题写笔记，记录调用链、存储、默认值、失败分支和例子，附 `文件:行号`。
3. **梳理**：核实大纲引用的冲突和推断，写 brief 和术语表，多义词只定义一次。
4. **写作**：新上下文的写作 agent 只读自己章节引用的笔记，写某个机制前回源码核对。
5. **核查**：三个不继承写作上下文的 agent 并行检查事实与一致、需求与范围、文风与排版，只写证据表；主 session 汇总后修改，一处改动同步到表、图和示例里的所有出现位置。

<details>
<summary>模型与 doc-lint 怎样分工</summary>

doc-lint 按 G1 表标出套话、空泛修饰词和中文格式问题，还标出超长段落、正文加粗等排版候选。它只给候选位置，哪些属实由模型判断：命中不等于违规，零命中也不等于合格。词表抓不到的写作习惯，由 unslop 清单覆盖。

完整机制见[架构与写作方法](docs/guide/architecture.md)，写作规则的来源见 [SOURCES.md](SOURCES.md)。

</details>

## 什么时候不适合用

- 你要写英文文档。规则、禁用词表和扫描器都针对中文。
- 你的 agent 不能读本地文件。规则和写作指南都要按需读原文。
- 你希望它写完自动提交或发布。保存文件、执行文档里的部署操作和提交代码，都要你另外授权。

## 文档

| 文档 | 内容 |
|---|---|
| [使用文档入口](docs/guide/README.md) | 安装结构、首次使用和导航 |
| [使用指南](docs/guide/usage.md) | 提供材料、保存、修改原文、只检查不改写、单独运行 doc-lint |
| [架构与写作方法](docs/guide/architecture.md) | 五个阶段、写作指南、核查，以及模型与 doc-lint 的分工 |

## 贡献

欢迎提 issue 和 pull request。改规则、写作指南或扫描器前先读[贡献指南](CONTRIBUTING.md)，里面有测试命令和 doc-lint 用法。

## Star 趋势

<a href="https://www.star-history.com/#blankhoney/doc-writer&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=blankhoney/doc-writer&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=blankhoney/doc-writer&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=blankhoney/doc-writer&type=Date" />
  </picture>
</a>

## 许可证

本项目的代码、规则和文档采用 [MIT License](LICENSE)。unslop 清单改写自 unslop（Lauren Tan，MIT），详见 [SOURCES.md](SOURCES.md)。
