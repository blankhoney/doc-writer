import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EXAMPLES = REPO / "skills" / "doc-writer" / "assets" / "examples"


class ExampleSourceTests(unittest.TestCase):
    def test_examples_are_registered_with_source_and_license(self):
        registry = (EXAMPLES / "SOURCES.md").read_text(encoding="utf-8")
        for path in sorted(EXAMPLES.glob("*/*.md")):
            with self.subTest(example=path.name):
                self.assertIn(path.name, registry)
                text = path.read_text(encoding="utf-8")
                if path.name != "implementation-sketch.md":
                    self.assertIn("https://", text)
                    self.assertIn("../licenses/", text)


if __name__ == "__main__":
    unittest.main()
