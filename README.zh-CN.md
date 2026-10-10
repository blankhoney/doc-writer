<p>
  <img src="docs/images/doc-writer-logo.png" alt="doc-writer 黑白笔记本与笔标志" width="64" height="64">
</p>

# doc-writer

[English](README.md) | **简体中文**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

按项目证据编写和检查中文技术文档的 Agent Skill，覆盖 PRD、技术设计、API、ADR、README 等 12 类文档。

你给出材料和目标，主 session 分五个阶段编排（定义、研究、梳理、写作、核查），每篇文档一个 lead，读代码、写正文和核查交给子 agent。每个阶段的产出写成文件，下一阶段只读文件。本技能遵循 [Agent Skills](https://agentskills.io) 规范，能读取文件的 agent 都可以使用。只有你明确要求写或检查技术文档时它才会启用，改代码、日常问答不会触发；保存文件、执行文档里描述的操作、提交代码都需要你另外授权。

## 安装

用 [skills](https://github.com/vercel-labs/skills) 命令行安装，它会识别你本机的 agent（Codex、Cursor、Gemini CLI、GitHub Copilot、Claude Code 等），把技能放进各自的技能目录：

```bash
npx skills add blankhoney/doc-writer        # 装到当前项目
npx skills add blankhoney/doc-writer -g     # 装到个人目录，所有项目可用
```

不用 Node 时，手动把仓库里的 `skills/doc-writer/` 目录复制到你所用 agent 的技能目录，目录名保持 `doc-writer`（与 `SKILL.md` 中的 `name` 一致）。各 agent 的技能目录位置见其文档。安装后重新打开会话，确认 agent 能列出 `doc-writer`。

doc-lint 需要 Python 3.9 或更高版本，只用标准库。没有 Python 时，助手照常写作和检查，并在交付说明里注明扫描未执行。

## 用法

在目标项目的会话中输入（支持斜杠命令的客户端也可以用 `/doc-writer` 开头）：

```text
用 doc-writer 根据以下材料，写一份给项目贡献者的代码提交流程指南，只在对话中输出：开发者创建功能分支并提交合并请求；合并请求需要说明改动目的；自动化测试通过且一名维护者审核通过后，由维护者合并。
```

你会得到一份按创建分支、提交请求、测试和审核组织的操作指南，文末注明"未保存文件，未运行候选脚本"。

需要保存时，在请求里写明路径：

```text
用 doc-writer 根据当前项目的 README.md，为新加入项目的工程师编写快速开始，保存到 docs/quickstart.md。
```

只检查、不改写：

```text
用 doc-writer 检查 docs/architecture.md 的结构、术语和实现描述，列出具体位置及修改建议，不修改文件。
```

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

用自然语言描述任务即可，也可以在请求里直接写类型名。一篇文档常含多种片段（README 开头是产品介绍，安装节是操作步骤），写作 agent 只读自己负责的片段对应的指南：`skills/doc-writer/references/writing/` 下的 `product`、`tech`、`reference`、`ops`、`test`、`marketing`。

## 它怎样保证质量

- **阶段产出成文件**：研究笔记每条附 `文件:行号`，术语表把多义词定义一次，新上下文的写作 agent 依据这些文件写作，而不是翻原始研究。
- **事实来自项目**：代码、配置、已有决策和运行记录分别支撑对应描述；缺的信息写成缺口，不编造。
- **三路核查**：三个不继承写作上下文的核查 agent 并行检查事实与一致、需求与范围（哪些决定下得太早、哪些内容写得太重），以及文风与排版（文字、表格和图是否平衡）；只写证据表，由 lead 统一修改。
- **模型判断，脚本定位**：doc-lint 按 G1 表标出套话、空泛修饰词和中文格式的候选位置，并标出超长段落、正文加粗等排版候选，由模型判断哪些属实；词表抓不到的毛病另有 unslop 清单。

完整机制见[架构与写作方法](docs/guide/architecture.md)，写作规则的来源见 [SOURCES.md](SOURCES.md)。

## 什么时候不适合用

- 你要写英文文档。规则、禁用词表和扫描器都针对中文。
- 你的 agent 不能读取本地文件。规则和写作指南都要按需读取原文。
- 你希望它写完后自动提交或发布。提交和发布需要你自己决定。

## 文档

| 文档 | 内容 |
|---|---|
| [使用文档入口](docs/guide/README.md) | 安装结构、首次使用和导航 |
| [使用指南](docs/guide/usage.md) | 提供材料、保存、修改原文、只检查不改写、单独运行 doc-lint |
| [架构与写作方法](docs/guide/architecture.md) | 五个阶段、写作指南、核查，以及模型与 doc-lint 的分工 |

## 贡献

欢迎提 issue 和 pull request。修改规则、写作指南或扫描器前请先读[贡献指南](CONTRIBUTING.md)，其中包括测试命令和 doc-lint 用法。

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
