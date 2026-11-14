"""Regression checks for graph integrity and portable viewer generation."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from check_graph import content_lines, read_node

ROOT = Path(__file__).resolve().parents[1]


def note(metadata, body):
    return "---\n" + "\n".join(f"{k}: {json.dumps(v)}" for k, v in metadata.items()) + "\n---\n\n" + body


class GraphIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for folder in ("concepts", "references", "tools"):
            (self.root / folder).mkdir()
        shutil.copyfile(ROOT / "tools/check_graph.py", self.root / "tools/check_graph.py")
        self.hub = self.root / "README.md"
        self.concept = self.root / "concepts/example.md"
        self.reference = self.root / "references/source.md"
        self.hub.write_text(note(dict(id="test", type="hub", title="Test", aliases=[], domains=["algorithms"]), "# Test\n\n- **Reading route:** [Example](concepts/example.md)\n"))
        self.concept.write_text(note(dict(id="example", type="concept", title="Example", aliases=[], domains=["algorithms"], branch="algorithms"), "# Example\n\n## Mechanism\n\nA mechanism.\n\n## Worked example\n\nAn example.\n\n## Engineering implications\n\nA tradeoff.\n\n## Graph connections\n\n- **supported_by:** [Source](../references/source.md)\n"))
        self.reference.write_text(note(dict(id="source", type="reference", title="Source", authors=["Author"], kind="book", accessed="2026-11-10"), "# Source\n\n[Primary source](https://example.com/book)\n\n- **explains:** [Example](../concepts/example.md)\n"))

    def run_checker(self, *args):
        return subprocess.run([sys.executable, str(self.root / "tools/check_graph.py"), *args], capture_output=True, text=True)

    def test_valid_graph_and_deterministic_export(self):
        result = self.run_checker("--expected-concepts", "1", "--export", "graph.json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        first = (self.root / "graph.json").read_bytes()
        graph = json.loads(first)
        self.assertEqual(len(graph["nodes"]), 3)
        self.assertEqual(len(graph["edges"]), 3)
        self.assertEqual(self.run_checker("--export", "graph.json").returncode, 0)
        self.assertEqual(first, (self.root / "graph.json").read_bytes())

    def test_missing_target_is_rejected(self):
        self.concept.write_text(self.concept.read_text() + "\n[Missing](missing.md)\n")
        result = self.run_checker()
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing or outside-repository target", result.stdout)

    def test_prerequisite_cycle_is_rejected(self):
        self.concept.write_text(self.concept.read_text() + "\n- **requires:** [Self](example.md)\n")
        result = self.run_checker()
        self.assertEqual(result.returncode, 1)
        self.assertIn("prerequisite cycle", result.stdout)

    def test_unknown_relation_is_rejected(self):
        self.concept.write_text(self.concept.read_text().replace("supported_by", "suported_by"))
        result = self.run_checker()
        self.assertEqual(result.returncode, 1)
        self.assertIn("unknown relation", result.stdout)

    def test_fenced_and_inline_examples_are_not_edges(self):
        self.concept.write_text(self.concept.read_text() + "\n```markdown\n[Missing](missing.md)\n```\n\n`[Missing](missing.md)`\n")
        self.assertEqual(self.run_checker().returncode, 0)

    def test_source_path_cannot_use_hub(self):
        self.concept.write_text(self.concept.read_text().replace("- **supported_by:** [Source](../references/source.md)", "[Hub](../README.md)"))
        result = self.run_checker()
        self.assertEqual(result.returncode, 1)
        self.assertIn("no path to a paper or primary reference", result.stdout)

    def test_reference_requires_primary_url(self):
        self.reference.write_text(self.reference.read_text().replace("[Primary source](https://example.com/book)", "No external source."))
        result = self.run_checker()
        self.assertEqual(result.returncode, 1)
        self.assertIn("no external source link", result.stdout)

    def test_invalid_branch_metadata_reports_error_without_crash(self):
        self.concept.write_text(self.concept.read_text().replace('branch: "algorithms"', 'branch: ["algorithms"]'))
        result = self.run_checker()
        self.assertEqual(result.returncode, 1)
        self.assertIn("unknown branch", result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_invalid_calendar_date_is_rejected(self):
        self.reference.write_text(self.reference.read_text().replace("2026-11-10", "2026-99-99"))
        result = self.run_checker()
        self.assertEqual(result.returncode, 1)
        self.assertIn("reference needs accessed date", result.stdout)

    def test_prerequisite_must_be_a_concept(self):
        self.concept.write_text(self.concept.read_text() + "\n- **requires:** [Source](../references/source.md)\n")
        result = self.run_checker()
        self.assertEqual(result.returncode, 1)
        self.assertIn("requires must connect two concepts", result.stdout)

    def test_filename_and_node_identity_must_match(self):
        self.concept.write_text(self.concept.read_text().replace('id: "example"', 'id: "different"'))
        result = self.run_checker()
        self.assertEqual(result.returncode, 1)
        self.assertIn("ID must match filename", result.stdout)


class PublishedGraphTests(unittest.TestCase):
    def test_requested_topics_are_present(self):
        ids = {read_node(p)[0]["id"] for p in (ROOT / "concepts").glob("*.md")}
        expected = {"stacks", "queues", "trees", "graphs", "sorting", "dynamic-programming", "c", "cpp", "java", "python", "csharp", "go", "rust", "javascript", "typescript", "compilers", "design-patterns", "vibe-programming", "databases", "operating-systems", "distributed-systems"}
        self.assertFalse(expected - ids)

    def test_viewer_embeds_current_graph_and_every_note(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        start = '<script type="application/json" id="graph-data">'
        embedded = json.loads(html.split(start, 1)[1].split("</script>", 1)[0])
        exported = json.loads((ROOT / "graph.json").read_text(encoding="utf-8"))
        for node in embedded["nodes"]:
            self.assertEqual(node.pop("body"), read_node(ROOT / node["path"])[1])
        self.assertEqual(embedded, exported)

    def test_code_fences_ignore_other_fence_characters(self):
        self.assertEqual(list(content_lines("before\n````\n~~~\n[hidden](x.md)\n````\nafter")), ["before", "after"])


if __name__ == "__main__":
    unittest.main()
