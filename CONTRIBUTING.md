# 贡献指南

技能包在 `skills/doc-writer/`，下文的 `references/`、`assets/`、`scripts/` 都指这个目录下的路径。修改 skill 时保持规则来源明确、模板职责清楚，并用实际测试结果说明变更。模板扩展的完整操作见[模板扩展指南](docs/guide/templates.md)。

## 1. 修改规则或脚本

1. 先读 [rules.md](skills/doc-writer/references/rules.md)、[constraints-writing.md](skills/doc-writer/references/constraints-writing.md)，以及按性质的 [product-docs.md](skills/doc-writer/references/product-docs.md) 或 [tech-docs.md](skills/doc-writer/references/tech-docs.md)。一条规则只在一个文件里写，其他文件写路径引用，不复述。
2. 修改规则时同步相关运行时指引和适用模板。词项变化应由脚本从 G1 原文读取（当前为 `references/constraints-writing.md` 的 G1）；更改 G1 表格格式时，同步解析逻辑与损坏输入测试。
3. 为行为变更增加可复现的正例、反例或豁免测试，再运行：

   ```bash
   python3 -B -m unittest discover -s tests -v
   ```

4. 在变更说明中记录影响、实际测试结果及尚未验证的行为。模型负责语义判断，脚本保持只读、无第三方依赖和无联网行为；语义判断不得被改成字面命中即违规。

## 2. 修改模板与示例

保留类型索引、变体选择、必需内容、模块字段与类型验证。内容相关但证据不足时，保留已知事实并说明需要补充的信息。

- 新类型同步 `assets/templates/_index.md`、公开类型说明及 `tests/test_package_contract.py` 的预期集合。
- 真实来源示例在 `assets/examples/SOURCES.md` 登记固定来源、版本、许可、署名和摘录或改编范围，并随包保留所需许可证与 NOTICE；核验后再收录，未核验材料不进入正向示例集合。
- 第三方示例保留原许可证和所需 NOTICE；改动译文时对照原文。
- 构造示意明确用途；测试夹具只用于复现行为，不写成真实项目数据，也不冒充真实文档的 few-shot。

不要提交公司内部材料、凭据、个人隐私或尚未核验的外部原文。

## 3. 提交改动

提交标题使用 `类型(范围): 变更目的`，例如 `feat(templates): 增加操作指南变体`。正文按需要说明关键改动、验证命令及结果。

提交前核对实际暂存文件及差异：

- 收录规则、模板、使用文档、维护测试和已核验来源记录。
- 排除本地配置、凭据、缓存、试写产物和临时研究材料。
- 保留 `skills/doc-writer/` 下的全部运行文件。
- 新增或移动包内文件时，按[跳转模型](docs/design/5.1-progressive-disclosure.md#513-文件组织)放链接：只向下链接，指向 `SKILL.md` 和它资源表里的文件时只写路径。
- `.gitignore` 只影响未跟踪文件；敏感内容曾入库时，另行处理历史，不能只删当前文件。

推送和版本发布分别确认范围，不将一次本地提交等同于发布授权。

## 4. 许可与版本验证

项目原创内容采用 [MIT License](LICENSE)。提交者应有权按该许可贡献原创内容；第三方片段继续使用各自许可，详见[来源记录](skills/doc-writer/assets/examples/SOURCES.md)。

发布版本前运行自动测试，并按[手动验收任务](tests/SMOKE.md)验证目标客户端和代表性写作场景。记录实际环境与结果，不将测试数量换算成模型遵守率。
