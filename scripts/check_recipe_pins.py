#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Verify every pinned p4a_recipes/*/__init__.py version resolves on TestPyPI.

This is the check that would have caught the pydevices==0.0.17 /
pydevices-palettes==0.0.8 pin rot: both were repo-local floors that had
drifted behind (or, for 0.0.17, never matched) any version TestPyPI ever
published. Recipes with ``version = None`` (unpinned, resolved at build
time) are skipped -- there is nothing to verify.
"""
import ast
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECIPES_DIR = ROOT / "p4a_recipes"


def parse_recipe(init_py: Path):
    """Return (pip_name, version) or (name, None) if unpinned."""
    src = init_py.read_text()
    tree = ast.parse(src, filename=str(init_py))

    name = None
    version = None
    pip_name = None

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for stmt in node.body:
                if isinstance(stmt, ast.Assign):
                    target = stmt.targets[0]
                    if not isinstance(target, ast.Name):
                        continue
                    if target.id == "name":
                        name = ast.literal_eval(stmt.value)
                    elif target.id == "version":
                        try:
                            version = ast.literal_eval(stmt.value)
                        except ValueError:
                            version = None
                elif isinstance(stmt, ast.FunctionDef) and stmt.name == "get_pip_name":
                    for sub in ast.walk(stmt):
                        if isinstance(sub, ast.Return) and isinstance(sub.value, ast.Constant):
                            pip_name = sub.value.value

    return (pip_name or name), version


def check(pip_name: str, version: str) -> bool:
    url = f"https://test.pypi.org/pypi/{pip_name}/json"
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.load(resp)
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL  {pip_name}: could not fetch {url}: {exc}")
        return False

    releases = data.get("releases", {})
    if version in releases and releases[version]:
        print(f"OK    {pip_name}=={version}")
        return True

    latest = data.get("info", {}).get("version", "?")
    print(f"FAIL  {pip_name}=={version} not found on TestPyPI (latest: {latest})")
    return False


def main() -> int:
    ok = True
    for init_py in sorted(RECIPES_DIR.glob("*/__init__.py")):
        pip_name, version = parse_recipe(init_py)
        if version is None:
            print(f"SKIP  {pip_name} (version = None, resolved at build time)")
            continue
        if not check(pip_name, version):
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
