---
type: adr
category: engineering
default_variant: nygard
---

# ADR
> 记录一个决策的背景、选择和后果，让后人知道"为什么是这样"而不用重新讨论。

> **示例使用范围**：Nygard 变体保留已核验的 Backstage 局部节译，只示范理由与决策写法，不是目标项目事实。见[来源说明](../examples/SOURCES.md)。

## 变体选择

```
记录的是什么？
  ├─ 单个架构决策（快速记录）       → 决策日志
  ├─ 单个架构决策（标准格式）       → Nygard ADR（默认）
  ├─ 单个架构决策（逐项比较备选方案） → MADR
  └─ 单个决策只需一句话记录         → Y-statement
```

---

## 变体 A: 决策日志

轻量 ADR。一条决策一行或一段，适合在项目初期快速积累决策记录。可后续升级为 Nygard ADR。

### 必需内容

| 必需内容 | 本节回答 | 排版 |
|--------|------|------|
| 决策表 | 做了什么决定？为什么？有什么后果？ | 契约表 |

表结构：`| 编号 | 日期 | 状态 | 决策 | 理由 | 后果 |`

### 按需模块

无——决策日志不插入模块。需要更多细节时升级为 Nygard ADR。

---

## 变体 B: Nygard ADR

标准 ADR 格式（Michael Nygard 2011 原文格式）。一篇一事，Accepted 后不改——决策变更时开新 ADR 并标注 Superseded。

### 必需内容

| 必需内容 | 本节回答 | 排版 |
|--------|------|------|
| 标题 | 编号 + 短名词短语，点明决策对象，如"ADR 9：多租户集成使用 LDAP" | — |
| 状态 | 当前状态（Proposed / Accepted / Deprecated / Superseded by ADR-xxx） | — |
| 背景（Context） | 哪些技术、组织和项目因素促成这个决策？ | 中性陈述各方因素，不提前写选择和后果 |
| 决策（Decision） | 决定了什么？用完整句、主动语态写，如"我们将……" | 倒金字塔 |
| 后果（Consequences） | 决策落地后的新情况：正面、负面和中性后果都列出 | 无序列表，每条标明正面／负面／中性 |

### 按需模块

| 模块名 | 本节回答 | 排版 | 格式规范 | 保留条件 |
|--------|------|------|----------|-----------|
| 备选方案 | 还考虑了什么？为什么没选？（不是 Nygard 原节） | 契约表 | 列：方案、优势、劣势、淘汰原因；只列现实候选 | 候选真实且有淘汰依据即可保留，不要求至少一个维度更优；纯为凑数或与决策无关时删除 |
| 参与者 | 谁参与了决策？ | 无序列表 | 姓名 + 角色 | 材料中有则插入 |
| 置信度 | 决策把握有多大？ | 一句话 | 高／中／低 + 依据 | 低置信度决策写明，便于日后重审 |

### 示例（已核验局部：Backstage ADR003）

> **非官方中文节译，2026-09-06**：节选自 The Backstage Authors 的 [ADR003 第 28–51 行](https://github.com/backstage/backstage/blob/1134d4b38c40583cdcd00637a7c29de02351f9d8/docs/architecture-decisions/adr003-avoid-default-exports.md#L28-L51)，翻译正文并补出节选标题；省略历史背景、替代代码和迁移动作。保留原有理由、决策与例外，不新增事实。Copyright 2020 The Backstage Authors；[Apache-2.0 全文](../examples/licenses/backstage-LICENSE.txt)与[原 NOTICE](../examples/licenses/backstage-NOTICE.txt)随包保留。见[核验记录](../examples/SOURCES.md#backstage-adr003)。

只模仿“具体理由 → 决策 → 例外”的写法。原文未标 Accepted 或决策日期，后果也未区分正负，因此本片段**不是完整 Nygard ADR 合格样本**；实际任务仍须按上方必需内容记录目标项目的真实状态和后果，不得用仓库提交日期补造决策日期。

````markdown
# ADR003：避免默认导出，优先使用具名导出

## 背景（节选）

避免默认导出的理由：
- 鼓励为模块另取本地名称，增加理解成本，例如
  `import TheListThing from 'not-a-list-thing';`。
- 妨碍 IDE 自动重命名和重构代码。
- 导入成员的名称完全由使用方定义，容易产生拼写错误。
- CommonJS 互操作时需要使用方手工指定 default 属性；Babel 经常隐藏这层处理。
- 重新导出时会出现名称冲突，迫使开发者逐个手工命名。

具名导出减少符号重命名，便于：
- 使用 IDE 的 Find All References 和 Go To Definition。
- 通过唯一符号名搜索代码库，例如使用 grep。

## 决策（节选）

停止使用默认导出，除非绝对必要，例如 React.lazy 模块。
````

---

## 变体 C: MADR

Markdown ADR（MADR 4.0）。在 Nygard 基础上逐项列出备选方案及其利弊，适合需要展示比较过程的决策。节名为 MADR 4.0 的中文译名，括注原名；节的顺序为：背景与问题 / 决策驱动因素 / 备选方案 / 决策结果 / 各方案利弊 / 更多信息。

### 必需内容

| 必需内容 | 本节回答 | 排版 |
|--------|------|------|
| 标题 | 编号 + 短标题，写明所解决的问题和所选方案 | — |
| 元数据（front matter） | status（Proposed / Accepted / Deprecated / Superseded；MADR 中为可选，本包要求填写）；date、decision-makers、consulted、informed 按需，它们是元数据不是章节 | — |
| 背景（Context and Problem Statement） | 什么问题需要决策？背景是什么？ | 陈述问题与背景，不提前写选择和后果 |
| 备选方案（Considered Options） | 考虑了哪些方案？ | 无序列表 |
| 决策结果（Decision Outcome） | 选了哪个方案？因为什么？ | 倒金字塔："选择 X，因为……"；选用后果、确认时作为其下的小节 |

### 按需模块

| 模块名 | 本节回答 | 排版 | 格式规范 | 保留条件 |
|--------|------|------|----------|-----------|
| 决策驱动因素（Decision Drivers） | 哪些因素影响了选择？ | 无序列表 | 每条一个驱动因素 | 每条至少影响一个方案的取舍 |
| 后果（Consequences，决策结果下） | 决策带来哪些好处和坏处？ | 无序列表 | "好处，因为……"／"坏处，因为……" | 本包要求填写：至少一条负面后果，或说明为何没有 |
| 确认（Confirmation，决策结果下） | 怎么确认实现符合决策？ | 一段或条目 | 评审、测试或检查手段 + 判定标准 | 有可执行的检查手段则有效 |
| 各方案利弊（Pros and Cons of the Options） | 每个方案的利弊？ | 每方案一小节 | 好／中性／坏，因为…… | 只写真实的评价，不为凑齐利弊硬加条目 |
| 另见（More Information） | 补充材料、后续重审条件？ | 链接或段落 | — | 有则插入 |

---

## 变体 D: Y-statement

用一句话记录单个决策（Zdun et al. 2013）。适合决策日志里需要比一行更完整、又不值得写整篇 ADR 的决策。

### 必需内容

| 必需内容 | 本节回答 | 排版 |
|--------|------|------|
| Y-statement | 在 [功能需求或组件] 的背景下，面对 [非功能需求或关注点]，我们决定采用 [方案]、放弃 [其他方案]，以达到 [收益]，接受 [代价] | 一句话 |

### 按需模块

| 模块名 | 本节回答 | 排版 | 格式规范 | 保留条件 |
|--------|------|------|----------|-----------|
| 理由补充 | 一句话放不下的依据？ | 一段 | 只补依据，不重复句中内容 | 句中各段已足够清楚时删除 |

---

## 类型验证标准

通过核对清单（`references/verify.md`）后，额外检查以下 ADR 专用项：

| # | 检查项 | 判定标准 |
|---|--------|---------|
| A1 | 决策在前 3 段可见 | 读者不需要翻到文档中间才知道"决定了什么" |
| A2 | 理由通过排除性检验（G3） | 将决策替换为相反选择时，论据需要重写；不是可支持任意选择的通用理由 |
| A3 | 有状态标记 | 决策日志、Nygard、MADR：Proposed / Accepted / Deprecated / Superseded 不缺失；Y-statement 不适用 |
| A4 | Accepted 后不改 | 决策变更时开新 ADR 标注 Superseded by，不修改原文 |
| A5 | 后果完整 | Nygard：后果列出全部后果，含负面和中性，不为凑类别硬加；MADR：本包要求的后果至少一条负面后果或说明为何没有；Y-statement 由"接受 [代价]"承担 |
| A6 | 后果有度量 | 每条后果有具体度量或影响范围，不是"可能有影响" |
| A7 | 备选方案非凑数 | 若有备选方案模块，候选必须真实且有淘汰依据；缺依据时说明缺口与核实方式，不因全维度不占优而删除真实候选 |
| A8 | 一篇一事 | 一个 ADR 只记录一个决策；分短期、中期、长期阶段的决策每阶段各开一篇 |

## 权威参考

| 来源 | 类型 | 用途 |
|------|------|------|
| Michael Nygard "Documenting Architecture Decisions"（2011 原文） | 教写法 | Nygard 三段式的原始定义（Context / Decision / Consequences） |
| Zdun et al. "Sustainable Architectural Design Decisions"（IEEE Software, 2013） | 教写法 | Y-statement 格式的学术来源 |
| MADR 4.0（adr.github.io/madr） | 字段模板 | 备选方案、决策结果、Confirmation 等节名 |
| Microsoft Azure Well-Architected Framework ADR | 字段模板 | Accepted 记录只追加不修改、记录置信度、分阶段决策拆成多篇 |
| adr.github.io | 字段模板 | ADR 工具和格式索引 |
| Google AIP（一篇一个主题） | 成品逻辑 | ADR "一篇一事"原则的实际范例 |
