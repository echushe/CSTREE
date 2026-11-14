#!/usr/bin/env python3
"""Validate CSTREE's inline Markdown graph; optionally export derived JSON.

Uses only the Python 3.10+ standard library. Front matter accepts simple
key/value scalars and JSON-style lists, not arbitrary YAML. Fenced code is
excluded from link extraction. Scientific claims and remote URLs are not tested.
"""

import argparse
import json
import re
from collections import Counter, deque
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit


RELATIONS = {
    "requires", "uses", "used_by", "specialization_of", "specialized_by",
    "extends", "extended_by", "compares_with", "related_to", "introduced_in",
    "popularized_by", "supported_by", "applied_in", "explains", "contains",
}
BRANCHES = {
    "algorithms": "Data structures and algorithms",
    "languages": "Programming languages",
    "compilers": "Compilers and runtimes",
    "design": "Software design and architecture",
    "ai-development": "AI assisted development",
    "databases": "Databases and storage",
    "operating-systems": "Operating systems",
    "distributed-systems": "Networks and distributed systems",
    "engineering": "Engineering practice",
}
LINK = re.compile(r"(?<!!)\[([^\]\n]+)\]\(([^\s)]+)\)")
INLINE_CODE = re.compile(r"(?<!`)(`+)(?!`)(.*?)\1(?!`)")
RELATION = re.compile(r"^- \*\*([^*]+):\*\*")
FRONT = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)


def read_node(path):
    match = FRONT.match(path.read_text(encoding="utf-8"))
    if not match:
        raise ValueError("missing front matter")
    metadata = {}
    for line in match[1].splitlines():
        key, separator, raw = line.partition(":")
        if not separator or not re.fullmatch(r"[a-z_]+", key):
            raise ValueError(f"unsupported metadata line: {line}")
        if key in metadata:
            raise ValueError(f"duplicate metadata field: {key}")
        raw = raw.strip()
        try:
            metadata[key] = json.loads(raw)
        except json.JSONDecodeError:
            if raw.startswith(('"', "[", "{")) or not raw:
                raise ValueError(f"invalid metadata value for {key}")
            metadata[key] = raw
    return metadata, match[2]


def content_lines(body):
    fence_character = None
    fence_length = 0
    for line in body.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            run = marker[1]
            if fence_character is None:
                fence_character, fence_length = run[0], len(run)
            elif run[0] == fence_character and len(run) >= fence_length:
                fence_character = None
            continue
        if fence_character is None:
            yield line


def reachable(start, adjacency):
    seen = {start}
    queue = deque([start])
    while queue:
        for target in adjacency.get(queue.popleft(), ()):
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return seen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-concepts", type=int)
    parser.add_argument("--export", type=Path, help="write derived graph JSON")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    files = [root / "README.md"]
    for directory in ("concepts", "papers", "references"):
        files.extend(sorted((root / directory).rglob("*.md")))
    errors, nodes, bodies, ids = [], {}, {}, {}
    for path in files:
        relative = path.relative_to(root).as_posix()
        try:
            node, body = read_node(path)
        except (ValueError, OSError) as exc:
            errors.append(f"{relative}: {exc}")
            continue
        for key in ("id", "type", "title"):
            if not isinstance(node.get(key), str) or not node[key].strip():
                errors.append(f"{relative}: missing string field {key}")
        node_id = node.get("id")
        if not isinstance(node_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", node_id):
            errors.append(f"{relative}: invalid node ID")
            continue
        if node_id in ids:
            errors.append(f"{relative}: duplicate ID {node_id}")
        ids[node_id] = path
        expected_type = "hub" if relative == "README.md" else {"concepts": "concept", "papers": "paper", "references": "reference"}[path.relative_to(root).parts[0]]
        if node.get("type") != expected_type:
            errors.append(f"{relative}: expected type {expected_type}")
        if expected_type != "hub" and path.stem != node_id:
            errors.append(f"{relative}: ID must match filename")
        if not body.startswith(f"\n# {node.get('title')}\n") and not body.startswith(f"# {node.get('title')}\n"):
            if expected_type != "hub":
                errors.append(f"{relative}: title does not match H1")
        for key in (("aliases", "domains") if expected_type in ("hub", "concept") else ("authors",)):
            value = node.get(key)
            if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
                errors.append(f"{relative}: {key} must be a list of strings")
        if expected_type == "concept":
            if not isinstance(node.get("branch"), str) or node["branch"] not in BRANCHES:
                errors.append(f"{relative}: unknown branch")
            if not node.get("domains"):
                errors.append(f"{relative}: domains must not be empty")
            for heading in ("## Mechanism", "## Worked example", "## Engineering implications", "## Graph connections"):
                if heading not in body:
                    errors.append(f"{relative}: missing section {heading}")
        if expected_type == "paper":
            if type(node.get("year")) is not int:
                errors.append(f"{relative}: paper needs an integer year")
            for key in ("venue", "selection"):
                if not isinstance(node.get(key), str) or not node[key].strip():
                    errors.append(f"{relative}: paper needs {key}")
        if expected_type == "reference":
            if node.get("kind") not in ("book", "specification", "documentation", "evidence", "guide"):
                errors.append(f"{relative}: unsupported reference kind")
            accessed = node.get("accessed")
            try:
                if not isinstance(accessed, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", accessed):
                    raise ValueError
                date.fromisoformat(accessed)
            except ValueError:
                errors.append(f"{relative}: reference needs accessed date YYYY-MM-DD")
        if expected_type in ("paper", "reference") and not node.get("authors"):
            errors.append(f"{relative}: source needs at least one author or organization")
        nodes[path] = {**node, "path": relative, "external_references": []}
        bodies[path] = body

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    edges = set()
    for path, body in bodies.items():
        for line in content_lines(body):
            line = INLINE_CODE.sub("", line)
            label = RELATION.match(line) if nodes[path]["type"] != "hub" else None
            relation = label[1] if label else "related_to"
            if relation not in RELATIONS:
                errors.append(f"{nodes[path]['path']}: unknown relation {relation}")
            for text, target in LINK.findall(line):
                url = urlsplit(target)
                if url.scheme in ("http", "https"):
                    if not url.netloc:
                        errors.append(f"{nodes[path]['path']}: malformed external URL {target}")
                        continue
                    item = {"label": text, "url": target}
                    if item not in nodes[path]["external_references"]:
                        nodes[path]["external_references"].append(item)
                    continue
                if not url.path and url.fragment and not url.scheme and not url.netloc and not url.query:
                    continue
                if url.scheme or url.netloc or url.query or url.fragment:
                    errors.append(f"{nodes[path]['path']}: unsupported local link {target}; use a whole-node relative link")
                    continue
                destination = (path.parent / unquote(url.path)).resolve()
                if not destination.is_relative_to(root) or not destination.is_file():
                    errors.append(f"{nodes[path]['path']}: missing or outside-repository target {target}")
                elif destination.suffix == ".md":
                    if destination not in nodes:
                        errors.append(f"{nodes[path]['path']}: target is not a graph node: {target}")
                    else:
                        edges.add((nodes[path]["id"], relation, nodes[destination]["id"]))

    by_id = {node["id"]: node for node in nodes.values()}
    adjacency = {node_id: set() for node_id in by_id}
    undirected = {node_id: set() for node_id in by_id if by_id[node_id]["type"] != "hub"}
    requirements = {node_id: set() for node_id in by_id}
    for source, relation, target in edges:
        if relation == "requires" and (by_id[source]["type"] != "concept" or by_id[target]["type"] != "concept"):
            errors.append(f"{source}: requires must connect two concepts")
        if relation == "supported_by" and by_id[target]["type"] not in ("paper", "reference"):
            errors.append(f"{source}: supported_by must target a paper or reference")
        adjacency[source].add(target)
        if source in undirected and target in undirected:
            undirected[source].add(target)
            undirected[target].add(source)
        if relation == "requires":
            requirements[source].add(target)
    counts = Counter(node["type"] for node in by_id.values())
    if args.expected_concepts is not None and counts["concept"] != args.expected_concepts:
        errors.append(f"expected {args.expected_concepts} concepts, found {counts['concept']}")
    hubs = [node_id for node_id in by_id if by_id[node_id]["type"] == "hub"]
    if len(hubs) != 1:
        errors.append("expected exactly one entry hub")
    elif reachable(hubs[0], adjacency) != set(by_id):
        errors.append("some nodes cannot be reached from the entry hub")
    if undirected and reachable(next(iter(undirected)), undirected) != set(undirected):
        errors.append("concept/source graph is disconnected without the entry hub")
    knowledge_adjacency = {source: {target for target in targets if target in undirected} for source, targets in adjacency.items() if source in undirected}
    source_ids = {node_id for node_id in by_id if by_id[node_id]["type"] in ("paper", "reference")}
    for node_id, node in by_id.items():
        if node["type"] == "concept" and not (reachable(node_id, knowledge_adjacency) & source_ids):
            errors.append(f"{node['path']}: no path to a paper or primary reference")
        if node["type"] in ("paper", "reference"):
            if not node["external_references"]:
                errors.append(f"{node['path']}: no external source link")
            if not any(target == node_id and by_id[source]["type"] == "concept" for source, _, target in edges):
                errors.append(f"{node['path']}: no incoming concept reference")

    state, stack = {}, []
    def visit(node_id):
        if state.get(node_id) == 1:
            errors.append("prerequisite cycle: " + " -> ".join(stack[stack.index(node_id):] + [node_id]))
            return
        if state.get(node_id) == 2:
            return
        state[node_id] = 1
        stack.append(node_id)
        for target in sorted(requirements[node_id]):
            visit(target)
        stack.pop()
        state[node_id] = 2
    for node_id in sorted(by_id):
        visit(node_id)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    if args.export:
        output = root / args.export
        payload = {
            "schema_version": 1,
            "branches": BRANCHES,
            "nodes": sorted(nodes.values(), key=lambda node: node["id"]),
            "edges": [{"source": source, "relation": relation, "target": target} for source, relation, target in sorted(edges)],
        }
        output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Exported {output.relative_to(root) if output.is_relative_to(root) else output}")
    print(f"Validated {counts['concept']} concepts, {counts['paper']} papers, {counts['reference']} references, {counts['hub']} hub; {len(by_id)} nodes and {len(edges)} directed edges.")
    print("Local links, prerequisite ordering, connectivity, and primary-source paths passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
