<p>
  <img src="assets/doc-writer-logo.png" alt="doc-writer 黑白笔记本与笔标志" width="64" height="64">
</p>

# doc-writer

[English](README.md) | **简体中文**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

按项目证据编写和检查中文技术文档的 Agent Skill，覆盖 PRD、技术设计、API、ADR、README 等 12 类文档。

你给出材料和目标，助手选择文档类型和变体，读取对应规则，从代码、配置和运行记录核对事实，写出正文后逐项检查结构、证据和用词。本技能遵循 [Agent Skills](https://agentskills.io) 规范，能读取文件的 agent 都可以使用。只有你明确要求写或检查技术文档时它才会启用，改代码、日常问答不会触发；保存文件、执行文档里描述的操作、提交代码都需要你另外授权。

## 安装

把仓库克隆到你所用 agent 的技能目录，目录名保持 `doc-writer`（与 `SKILL.md` 中的 `name` 一致）。以 Claude Code 的项目级目录为例：

```bash
mkdir -p .claude/skills
git clone https://github.com/blankhoney/doc-writer.git .claude/skills/doc-writer
```

其他 agent 的技能目录位置见各自文档。安装后重新打开会话，确认 agent 能列出 `doc-writer`。

想在所有项目中使用，克隆到该 agent 的个人技能目录（Claude Code 为 `~/.claude/skills/doc-writer/`）。目录已存在时，先比较版本再更新，保留本地定制。

候选扫描器需要 Python 3.9 或更高版本，只用标准库。没有 Python 时，助手照常写作和检查，并在交付说明里注明扫描未执行。

## 快速开始

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

用自然语言描述任务即可，也可以在请求里直接写类型名。每种类型的变体和文风要求见[模板索引](templates/_index.md)。

## 它怎样保证质量

- **先读规则再动笔**：准备、取材、编写、验证各阶段读取对应的规则原文，选中的模板完整读取。
- **事实来自项目**：代码、配置、已有决策和运行记录分别支撑对应描述；缺的信息写成缺口，不编造。
- **结论先行**：决策类文档开头给出结论，章节之间按金字塔结构组织。
- **模型判断，脚本定位**：模型逐项检查范围、证据、术语和可操作性；扫描器只标出套话、空泛修饰词和中文格式的候选位置。
- **示例有出处**：模板附带的 8 段外部示例都固定了原始提交和许可证，只示范写法。

完整机制见[架构与优化方法](docs/guide/architecture.md)。

## 什么时候不适合用

- 你要写英文文档。规则、禁用词表和扫描器都针对中文。
- 你的 agent 不能读取本地文件。规则和模板都要按需读取原文。
- 你希望它写完后自动提交或发布。提交和发布需要你自己决定。

## 文档

| 文档 | 内容 |
|---|---|
| [使用文档入口](docs/guide/README.md) | 安装结构、首次使用和导航 |
| [使用指南](docs/guide/usage.md) | 提供材料、保存、修改原文、只检查不改写、单独运行扫描器 |
| [架构与优化方法](docs/guide/architecture.md) | 规则、模板、模型和扫描器的分工 |
| [模板扩展](docs/guide/templates.md) | 添加类型、变体或模块 |

## 贡献

欢迎提 issue 和 pull request。修改规则、模板或扫描器前请先读[贡献指南](CONTRIBUTING.md)，其中包括测试命令和示例登记要求。

## Star 趋势

<a href="https://www.star-history.com/#blankhoney/doc-writer&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=blankhoney/doc-writer&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=blankhoney/doc-writer&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=blankhoney/doc-writer&type=Date" />
  </picture>
</a>

## 许可证

本项目的代码、规则和文档采用 [MIT License](LICENSE)。Requests、Backstage、Django、Kubernetes enhancements、ripgrep 和 uv 的示例片段保留各自的许可证和署名；PEP 380 片段保留作者 Gregory Ewing 的公共领域声明。详见[来源记录](examples/SOURCES.md)和 [examples/licenses/](examples/licenses/)。
