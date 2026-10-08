# ripgrep README 的开头定义与"何时不该用"（已核验局部来源·中文节译）

- **来源**：[ripgrep README](https://github.com/BurntSushi/ripgrep/blob/3fce3b5bb0236da2df6d99672afb8a719642eca7/README.md) 第 1–9 行与第 161–182 行，作者 Andrew Gallant，固定提交 `3fce3b5bb0236da2df6d99672afb8a719642eca7`
- **许可**：原项目以 Unlicense 或 MIT 双许可发布，本包按 MIT 使用，[MIT 许可证副本](../licenses/ripgrep-LICENSE-MIT.txt)
- **取样**：两段照译，省略中间的徽章、截图、对比示例和"为什么用"清单；链接与命令保留
- **值得模仿**：首段一口气说清是什么、默认行为、怎么关掉、支持平台、和谁类似；"何时不该用"把不适用场景写成具体条件，并给出替代工具

## 开头定义（第 1–9 行）

```markdown
ripgrep (rg)
------------
ripgrep 是一个面向行的搜索工具，在当前目录下递归搜索匹配正则表达式的内容。默认情况下，ripgrep 遵守 gitignore 规则，自动跳过隐藏文件、隐藏目录和二进制文件。（要关闭全部默认过滤，使用 `rg -uuu`。）ripgrep 对 Windows、macOS 和 Linux 提供一等支持，[每个版本](https://github.com/BurntSushi/ripgrep/releases)都提供二进制下载。ripgrep 与 The Silver Searcher、ack 和 grep 等常见搜索工具类似。
```

## 何时不该用（第 161–182 行）

```markdown
### 为什么不该用 ripgrep？

最初并不打算把所有功能都加进 ripgrep，但随着时间推移，它已经支持其他文件搜索工具中的大部分功能，包括跨多行的搜索结果，以及可选启用的 PCRE2（支持环视和反向引用）。

到目前为止，不用 ripgrep 的主要原因大概是以下一项或几项：

* 你需要一个可移植、随处都有的工具。ripgrep 能在 Windows、macOS 和 Linux 上运行，但并非随处预装，也不遵循 POSIX 等任何标准。做这件事最合适的工具仍是老牌的 grep。
* 你依赖其他工具中的某个功能（或 bug），ripgrep 没有，本 README 也没有列出。
* 存在某个性能边缘情况，ripgrep 表现不好而其他工具表现良好。（请提交 bug 报告！）
* ripgrep 无法安装在你的机器上，或不支持你的平台。（请提交 bug 报告！）
```
