# 贡献指南

技能包在 `skills/doc-writer/`，下文路径都相对该目录。每条规则只保留一处，其他位置引用文件名，因为复述容易失去同步。用实际测试结果说明变更。

## 1. 修改规则或脚本

1. 先读 `SKILL.md`，再按文件表读要改的参考。五阶段编排见 `references/orchestration.md`，分诊见 `references/review.md`，排版见 `references/formatting.md`。
2. `SKILL.md` 的文件表要列出 `references/` 下全部文件，新增或改名时同步。
3. 词项变化写在 G1 表里，`scripts/doc-lint.py` 从那里读取；更改 G1 表格格式时，同步解析逻辑与 `tests/test_doc_lint.py`。
4. 为行为变更增加正例、反例或豁免测试，再运行：

   ```bash
   uv run -q --with pytest python -m pytest -q tests
   ```

5. 改过的 Markdown 都跑一遍 doc-lint，逐条判断候选：

   ```bash
   python3 skills/doc-writer/scripts/doc-lint.py <文件>
   ```

6. 在变更说明中记录影响、实际测试结果及尚未验证的行为。脚本保持只读、无第三方依赖、无联网；语义判断留给模型，不要改成字面命中即违规。

新增写作规则时，在 `SOURCES.md` 登记来源；推论和综合标为「建议」。

## 2. 提交改动

提交标题使用 `类型(范围): 变更目的`，例如 `fix(review): 收紧图表选用标准`。正文按需要说明关键改动、验证命令及结果。

提交前核对实际暂存文件及差异：

- 收录规则、写作指南、使用文档、维护测试和来源记录。
- 排除本地配置、凭据、缓存、试写产物和临时研究材料；不提交公司内部材料或个人隐私。
- 保留 `skills/doc-writer/` 下的全部运行文件。包内链接只向下指向按需文件，且不指向包外。

推送和版本发布分别确认范围，不将一次本地提交等同于发布授权。

## 3. 许可与版本验证

项目原创内容采用 [MIT License](LICENSE)，第三方来源见 [SOURCES.md](SOURCES.md)。

发布版本前运行自动测试，并按[手动验收任务](tests/SMOKE.md)验证目标客户端和代表性写作场景。记录实际环境与结果，不将测试数量换算成模型遵守率。
