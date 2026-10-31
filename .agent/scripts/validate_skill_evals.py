#!/usr/bin/env python3
"""Validate cases, score reported host results, and optionally compare artifacts.

This command never runs a model. Result fields, file changes, actual host
execution and scientific validity are distinct observations.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required. Install development dependencies with "
        "`python -m pip install -r requirements-dev.txt`."
    ) from exc

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CASES = ROOT / ".agent" / "evals" / "skill_trigger_cases.yaml"
DEFAULT_PRODUCT_CASES = ROOT / ".agent" / "evals" / "product_surface_cases.yaml"
DEFAULT_SKILLS_ROOT = ROOT / ".agent" / "skills"
PRODUCT_SURFACES = {
    "manuscript", "code", "experiment", "figure", "submission", "decision", "governance",
}


def _read_yaml(path: Path, label: str) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        return None, [f"{label}: cannot read YAML: {exc}"]
    if not isinstance(data, dict):
        return None, [f"{label}: root must be a mapping"]
    return data, []


def _relative_path(value: Any) -> bool:
    """Accept portable, explicit file paths within a case snapshot."""
    return (
        isinstance(value, str) and bool(value.strip())
        and not Path(value).is_absolute()
        and ".." not in Path(value).parts
        and value not in (".", "") and "\\" not in value and ":" not in value
    )


def _case_list(
    path: Path, *, suite: str, product: bool,
) -> tuple[dict[str, dict[str, Any]], list[str]]:
    data, errors = _read_yaml(path, suite)
    if data is None:
        return {}, errors
    if data.get("schema_version") != 1:
        errors.append(f"{suite}: schema_version must be 1")
    if data.get("suite") != suite:
        errors.append(f"{suite}: suite must equal {suite!r}")
    raw = data.get("cases")
    if not isinstance(raw, list) or not raw:
        return {}, errors + [f"{suite}: cases must be a non-empty list"]

    cases: dict[str, dict[str, Any]] = {}
    for index, case in enumerate(raw):
        location = f"{suite}[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{location}: case must be a mapping")
            continue
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{location}: case_id must be a non-empty string")
            continue
        if case_id in cases:
            errors.append(f"{suite}: duplicate case_id {case_id}")
            continue
        cases[case_id] = case
        for key in ("prompt", "expected_primary"):
            if not isinstance(case.get(key), str) or not case[key].strip():
                errors.append(f"{case_id}.{key} must be a non-empty string")
        forbidden = case.get("must_not_trigger", [])
        if not isinstance(forbidden, list) or not all(isinstance(item, str) for item in forbidden):
            errors.append(f"{case_id}.must_not_trigger must be a string list")
        if case.get("expected_primary") in forbidden:
            errors.append(f"{case_id} forbids its expected primary")
        if product:
            if case.get("expected_primary_surface") not in PRODUCT_SURFACES:
                errors.append(f"{case_id}.expected_primary_surface is invalid")
            for key in ("must_change_product", "audit_allowed"):
                if not isinstance(case.get(key), bool):
                    errors.append(f"{case_id}.{key} must be boolean")
            hidden = case.get("must_not_surface", [])
            if not isinstance(hidden, list) or not all(isinstance(item, str) for item in hidden):
                errors.append(f"{case_id}.must_not_surface must be a string list")
            for key in ("artifact_paths", "protected_paths"):
                if key in case:
                    paths = case[key]
                    if not isinstance(paths, list) or not paths or not all(_relative_path(p) for p in paths):
                        errors.append(f"{case_id}.{key} must be a non-empty relative file path list")
            if "protected_paths" in case and not case.get("artifact_paths"):
                errors.append(f"{case_id}.protected_paths requires artifact_paths")
            if case.get("artifact_paths") and (
                not _relative_path(case_id) or "/" in case_id
            ):
                errors.append(f"{case_id}: snapshot case ID must be one directory name")
        elif not isinstance(case.get("critical"), bool):
            errors.append(f"{case_id}.critical must be boolean")
    return cases, errors


def load_cases(path: Path) -> tuple[dict[str, dict[str, Any]], list[str]]:
    return _case_list(path, suite="papertrace-routing", product=False)


def load_product_cases(path: Path) -> tuple[dict[str, dict[str, Any]], list[str]]:
    return _case_list(path, suite="papertrace-product-surfaces", product=True)


def _read_json(path: Path) -> tuple[Any | None, str | None]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return None, f"{path}: cannot read JSON: {exc}"


def validate_embedded_evals(skills_root: Path) -> tuple[dict[str, dict[str, int]], list[str]]:
    """Check only embedded eval definition files that actually exist."""
    summaries: dict[str, dict[str, int]] = {}
    errors: list[str] = []
    if not skills_root.is_dir():
        return summaries, [f"skills root not found: {skills_root}"]
    for eval_dir in sorted(skills_root.glob("*/evals")):
        skill_name = eval_dir.parent.name
        evals_path = eval_dir / "evals.json"
        queries_path = eval_dir / "eval_queries.json"
        if not evals_path.is_file() and not queries_path.is_file():
            continue
        eval_data, eval_error = _read_json(evals_path)
        query_data, query_error = _read_json(queries_path)
        if eval_error:
            errors.append(eval_error)
            continue
        if query_error:
            errors.append(query_error)
            continue
        if not isinstance(eval_data, dict) or not isinstance(eval_data.get("evals"), list):
            errors.append(f"{evals_path}: expected an object with an evals list")
            continue
        if not isinstance(query_data, list):
            errors.append(f"{queries_path}: expected a list")
            continue
        summaries[skill_name] = {"output_evals": len(eval_data["evals"]), "trigger_queries": len(query_data)}
    return summaries, errors


def load_results(path: Path) -> tuple[dict[str, dict[str, Any]], list[str]]:
    """Load reported host-result JSONL; these fields do not prove execution."""
    results: dict[str, dict[str, Any]] = {}
    errors: list[str] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        return {}, [f"cannot read results: {exc}"]
    for number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"results line {number}: invalid JSON: {exc}")
            continue
        if not isinstance(item, dict):
            errors.append(f"results line {number}: object required")
            continue
        case_id = item.get("case_id")
        selected = item.get("selected_primary")
        if not isinstance(case_id, str) or not isinstance(selected, str):
            errors.append(f"results line {number}: case_id and selected_primary must be strings")
            continue
        if case_id in results:
            errors.append(f"duplicate result for {case_id}")
            continue
        results[case_id] = item
    return results, errors


def _coverage_errors(expected_ids: set[str], result_ids: set[str]) -> list[str]:
    errors: list[str] = []
    missing = sorted(expected_ids - result_ids)
    extra = sorted(result_ids - expected_ids)
    if missing:
        errors.append(f"missing results: {missing}")
    if extra:
        errors.append(f"unknown result case IDs: {extra}")
    return errors


def score_routing(cases: dict[str, dict[str, Any]], results: dict[str, dict[str, Any]]) -> dict[str, Any]:
    evaluated = exact = prohibited = 0
    critical_failures: list[str] = []
    for case_id, case in cases.items():
        result = results.get(case_id)
        if not result:
            continue
        evaluated += 1
        selected = result.get("selected_primary")
        if selected == case.get("expected_primary"):
            exact += 1
        if selected in case.get("must_not_trigger", []):
            prohibited += 1
        if case.get("critical") and selected != case.get("expected_primary"):
            critical_failures.append(case_id)
    return {"evaluated": evaluated, "exact_matches": exact,
            "exact_accuracy": exact / evaluated if evaluated else 0.0,
            "prohibited_triggers": prohibited, "critical_failures": critical_failures}


def score_products(cases: dict[str, dict[str, Any]], results: dict[str, dict[str, Any]]) -> dict[str, Any]:
    evaluated = exact = 0
    failures: list[str] = []
    for case_id, case in cases.items():
        result = results.get(case_id)
        if not result:
            continue
        evaluated += 1
        selected = result.get("selected_primary")
        if selected == case.get("expected_primary"):
            exact += 1
        else:
            failures.append(f"{case_id}: selected_primary={selected!r}")
        if selected in case.get("must_not_trigger", []):
            failures.append(f"{case_id}: prohibited primary triggered: {selected}")
        surface = result.get("primary_surface")
        if surface != case.get("expected_primary_surface"):
            failures.append(f"{case_id}: primary_surface={surface!r}, expected={case.get('expected_primary_surface')!r}")
        changed = result.get("product_changed")
        if not isinstance(changed, bool):
            failures.append(f"{case_id}: product_changed must be boolean")
        elif changed is not case.get("must_change_product"):
            failures.append(f"{case_id}: product_changed={changed}, expected={case.get('must_change_product')}")
        audit_used = result.get("audit_used")
        if not isinstance(audit_used, bool):
            failures.append(f"{case_id}: audit_used must be boolean")
        elif audit_used and not case.get("audit_allowed"):
            failures.append(f"{case_id}: audit was used although audit_allowed=false")
        summary = result.get("user_visible_summary")
        if not isinstance(summary, str):
            failures.append(f"{case_id}: user_visible_summary must be a string")
        else:
            lowered = summary.lower()
            for phrase in case.get("must_not_surface", []):
                if phrase.lower() in lowered:
                    failures.append(f"{case_id}: surfaced prohibited phrase {phrase!r}")
    return {"evaluated": evaluated, "exact_matches": exact,
            "exact_accuracy": exact / evaluated if evaluated else 0.0, "failures": failures}


def _snapshot_bytes(root: Path, case_id: str, relative: str) -> bytes | None:
    """Read a specified artifact, never follow a path outside its case snapshot."""
    if not _relative_path(case_id) or "/" in case_id or not _relative_path(relative):
        raise ValueError("snapshot paths must stay within one case directory")
    case_root = root / case_id
    if not case_root.is_dir() or case_root.is_symlink():
        raise ValueError(f"case snapshot directory missing or linked: {case_root}")
    path = case_root / relative
    if not path.resolve().is_relative_to(case_root.resolve()):
        raise ValueError(f"artifact escapes case snapshot: {relative}")
    if path.is_symlink():
        raise ValueError(f"artifact must be a regular copied file: {relative}")
    if not path.exists():
        return None
    if not path.is_file():
        raise ValueError(f"artifact is not a file: {relative}")
    return path.read_bytes()


def score_artifacts(cases: dict[str, dict[str, Any]], before: Path, after: Path) -> dict[str, Any]:
    """Compare evaluator-specified files; not a semantic or host-provenance test."""
    checked: list[str] = []
    unchecked: list[str] = []
    failures: list[str] = []
    if not before.is_dir() or not after.is_dir() or before.resolve() == after.resolve():
        return {"checked_cases": [], "unchecked_cases": list(cases),
                "failures": ["before and after must be distinct existing snapshot directories"]}
    for case_id, case in cases.items():
        paths = case.get("artifact_paths")
        if not paths:
            unchecked.append(case_id)
            continue
        checked.append(case_id)
        for relative in paths:
            try:
                old = _snapshot_bytes(before, case_id, relative)
                new = _snapshot_bytes(after, case_id, relative)
                if case["must_change_product"]:
                    if not new or new == old:
                        failures.append(f"{case_id}: required artifact missing, empty or unchanged: {relative}")
                elif new != old:
                    failures.append(f"{case_id}: read-only artifact changed: {relative}")
            except (OSError, ValueError) as exc:
                failures.append(f"{case_id}: {exc}")
        for relative in case.get("protected_paths", []):
            try:
                old = _snapshot_bytes(before, case_id, relative)
                new = _snapshot_bytes(after, case_id, relative)
                if old is None or new != old:
                    failures.append(f"{case_id}: protected file missing from baseline or changed: {relative}")
            except (OSError, ValueError) as exc:
                failures.append(f"{case_id}: {exc}")
    return {"checked_cases": checked, "unchecked_cases": unchecked, "failures": failures}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--product-cases", type=Path, default=DEFAULT_PRODUCT_CASES)
    parser.add_argument("--skills-root", type=Path, default=DEFAULT_SKILLS_ROOT)
    parser.add_argument("--results", type=Path, help="score reported JSONL; never executes a model")
    parser.add_argument("--case-id", action="append", help="evaluate only these IDs; repeat to select more")
    parser.add_argument("--before", type=Path, help="pre-run snapshots: ROOT/CASE_ID/relative_path")
    parser.add_argument("--after", type=Path, help="post-run snapshots with the same layout")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if (args.before is None) != (args.after is None) or (args.before is not None and args.results is None):
        parser.error("--before and --after must be supplied together with --results")

    routing, errors = load_cases(args.cases)
    products, product_errors = load_product_cases(args.product_cases)
    embedded, embedded_errors = validate_embedded_evals(args.skills_root)
    errors.extend(product_errors)
    errors.extend(embedded_errors)
    all_ids = set(routing) | set(products)
    if args.case_id:
        requested = set(args.case_id)
        unknown = sorted(requested - all_ids)
        if unknown:
            errors.append(f"unknown selected case IDs: {unknown}")
        routing = {key: value for key, value in routing.items() if key in requested}
        products = {key: value for key, value in products.items() if key in requested}

    routing_metrics: dict[str, Any] | None = None
    product_metrics: dict[str, Any] | None = None
    artifact_metrics: dict[str, Any] | None = None
    results_supplied = args.results is not None
    if args.results:
        results, result_errors = load_results(args.results)
        errors.extend(result_errors)
        if args.case_id:
            unknown_results = set(results) - all_ids
            if unknown_results:
                errors.append(f"unknown result case IDs: {sorted(unknown_results)}")
            results = {key: value for key, value in results.items() if key in set(routing) | set(products)}
        errors.extend(_coverage_errors(set(routing) | set(products), set(results)))
        routing_metrics = score_routing(routing, results)
        product_metrics = score_products(products, results)
    if args.before is not None and not errors:
        artifact_metrics = score_artifacts(products, args.before, args.after)

    failed = bool(errors)
    if results_supplied:
        assert routing_metrics is not None and product_metrics is not None
        failed = failed or bool(
            (routing and routing_metrics["exact_accuracy"] < 1.0)
            or routing_metrics["prohibited_triggers"] or routing_metrics["critical_failures"]
            or (products and product_metrics["exact_accuracy"] < 1.0) or product_metrics["failures"]
        )
    if artifact_metrics:
        failed = failed or bool(artifact_metrics["failures"])
    report = {
        "mode": "host-results" if results_supplied else "definitions-only",
        "behavior_executed": False,
        "host_execution_verified": False,
        "reported_results_scored": results_supplied,
        "routing_case_definitions": len(routing), "product_case_definitions": len(products),
        "embedded_eval_definitions": embedded,
        "routing_metrics": routing_metrics, "product_metrics": product_metrics,
        "artifact_metrics": artifact_metrics, "errors": errors,
    }
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"routing definitions={len(routing)}; product definitions={len(products)}; embedded skill definitions={len(embedded)}")
        for error in errors:
            print(f"ERROR: {error}")
        if not results_supplied:
            print("NOTE: definitions only; no Claude/Codex/LLM behavior was executed.")
        else:
            print("NOTE: reported fields are scored; this command does not execute or authenticate a host run.")
            print(f"routing metrics={routing_metrics}")
            print(f"product metrics={product_metrics}")
        if artifact_metrics is not None:
            print(f"artifact metrics={artifact_metrics}")
            print("NOTE: file changes do not prove semantic correctness or scientific validity.")
        if not failed:
            if not results_supplied:
                print("PASS: routing/product case definitions are valid; behavior not executed.")
            else:
                print("PASS: requested report/file checks passed; host execution is not established.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
