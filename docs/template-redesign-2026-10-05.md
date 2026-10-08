# 模板与示例重设计方案

**结论：模板结构可以保留，但要分三批修：先改事实错误和过时编号，再把金字塔原理和中文文风规则落进模板，最后补齐缺示例的类型。** 已核验的 6 段外部示例来源可靠，保留；问题集中在 GPT 写的模板正文：有事实错误和查不到的参考来源，内部编号已经过时，还有一套第一次读很难懂的自造表格术语。

## 1. 审核发现

### 1.1 事实错误（已对照一手资料）

| 位置 | 现在写的 | 一手资料 | 改法 |
|---|---|---|---|
| `adr.md` 变体 E | Y 型"适合多阶段演进的决策，追溯决策链"；句式缺"未选方案" | Y-statement 是一句话记录单个决策，六段：In the context of / facing / we decided for / and neglected / to achieve / accepting that（Zimmermann 等） | 改写用途；句式补"放弃了 [其他方案]"；决策链图模块移除或改为可选的 ADR 索引 |
| `adr.md` 变体 D | MADR 含"评估矩阵"；节名为"决策结果""优劣对比" | MADR 4.0.0（2024-09-17）必需：Context and Problem Statement / Considered Options / Decision Outcome；可选：Decision Drivers / Consequences / Confirmation / Pros and Cons of the Options / More Information；没有评估矩阵 | 节名按 4.0 对齐；"验证计划"改为 Confirmation；评估矩阵降为本包自定义可选模块，不归到 MADR |
| `adr.md` A5 | "后果分好坏" | Nygard：列出全部后果，可能有正面、负面和中性 | 改为"列出全部后果，含负面与中性" |
| `adr.md` Nygard 锚定节 | 标题行"编号 + 决策一句话" | Nygard：标题是短名词短语，如"ADR 9: LDAP for Multitenant Integration"；Decision 用完整句、主动语态"We will …" | 标题照 Nygard；Decision 节要求"我们将……"式完整句 |
| `adr.md` | 未提置信度、分阶段 | Azure WAF ADR 页：记录决策置信度；多阶段决策拆成多条记录；只追加不改 | 加可选字段"置信度"；"一篇一事"补"分阶段决策各开一篇" |
| `test-report.md` 参考 | IEEE 829 | 2013 年起由 ISO/IEC/IEEE 29119-3 取代，对应文档为 Test Completion Report | 换成 29119-3 |
| `test-report.md` 参考 | Google SRE Book §15 Postmortem Culture | 事后复盘文化，和测试报告无关 | 删除 |
| `test-report.md` CI 失败项 | 排版"时间线（按严重程度排序）" | 时间线和按严重程度排序互相矛盾 | 改为"按严重程度排序的列表" |
| `changelog.md` 参考 | "Conventional Changelogs Suck" | 来源存在：Sophia Willows，2024-06-24（初查误判为查不到，Codex 复审纠正） | 保留并补作者、日期与链接 |
| `changelog.md` 参考 | Keep a Changelog 分类写成 4 个 | 1.1.0 有 6 类：Added / Changed / Deprecated / Removed / Fixed / Security | 补全 |
| `tech-design.md` 变体 B | "对应 Google 10-20 页格式中的精简版" | Google 设计文档：迷你版 1-3 页，完整版 10-20 页；核心节含 Alternatives considered 与 Cross-cutting concerns | 改写对应关系；备选方案在有取舍时列为必需节，补"跨领域关注点（安全、隐私、可观测性）"可选节 |

待核实（来源说法具体但未找到依据）：`tutorial.md` 的"Django Tutorial 每部分 < 30 分钟""Stripe 零分支"，`how-to.md` 的"K8s 任务标题命名'如何 X'"（K8s 任务页实际用祈使句标题，如 Configure a Pod to Use a ConfigMap），`reference.md` 的"K8s style guide 键卡片格式、问题先行"。核实不了的一律删除。

### 1.2 过时编号（字母代号问题在模板里仍在）

10 个模板的标题写着"类型验证标准（Phase 4 Step 1c）"，正文写"通用收尾检查（3.5）""约束体系 §3.4 D1"。运行时早已不按 Phase 4 和 3.5 组织，第一次读的 agent 无从查起。改为"类型验证标准"，正文写"通过 [检查入口](../skills/doc-writer/references/verify-checks.md) 的通用检查后"。测试只锁定 `## 类型验证标准` 前缀，改名不破坏测试。

### 1.3 自造术语

模板用一套 GPT 自造的表格词汇："锚定节／锚问／排版／可插模块／有效性检验"，排版列再填"倒金字塔／契约表／定义列表／问题→方案→代价"。这些词在 `write-assist.md` 有定义，但读模板时不在眼前。

改法（第二批）：表头改成常用词，含义不变。

| 现在 | 改成 |
|---|---|
| 锚定节 | 必需章节 |
| 锚问 | 本节回答 |
| 排版 | 写法（用一句话写清，如"表格：指标 / 目标值 / 测量方式"） |
| 可插模块 | 按需章节 |
| 有效性检验 | 保留条件 |

术语出现在 runtime、5.2 模块和测试中，需同批替换并加一条测试，防止旧词回流。

### 1.4 防御性叙述

模板顶部的规则段（如 `tech-design.md` 第 24–30 行、`adr.md` 第 91 行）和 `SOURCES.md` 仍有大量"不暗示背书""不补造""不宣称"之类的重复声明。按第一轮去 GPT 腔的同一标准删重复，保留事实、条件和许可义务。

## 2. 金字塔原理落进模板（第一批）

C1e 已在共同约束里，但模板没有给出落点，agent 会把模板章节名当固定标题照抄。

1. `templates/_index.md` 加一条：固定锚定标题只限外部标准规定的名称（Nygard 的 Context / Decision / Consequences、MADR 4.0 节名、Keep a Changelog 的 6 个分类、Diátaxis 类型的惯用标题），其余表格里的章节名是内容槽位；论证类文档写成结论句，参考与操作类保留名词标题。
2. `write-assist.md` 结构表"倒金字塔"一行补：章节之间按 C1e 组织。
3. 默认变体补"开头结论"：技术设计 Lean、测试报告 CI、PRD Lean、ADR Nygard（Decision 已在前三段，核对即可）。CI 报告首行写"能否合并 + 阻断项"。
4. eval 每个用例加一条逐条评审器："论证类章节标题写成结论句，开头一段给出全文结论"。

## 3. 文风规则补充（第一批）

技术文档不需要拟人化，只要中性陈述，操作用祈使句。所以 humanizer-zh 的"作者声音、个性、节奏变化"一律不引入，只借"删除型"模式，补进 G1。

**从 humanizer-zh（MIT，op7418/Humanizer-zh）借入 G1 未覆盖的模式**，注明出处：

| 新增类别 | 模式 | 处理 |
|---|---|---|
| 与假想敌辩论 | "有人可能会认为……但实际上" | 删除，直接陈述结论与条件 |
| 强凑三段式 | 为凑三项硬加一项 | 按实际项数写 |
| 意义拔高 | 句尾"，这体现了……的重要性" | 删除 |
| 宣传语 | "强大的""无缝""开箱即用"（无度量时） | 删除或给度量 |
| 借权威 | "业界普遍认为""专家指出"（无出处） | 给出处或删除 |
| 限定词堆叠 | "可能在一定程度上" | 只留一个，或写出具体条件 |
| 客服腔 | "希望对您有帮助""如有疑问请随时" | 删除 |
| 谈论上一稿 | "相比上一版，本文……" | 删除；变更记录归对应文档 |
| 首句复读标题 | 节首句重复标题 | 删除，首句直接给要点 |
| 粗体当装饰 | 一段多处加粗 | 每段最多一处，只标结论或警告 |
| 破折号连接 | 用破折号串联分句 | 改为句号或冒号 |

不引入：作者声音与个性、节奏变化、戏剧性短句（与技术文档的中性要求冲突）。

**从阮一峰《中文技术文档的写作规范》（公共领域）借入的句法与排版规则**，放进 `constraints-writing.md` 新的一小节"中文表达基础"：

- 中文与半角英文之间加一个半角空格；中文与数字之间空格与否全文统一。
- 用主动语态，少用"被"字句；避免双重否定。
- "其、该、此、这"等代词只能有一个指代对象。
- 段落中心句放段首；同级标题不出现孤立的单个子标题，下级标题不重复上级名称。

`doc-lint.py` 只补一条机械候选：汉字与半角字母直接相邻（缺空格）。

## 4. 示例补全（第三批）

现有 6 段外部示例都有固定提交、行号、SHA-256 和许可登记，质量可靠，保留。缺口是 11 个类型中有 7 个没有真实示例。候选来源（许可已查）：

| 类型 | 候选 | 许可 | 优势 |
|---|---|---|---|
| Tutorial / How-to / Reference / Explanation | Kubernetes 官方文档 zh-cn 版（如 Hello Minikube、配置 Pod 使用 ConfigMap、Pod 概念页） | CC BY 4.0 | 有官方中文译文，不必自译 |
| ADR（完整 MADR） | adr/madr 仓库自身的 `docs/decisions` | MIT / CC0-1.0 | 完整决策记录，补上 Backstage 片段缺的状态和后果 |
| 技术设计 RFC | rust-lang/rfcs 中带 Drawbacks / Alternatives 的短 RFC | Apache-2.0 / MIT | 取舍和备选方案写法 |
| Runbook | 待查 GitLab runbooks 许可 | 待核实 | — |
| PRD、测试报告 | 未找到许可清楚的真实样本 | — | 保持无示例，靠结构与验证标准 |

每段新示例按 `SOURCES.md` 现有登记字段入库（固定提交、行号、SHA-256、许可全文），并加入 `test_verified_translations_are_unchanged` 的哈希锁定。

## 5. 执行顺序与验证

| 批次 | 内容 | 验证 |
|---|---|---|
| 一 | 1.1 事实修正、1.2 去过时编号、第 2 节金字塔落点、第 3 节文风规则 | 61 项测试 + 新增旧编号回流测试；ruff；doc-lint 扫全部模板 |
| 二 | 1.3 术语改名、1.4 去防御性叙述 | 同上 + 旧术语回流测试；eval 重跑（逐条评审器） |
| 三 | 第 4 节示例补全 | 来源登记字段齐全；哈希测试 |

每批单独提交。第一批完成后重跑 eval，对比本次基线（带 skill 9/18，无 skill 1/18）。

## 6. Codex 复审与执行记录

Codex（gpt-6.1-sol xhigh）复审后结论为"修订后执行"。逐条核实后全部采纳：

| 意见 | 处理 |
|---|---|
| "Conventional changelogs suck" 确实存在 | 恢复参考并补作者、日期；"不自动生成"不再归给 Common Changelog（它允许从提交生成草稿），改为本包要求 |
| Zdun 论文题名少了 Design | 改为 "Sustainable Architectural Design Decisions"（IEEE Software, 2013） |
| IEEE 829 由 29119 系列整体取代；现行 29119-3:2021；CI 报告接近 Test Status Report | 参考行改写 |
| Nygard Context 不应写"问题→方案→代价" | 改为中性陈述各方因素 |
| MADR 状态是可选元数据，Consequences、Confirmation 位于 Decision Outcome 下，无利弊配额 | 注明本包附加要求，保留层级，删除配额 |
| ADR 类型检查未区分变体 | A3、A5 写明适用变体 |
| Azure"只追加"只针对 Accepted 记录 | 已限定 |
| 技术设计篇幅说法无 Google 依据；隐私检查缺失 | 改为本包建议；安全分析模块改为"安全与隐私"，删除时仍须检查 |
| IETF RFC 不是 SDD 结构依据 | 删除后半句 |
| Keep a Changelog 无必需 Breaking 节，弃用项不必有移除时间 | 注明本包扩展；移除时间未定时照写 |
| Stripe、Rust Book、K8s 标题大小写、Twelve-Factor 归因过度 | 逐条改为有依据的表述 |
| G4 与 C1a、C1d 重复；限定词、粗体、破折号、无主句规则过度绝对 | 删除重复项；限定词按含义判断、粗体去配额、破折号只管滥用、祈使句允许省略主语；结构规则豁免用户骨架 |
| 术语改名用"必需章节"不准确 | 改用"必需内容／按需模块／保留条件／本节回答"，加旧词回流测试 |
| Rust RFC 许可不能全仓统一判断；MADR 为 MIT OR CC0-1.0；GitLab runbooks 根许可 MIT | 第三批选材时按单篇核验 |

1.4 节（删防御性叙述）暂缓：Codex 指出模板顶部规则段和 SOURCES.md 中的否定句多为真实义务（批准状态、D1 提前读取、BSD 不得背书条款），按句式删除会丢义务。

## 7. 第二轮复审与 eval5

第二轮 Codex 复审 5 条全部核实采纳：服务类 README 不强制截图（后台服务可用请求响应示例）；特性列表去掉条数下限；MADR 的 Confirmation 改为"选用时置于 Decision Outcome 下"；新增两份 MIT 副本加哈希保护；uv 示例补全第 76–77 行，选段改为 44–77 行并重算摘要。

eval5（sonnet 评审，每用例 3 次，$6.38，评审器已拆成逐条并新增"结论先行"两条，因此通过率与 eval4 不是同一标准，分差可比）：

| 用例 | 带 skill | 无 skill | 平均分差 |
|---|---|---|---|
| ci-report-no-log | 2/3 | 0/3 | +0.40 |
| cli-reference | 3/3 | 0/3 | +0.53 |
| tech-design-memo | 1/3 | 0/3 | +0.67 |

合计带 skill 6/9、无 skill 0/9，平均分差 +0.53（eval4 为 +0.44）。带 skill 的 3 次失败都在"结论先行"：两次在结论前写了元数据段，一次在正文前加了聊天式前言。已在 C1e 补一句：元数据压成一行放在结论之后或文末，只输出正文时不加前言。该修改未再跑 eval 验证。
