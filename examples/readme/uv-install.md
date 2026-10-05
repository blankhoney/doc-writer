# uv README 的安装节（已核验局部来源·中文节译）

- **来源**：[uv README](https://github.com/astral-sh/uv/blob/46b84fd0bfec23b72f29e8e2185ba68a65052f48/README.md) 第 44–77 行 Installation 全节，Astral Software Inc.，固定提交 `46b84fd0bfec23b72f29e8e2185ba68a65052f48`
- **许可**：原项目以 Apache-2.0 或 MIT 双许可发布，本包按 MIT 使用，[MIT 许可证副本](../licenses/uv-LICENSE-MIT.txt)；原始选段校验值见 [SOURCES.md](../SOURCES.md#uv-readme)
- **取样**：整节照译说明文字，命令和代码块内注释保持英文原样
- **值得模仿**：先给推荐方式，再给备选；每种方式一个代码块，块内注释写适用平台；最后告诉读者装好后怎么升级
- **未运行**：未执行任何安装命令

## 安装

````markdown
## Installation

用独立安装脚本安装 uv：

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

或者从 [PyPI](https://pypi.org/project/uv/) 安装：

```bash
# With pip.
pip install uv
```

```bash
# Or pipx.
pipx install uv
```

如果是用独立安装脚本安装的，uv 可以把自己升级到最新版本：

```bash
uv self update
```

安装细节和其他安装方式见[安装文档](https://docs.astral.sh/uv/getting-started/installation/)。
````
