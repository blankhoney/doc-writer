# 手动调用验收

这些是验收任务，不是已执行记录。自动测试检查脚本和包结构，以下任务检查客户端发现、阶段编排和真实写作行为。使用独立临时项目安装完整包，保持原项目配置不变。

## 1. 写作任务

| 场景 | 手动请求 | 核对重点 |
|---|---|---|
| 技术设计 | `/doc-writer 根据 skills/doc-writer/scripts/doc-lint.py 写一份技术设计，说明为什么只定位候选。只输出正文，不保存文件。` | 依据带 `文件:行号`；有数据模型或流程、失败路径和取舍；没有编造性能数据 |
| 参考文档 | `/doc-writer 根据 doc-lint.py 写 CLI 参数参考，只描述已有行为，只输出正文，不保存文件。` | `FILE`、`--skip-format`、退出码与实现一致；不加主观决策 |
| 无运行记录的测试报告 | `/doc-writer 我只提供测试源码，没有本次运行日志。写测试报告草稿，只输出正文，不保存文件。` | 不推断本次已通过，说明缺哪条运行记录 |

## 2. 阶段与文件读取核对

在真实会话中查看工具调用轨迹：

| 阶段 | 方法 | 判定依据 |
|---|---|---|
| 编排 | 请求一份涉及源码的技术文档 | 开工前读 `references/orchestration.md`，写出 `definition.md` |
| 研究 | 同上 | 并发派多个子 agent，笔记每条带 `文件:行号` |
| 解决 | 同上 | 读研究阶段的 `edges.md`，产出 `resolutions.md`；符合待问标准的记进 `questions.md`，写作不等待；交付时一次提问，每问附推荐答案 |
| 梳理 | 同上 | 产出 `brief.md` 和 `glossary.md`，多义词只定义一次 |
| 写作 | 请求既有产品介绍又有操作步骤的 README | 写作 agent 按片段读 `writing/marketing.md`、`writing/ops.md`，并读 `formatting.md`、`review.md`、`constraints-writing.md`、`unslop.md` |
| 核查 | 走完整流程 | 派 3 个核查 agent，各写 `evidence/<名称>.md`，不改文档；lead 按三张表统一修改，改完运行 doc-lint |
| 术语一致 | 改一个术语后重走 | 事实与一致核查 agent 全文搜索旧名，列出所有出处，写入 `evidence/事实与一致.md` |
| 无法派子 agent | 在不能派发的环境重试 | 主 agent 按同样阶段自己做，每阶段结束只保留文件 |

会话级核对未执行时如实记录，不写成通过。

## 3. 静态检查

```bash
uv run -q --with pytest python -m pytest -q tests
python3 skills/doc-writer/scripts/doc-lint.py README.md
```

静态测试通过只说明包结构、本地链接和脚本行为一致，不证明模型按阶段工作。

## 4. 操作与记录

1. 在临时项目的 `.claude/skills/doc-writer/` 安装当前包，用 `/skills` 检查发现状态。
2. 每个任务开新会话，保留实际工具调用与结果。
3. 用一个不含 `/doc-writer` 的普通写作请求，检查是否自动调用本 skill。
4. 记录客户端版本、任务输入、实际结果和未执行项。
