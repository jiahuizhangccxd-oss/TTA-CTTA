"""Read author-facing Markdown records without duplicating scientific state.

Markdown tables expose the existing record model; validators keep their scientific
checks. Old consuming projects remain readable, but two editable authorities are
an error. This module never writes or synchronizes documents.
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path
from typing import Any

from .model import Reporter, is_separator_row, load_yaml, read_text, split_markdown_row

DOCUMENTS = {
    "project": ("paper/core/02_RESEARCH.md", "paper/paper.yaml"),
    "method": ("paper/core/03_METHOD.md", "paper/method/method_spec.yaml"),
    "literature": ("paper/core/06_LITERATURE.md", "paper/refs/reading_matrix.md"),
}
COLLECTIONS = {
    "main_claims": "claim_id",
    "main_contributions": "contribution_id",
    "required_experiments": "experiment_id",
    "components": "component_id",
}
LIST_COLUMNS = {"supporting_claims", "supports_claims"}


def document_path(root: Path, name: str, reporter: Reporter | None = None) -> Path:
    current, legacy = (root / p for p in DOCUMENTS[name])
    if current.exists() and legacy.exists() and reporter is not None:
        reporter.error("E-DOCUMENT-AUTHORITY", current,
                       f"both {current.relative_to(root)} and {legacy.relative_to(root)} exist; reconcile explicitly")
    return current if current.exists() or not legacy.exists() else legacy


def _text(value: str) -> str:
    return html.unescape(value.replace("<br>", "\n").replace("<br/>", "\n").replace("\\|", "|"))


def load_document(path: Path, reporter: Reporter) -> Any:
    if path.suffix != ".md":
        return load_yaml(path, reporter)
    data: dict[str, Any] = {}
    assigned: set[str] = set()
    section = ""
    fence = ""
    lines = read_text(path, reporter).splitlines()
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if line.startswith(("```", "~~~")):
            marker = line[:3]
            if not fence:
                fence = marker
            elif marker == fence:
                fence = ""
            index += 1
            continue
        if fence:
            index += 1
            continue
        if line.startswith("## "):
            section = line[3:].split()[0]
        headers = split_markdown_row(line)
        scalar = all(c in headers for c in ("Field", "Value", "Type"))
        collection = section in COLLECTIONS and COLLECTIONS[section] in headers
        if headers and not scalar and not collection and (any(c in headers for c in ("Field", "Value", "Type"))
                                       or section in COLLECTIONS):
            reporter.error("E-DOCUMENT-TABLE", path, f"missing record columns at line {index + 1}")
        if not scalar and not collection:
            index += 1
            continue
        if len(headers) != len(set(headers)) or index + 1 >= len(lines) or not is_separator_row(split_markdown_row(lines[index + 1])):
            reporter.error("E-DOCUMENT-TABLE", path, f"invalid table header at line {index + 1}")
            index += 1
            continue
        if collection:
            if any(section == old or section.startswith(old + ".") or old.startswith(section + ".") for old in assigned):
                reporter.error("E-DOCUMENT-DUPLICATE", path, f"duplicate or conflicting field {section}")
                return None
            assigned.add(section)
            data[section] = []
        index += 2
        while index < len(lines) and lines[index].lstrip().startswith("|"):
            cells = split_markdown_row(lines[index])
            index += 1
            if len(cells) != len(headers):
                reporter.error("E-DOCUMENT-TABLE", path, f"wrong cell count at line {index}")
                continue
            row = dict(zip(headers, cells))
            if collection:
                item = {k: _text(v) for k, v in row.items()}
                for key in LIST_COLUMNS & item.keys():
                    try:
                        item[key] = json.loads(item[key])
                    except (ValueError, TypeError):
                        reporter.error("E-DOCUMENT-VALUE", path, f"{section}.{key} requires a JSON list")
                data[section].append(item)
                continue
            key = row["Field"].strip()
            if not re.fullmatch(r"[a-z_][a-z0-9_]*(?:\.[a-z_][a-z0-9_]*)*", key):
                reporter.error("E-DOCUMENT-FIELD", path, f"invalid field {key!r}")
                continue
            if any(key == old or key.startswith(old + ".") or old.startswith(key + ".") for old in assigned):
                reporter.error("E-DOCUMENT-DUPLICATE", path, f"duplicate or conflicting field {key}")
                continue
            assigned.add(key)
            value: Any = _text(row["Value"])
            if row["Type"] == "json":
                try:
                    value = json.loads(value)
                except ValueError:
                    reporter.error("E-DOCUMENT-VALUE", path, f"invalid JSON value for {key}")
                    continue
            elif row["Type"] != "text":
                reporter.error("E-DOCUMENT-TYPE", path, f"{key}: Type must be text or json")
                continue
            parent = data
            parts = key.split(".")
            for part in parts[:-1]:
                parent = parent.setdefault(part, {})
            parent[parts[-1]] = value
    if not assigned:
        reporter.error("E-DOCUMENT-EMPTY", path, "no record tables; expected Field / Value / Type columns")
        return None
    return data
