#!/usr/bin/env python3
"""Check package-relative links, names, licenses and installable inventory (no network)."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def check(root: Path) -> list[str]:
    errors = []
    manifest = json.loads((root / "plugin.json").read_text())
    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("Manifest must target Agent Plugins 1.0.0")
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        text = path.read_text()
        match = re.search(r"^name: (.+)$", text, re.M)
        if not match or match[1] != path.parent.name:
            errors.append(f"Skill name must match directory: {path}")
        if "disable-model-invocation: false" not in text.split("---", 2)[1]:
            errors.append(f"Expected explicit model-invocation policy: {path}")
    for path in sorted(root.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        for link in re.findall(r"\]\(([^)\s]+)\)", path.read_text()):
            if "://" in link or link.startswith(("#", "mailto:")):
                continue
            local = link.split("#", 1)[0]
            # Template examples such as (url) are not package paths.
            if not local or not ("/" in local or Path(local).suffix):
                continue
            target = (path.parent / local).resolve()
            if not target.is_relative_to(root.resolve()):
                errors.append(f"Link escapes package: {path.relative_to(root)} -> {link}")
            elif not target.exists():
                errors.append(f"Missing link target: {path.relative_to(root)} -> {link}")
    for name, owner in (("pstack-MIT.txt", "Lauren Tan"), ("thermos-MIT.txt", "Cursor")):
        text = (root / "licenses" / name).read_text()
        if f"Copyright (c) 2026 {owner}" not in text or "Permission is hereby granted" not in text:
            errors.append(f"Missing upstream MIT notice: {name}")
    return errors


if __name__ == "__main__":
    errors = check(ROOT)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print(f"Package checks passed: {len(list((ROOT / 'skills').glob('*/SKILL.md')))} skills")
