#!/usr/bin/env python3
"""Validate Markdown, export graph.json, and build a portable offline explorer."""

import json
import subprocess
import sys
from pathlib import Path

from check_graph import read_node


def build(root):
    subprocess.run(
        [sys.executable, str(root / "tools/check_graph.py"), "--export", "graph.json"],
        check=True,
    )
    graph = json.loads((root / "graph.json").read_text(encoding="utf-8"))
    for node in graph["nodes"]:
        _, node["body"] = read_node(root / node["path"])
    # Escape '<' so note text cannot terminate this non-executable script element.
    payload = json.dumps(graph, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    template = (root / "tools/viewer_template.html").read_text(encoding="utf-8")
    if template.count("__CSTREE_DATA__") != 1:
        raise ValueError("viewer template must have exactly one data placeholder")
    (root / "index.html").write_text(template.replace("__CSTREE_DATA__", payload), encoding="utf-8")
    print(f"Built index.html with {len(graph['nodes'])} embedded notes; no server required.")


if __name__ == "__main__":
    build(Path(__file__).resolve().parents[1])
