"""Seeded property tests for doc-lint; standard library only.

These complement the example-based suites: they generate documents from a fixed
seed and check invariants that must hold for any input, so regressions do not
need a new hand-written example per edge case.
"""

import random
import runpy
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ROOT = REPO / "skills" / "doc-writer"
SCRIPT = ROOT / "scripts" / "doc-lint.py"
MODULE = runpy.run_path(str(SCRIPT))
parse_rules = MODULE["parse_rules"]
scan_text = MODULE["scan_text"]
RULES = parse_rules(
    (ROOT / "references" / "constraints-writing.md").read_text(encoding="utf-8-sig")
)

# Layout records summarize several lines or use their own text; the rest report
# a literal hit that must appear in the original physical line.
SUMMARY_CATEGORIES = {
    "候选/超长段落",
    "候选/正文加粗",
    "候选/首先其次串连",
}
DIRECTIVE = "<!-- doc-lint: ignore-next-line 引用原文 -->"
TOKENS = [
    "显著", "赋能", "众所周知", "不言而喻", "首先", "其次", "然后", "最后",
    "中文API", "说明:中文", "方案(中文)", "**甲**", "长", "X", "。", "，",
    "`code`", "https://x.test/显著", "[显著](a)", "| a |", "# 标题",
    "- 列表项", "1. 系统会写入", "<!-- 引用 -->",
]
SAFE_TOKENS = ["显著", "赋能", "中文API", "说明:中文", "方案(中文)", "X", "。", "，"]


def physical_lines(text):
    text = text.removeprefix("﻿").replace("\r\n", "\n")
    lines = text.split("\n") if text else []
    if lines and lines[-1] == "" and text.endswith("\n"):
        lines.pop()
    return lines


def candidates(text, skip=()):
    return [row for row in scan_text(text, RULES, skip)[0] if row[1].startswith("候选/")]


def generated_documents(count=250):
    rng = random.Random(20261020)
    for _ in range(count):
        lines = [
            "".join(rng.choice(TOKENS) for _ in range(rng.randint(0, 8)))
            for _ in range(rng.randint(0, 12))
        ]
        yield "\n".join(lines) + rng.choice(("", "\n"))


class GeneratedDocumentTests(unittest.TestCase):
    def test_records_stay_inside_physical_lines_and_report_original_text(self):
        for text in generated_documents():
            lines = physical_lines(text)
            records, suppressed = scan_text(text, RULES)
            self.assertGreaterEqual(suppressed, 0)
            self.assertEqual([row[0] for row in records], sorted(row[0] for row in records))
            for number, category, hit in records:
                self.assertGreaterEqual(number, 1, text)
                self.assertLessEqual(number, max(len(lines), 1), text)
                if category.startswith("候选/") and category not in SUMMARY_CATEGORIES:
                    self.assertIn(hit, lines[number - 1], (category, text))

    def test_bom_and_crlf_do_not_change_records(self):
        for text in generated_documents(80):
            expected = scan_text(text, RULES)
            self.assertEqual(scan_text("﻿" + text, RULES), expected)
            self.assertEqual(scan_text(text.replace("\n", "\r\n"), RULES), expected)


class StructureTests(unittest.TestCase):
    def test_suppression_counts_only_the_next_physical_line(self):
        rng = random.Random(20261021)
        for _ in range(40):
            body = "".join(rng.choice(SAFE_TOKENS) for _ in range(rng.randint(0, 8)))
            alone = candidates(body)
            records, suppressed = scan_text(DIRECTIVE + "\n" + body + "\n显著。", RULES)
            self.assertEqual(suppressed, len(alone), body)
            self.assertFalse(
                [row for row in records if row[1].startswith("候选/") and row[0] == 2]
            )
            applications = [row for row in records if row[1] == "抑制应用"]
            self.assertEqual(len(applications), 1, body)
            self.assertEqual(applications[0][0], 2)

    def test_format_skips_partition_the_candidates(self):
        rng = random.Random(20261022)
        for _ in range(40):
            text = "".join(rng.choice(TOKENS) for _ in range(rng.randint(0, 6)))
            if "\n" in text:
                continue
            full = candidates(text)
            kept = candidates(text, MODULE["FORMATS"])
            formats = [
                row
                for row in full
                if row[1].split("/", 1)[1].split("·")[0] in MODULE["FORMATS"]
            ]
            self.assertEqual(sorted(full), sorted(kept + formats), text)


if __name__ == "__main__":
    unittest.main()
