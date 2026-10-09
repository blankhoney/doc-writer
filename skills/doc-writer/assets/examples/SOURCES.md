# 示例来源与使用范围

本包收录 8 段外部示例的中文节译，另有若干本仓库原创的构造示意。示例只示范写法，不是目标项目事实，也不覆盖本包规则。

## 材料与使用范围

| 材料 | 性质 | 只示范什么 |
|---|---|---|
| Changelog 模板（`assets/templates/changelog.md`）的 Requests 2.31.0 条目 | 非官方翻译＋格式改编 | Security 条目的影响范围与用户行动；历史版本，不是升级建议 |
| ADR 模板（`assets/templates/adr.md`）的 Backstage ADR003 片段 | 非官方节译 | 理由摘要与决策句，不是完整 ADR |
| How-to 模板（`assets/templates/how-to.md`）的 Django CSV 片段 | 非官方节译＋格式转换 | 任务前提与完整实现片段 |
| 技术设计模板（`assets/templates/tech-design.md`）的备忘与长片段、How-to 模板的扫描操作 | 本仓库源码改编，MIT | 深度与操作组织；不是运行记录 |
| Reference 模板（`assets/templates/reference.md`）的 JSON | 构造示意，MIT | 排版与语法 |
| `tech-design/kep-753.md`、`tech-design/kep-1287-cri.md`、`tech-design/pep-380.md` | 非官方节译 | 完整子节、步骤顺序与前提、局部接口契约 |
| `tech-design/implementation-sketch.md` | 构造示意，MIT | 结构、拟议文件、契约与验证的对应 |
| `readme/ripgrep.md`、`readme/uv-install.md` | 非官方节译 | 首段定义、"何时不该用"、安装节 |

源码改编依据本包的 [doc-lint.py](../../scripts/doc-lint.py)，扫描操作样本以 `SKILL.md` 为扫描对象，均未实际执行。本包原创内容采用 [MIT 许可证](../../LICENSE)；第三方片段继续受其原许可约束，所需许可证和 NOTICE 放在 `licenses/`。

## Requests 2.31.0

- **来源**：[HISTORY.md 第 9–33 行](https://github.com/psf/requests/blob/147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4/HISTORY.md#L9-L33)，v2.31.0，2023-05-22。
- **改动**：翻译；版本标题改成 `## [版本] - 日期`，分类改为 `### Security`，示例 URL 加行内代码。未新增迁移建议。
- **许可**：Apache-2.0，Copyright 2019 Kenneth Reitz。附[许可证](licenses/requests-LICENSE.txt)和 [NOTICE](licenses/requests-NOTICE.txt)。

## Backstage ADR003

- **来源**：The Backstage Authors，[ADR003 第 28–51 行](https://github.com/backstage/backstage/blob/1134d4b38c40583cdcd00637a7c29de02351f9d8/docs/architecture-decisions/adr003-avoid-default-exports.md#L28-L51)。
- **改动**：节译理由摘要、具名导出的收益和决策句；省略历史背景、替代代码与迁移动作。原文没有状态和决策日期，不补写。
- **许可**：Apache-2.0，Copyright 2020 The Backstage Authors。附[许可证](licenses/backstage-LICENSE.txt)和 [NOTICE](licenses/backstage-NOTICE.txt)。

## Django CSV

- **来源**：Django Software Foundation and individual contributors，[How to create CSV output 第 9–33 行](https://github.com/django/django/blob/9e7cc2b628fe8fd3895986af9b7fc9525034c1b0/docs/howto/outputting-csv.txt#L9-L33)，Django 5.2。
- **改动**：说明译为中文，reStructuredText 转 Markdown；代码、英文注释和示例数据不改，只去掉外层缩进。未运行 Django。
- **许可**：BSD-3-Clause，附[许可证](licenses/django-LICENSE.txt)；不得用 Django 或贡献者名称作背书。

## KEP-753

- **来源**：[KEP-753: Sidecar containers](https://github.com/kubernetes/enhancements/blob/fc09a26d4236305d3f282377ca92bdfb2b1fb03c/keps/sig-node/753-sidecar-containers/README.md) 第 453–471、935–953、1012–1014 行。
- **改动**：节译选定片段；未收 Alpha/Beta 历史方案、伪代码和第 472–504 行未完成条目。
- **许可**：Apache-2.0，附[许可证](licenses/kubernetes-enhancements-LICENSE.txt)，与 KEP-1287 共用。

## PEP 380

- **来源**：Gregory Ewing，[PEP 380](https://github.com/python/peps/blob/b39aefe6614b4e8a925d07c4b3ed47e147236dbe/peps/pep-0380.rst) 第 124–196 行 Formal Semantics。
- **改动**：节译；代码语义不改，只去掉字面块外层缩进。
- **许可**：原文声明 public domain，附[声明与作者信息](licenses/pep-380-public-domain.txt)。

## KEP-1287

- **来源**：[KEP-1287: In-place Update of Pod Resources](https://github.com/kubernetes/enhancements/blob/d47a8df46c8c26d6300fd30047520e397127805c/keps/sig-node/1287-in-place-update-pod-resources/README.md) 第 360–413 行 CRI Changes。
- **改动**：节译 CRI 契约部分；原文笔误 "may rely need" 按"可能需要"译出。
- **许可**：Apache-2.0，与 KEP-753 共用[许可证](licenses/kubernetes-enhancements-LICENSE.txt)。

## ripgrep README

- **来源**：Andrew Gallant，[ripgrep README](https://github.com/BurntSushi/ripgrep/blob/3fce3b5bb0236da2df6d99672afb8a719642eca7/README.md) 第 1–9 行与第 161–182 行。
- **改动**：节译；省略徽章、截图、对比示例与"为什么用"清单。
- **许可**：Unlicense 或 MIT，本包按 MIT 使用，附[许可证](licenses/ripgrep-LICENSE-MIT.txt)。

## uv README

- **来源**：Astral Software Inc.，[uv README](https://github.com/astral-sh/uv/blob/46b84fd0bfec23b72f29e8e2185ba68a65052f48/README.md) 第 44–77 行 Installation。
- **改动**：说明译为中文，命令和代码块注释保持原样。
- **许可**：Apache-2.0 或 MIT，本包按 MIT 使用，附[许可证](licenses/uv-LICENSE-MIT.txt)。

## 新增示例

登记来源（作者、链接、行号）、改动方式和许可；许可要求随附许可证或 NOTICE 的，放进 `licenses/`。许可不允许翻译或再分发的材料不收录。
