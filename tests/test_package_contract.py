"""Static package checks; these do not prove model behavior or skill discovery."""

import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

REPO = Path(__file__).resolve().parent.parent
ROOT = REPO / "skills" / "doc-writer"
RUNTIME = sorted((ROOT / "references").glob("*.md"))
TYPES = {
    "prd",
    "tech-design",
    "api-doc",
    "changelog",
    "test-report",
    "deploy-runbook",
    "adr",
    "tutorial",
    "how-to",
    "reference",
    "explanation",
    "readme",
}


def outside_fences(text):
    """Ignore fenced examples when checking prose links, not Markdown semantics."""
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            run = marker[1]
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield re.sub(r"(?<!`)(`+)(?!`).*?(?<!`)\1(?!`)", "", line)


class PackageTests(unittest.TestCase):
    def test_manual_entry_fields_and_size(self):
        data = (ROOT / "SKILL.md").read_bytes()
        self.assertTrue(data.startswith(b"---\n"))
        text = data.decode("utf-8")
        front = text.split("---", 2)[1]
        fields = dict(re.findall(r"^([a-z-]+):[ \t]*(.*)$", front, re.MULTILINE))
        # Agent Skills 规范只允许这六个顶层字段，客户端专用字段会让 skills-ref 校验失败。
        self.assertLessEqual(
            set(fields),
            {
                "name",
                "description",
                "license",
                "compatibility",
                "metadata",
                "allowed-tools",
            },
        )
        self.assertEqual(fields["name"], "doc-writer")
        self.assertEqual(fields["license"], "MIT")
        self.assertIn("description", fields)
        self.assertLess(len(text.splitlines()), 500)
        self.assertNotIn("CLAUDE_SKILL_DIR", text)
        self.assertNotIn("$ARGUMENTS", text)

    def test_entry_resources_are_real_and_portable(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        # 只看资源表的行，正文步骤里顺带提到的路径不算分发。
        table = "\n".join(l for l in text.splitlines() if l.startswith("|"))
        resources = set(
            re.findall(
                r"`((?:references|scripts|assets)/[a-zA-Z0-9_./-]+\.(?:md|py))`", table
            )
        )
        resources |= {unquote(link) for link in re.findall(r"\]\(([^)\s#]+)\)", text)}
        # 入口必须分发全部运行时文件，references 下不能有入口没提到的孤儿文件。
        self.assertEqual(
            {r for r in resources if r.startswith("references/")},
            {"references/" + p.name for p in RUNTIME},
        )
        self.assertIn("assets/templates/_index.md", resources)
        self.assertIn("/scripts/doc-lint.py'", text)
        self.assertTrue((ROOT / "scripts" / "doc-lint.py").is_file())
        for resource in resources:
            with self.subTest(resource=resource):
                self.assertEqual(urlsplit(resource).scheme, "")
                self.assertTrue((ROOT / resource).is_file(), resource)
        for path in [ROOT / "SKILL.md", *RUNTIME]:
            body = path.read_text(encoding="utf-8")
            self.assertNotIn("/Users/", body)
            self.assertNotIn("/home/", body)

    def test_runtime_files_use_plain_terms(self):
        # 运行时文件不用自造术语和失效编号，单独安装的技能包才能读懂。
        lint = (ROOT / "scripts" / "doc-lint.py").read_text(encoding="utf-8")
        self.assertIn('"constraints-writing.md"', lint)
        paths = [
            ROOT / "SKILL.md",
            *RUNTIME,
            *sorted((ROOT / "assets" / "templates").rglob("*.md")),
        ]
        for path in paths:
            with self.subTest(path=path.name):
                body = path.read_text(encoding="utf-8")
                self.assertNotIn("docs/research/", body)
                self.assertNotRegex(body, r"锚定节|锚问|可插模块|有效性检验")
                self.assertNotRegex(body, r"Phase 4|收尾检查（3\.5）|§3\.4")

    def test_index_default_variant_exists_in_template(self):
        index = (ROOT / "assets" / "templates" / "_index.md").read_text(
            encoding="utf-8"
        )
        rows = re.findall(
            r"^\|[^|]+\| \[([a-z-]+)\.md\]\([^)]+\) \| ([^|]+?) \|", index, re.MULTILINE
        )
        self.assertEqual({name for name, _ in rows}, TYPES)
        slugs = {
            "prd": "lean",
            "tech-design": "lean",
            "api-doc": "endpoint-reference",
            "changelog": "keep-a-changelog",
            "test-report": "ci-report",
            "deploy-runbook": "deploy-guide",
            "adr": "nygard",
            "tutorial": "shortest-path",
            "how-to": "task-recipe",
            "reference": "key-card",
            "explanation": "concept-explanation",
            "readme": "tool-library",
        }
        for name, default in rows:
            with self.subTest(template=name):
                text = (ROOT / "assets" / "templates" / (name + ".md")).read_text(
                    encoding="utf-8"
                )
                # frontmatter 的 default_variant 须与索引所列默认变体一致。
                self.assertIn(
                    "default_variant: " + slugs[name] + "\n", text.split("---", 2)[1]
                )
                self.assertRegex(
                    text,
                    r"(?m)^## 变体 [A-Z]: " + re.escape(default),
                )

    def test_template_index_and_metadata(self):
        index = (ROOT / "assets" / "templates" / "_index.md").read_text(
            encoding="utf-8"
        )
        links = set(re.findall(r"\]\(([a-z-]+)\.md\)", index))
        self.assertEqual(links, TYPES)
        for name in TYPES:
            with self.subTest(template=name):
                text = (ROOT / "assets" / "templates" / (name + ".md")).read_text(
                    encoding="utf-8"
                )
                self.assertTrue(text.startswith("---\n"))
                self.assertIn("type: " + name + "\n", text.split("---", 2)[1])
                self.assertIn("default_variant:", text.split("---", 2)[1])
                self.assertIn("## 变体选择", text)
                self.assertIn("## 类型验证标准", text)
                self.assertIn("**示例使用范围**", text)
                self.assertNotIn("示例来源待核验", text)
                self.assertNotIn("未核验草稿", text)
                self.assertIn("../examples/SOURCES.md", text)

    def test_local_markdown_links_resolve_inside_package(self):
        paths = [REPO / "README.md", REPO / "README.zh-CN.md", REPO / "CONTRIBUTING.md"]
        paths.extend((REPO / "docs").rglob("*.md"))
        paths.extend(ROOT.rglob("*.md"))
        for path in paths:
            body = path.read_text(encoding="utf-8")
            for term in {
                "implementation": ("| 代码规范 |", "重点注释已交接且可核验"),
                "code-conventions": ("## 主动注释", "主动补足上述适用重点注释"),
            }.get(path.stem, ()):
                self.assertIn(term, body)
            for line in outside_fences(body):
                for link in re.findall(r"\]\(([^\s)]+)\)", line):
                    parts = urlsplit(link)
                    if parts.scheme or parts.netloc or not parts.path:
                        continue
                    target = (path.parent / unquote(parts.path)).resolve()
                    # 技能包要能单独复制安装，包内链接不能指向包外。
                    home = ROOT if path.is_relative_to(ROOT) else REPO
                    with self.subTest(file=str(path.relative_to(REPO)), link=link):
                        self.assertTrue(
                            target.is_relative_to(home), "link escapes " + home.name
                        )
                        self.assertTrue(target.exists(), "missing local link target")

    def test_active_execution_docs_have_no_stale_script_contract(self):
        paths = [
            ROOT / "SKILL.md",
            REPO / "docs" / "design" / "design-spec.md",
            REPO / "docs" / "design" / "5.1-progressive-disclosure.md",
            *RUNTIME,
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                self.assertNotIn("doc-lint.sh", text)
                self.assertNotIn("hook-config.md", text)
                self.assertNotIn("40 条机械规则", text)
                self.assertNotIn("Hook 自动化为可选配置", text)


class DisclosureGraphTests(unittest.TestCase):
    """渐进式披露：入口统一分发必读文件，其余链接只向下指向按需文件。"""

    def links(self, path):
        body = "\n".join(outside_fences(path.read_text(encoding="utf-8")))
        for link in re.findall(r"\]\(([^\s)]+)\)", body):
            parts = urlsplit(link)
            if parts.scheme or parts.netloc or not parts.path.endswith(".md"):
                continue
            target = (path.parent / unquote(parts.path)).resolve()
            if target != path.resolve():
                yield target

    def test_links_form_shallow_acyclic_graph(self):
        entry = ROOT / "SKILL.md"
        text = entry.read_text(encoding="utf-8")
        stage = {
            (ROOT / p).resolve()
            for p in re.findall(r"`((?:references|assets)/[\w./-]+\.md)`", text)
        }
        graph = {entry.resolve(): stage}
        for path in ROOT.rglob("*.md"):
            if path.resolve() == entry.resolve():
                continue
            targets = set(self.links(path))
            graph[path.resolve()] = targets
            with self.subTest(file=str(path.relative_to(ROOT))):
                # 阶段文件和入口已由入口表分发，其他文件只写路径，不再链接回去。
                self.assertFalse(targets & (stage | {entry.resolve()}))
        # 最长链也不超过 4 跳：入口 → 阶段入口 → 模板 → 分支模板 → 示例。
        longest = {}

        def hops(node, seen=()):
            self.assertNotIn(node, seen, f"cycle at {node}")
            if node not in longest:
                longest[node] = max(
                    (1 + hops(t, (*seen, node)) for t in graph.get(node, ())),
                    default=0,
                )
            return longest[node]

        self.assertLessEqual(hops(entry.resolve()), 4)


if __name__ == "__main__":
    unittest.main()
