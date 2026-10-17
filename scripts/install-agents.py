#!/usr/bin/env python3
"""Explicit companion install: Rho plugins do not discover package agent files."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRESETS = {
    "matt": ("openai", "cliproxy", "local"),
    "native": ("openai", "anthropic", "google", "xai", "local"),
}


def install(names: list[str], destination: Path) -> list[str]:
    """Preflight the entire selection; never overwrite differing files or symlinks."""
    sources = []
    for name in dict.fromkeys(names):
        if name not in {p.stem.removeprefix("pstack-reviewer-") for p in (ROOT / "agents").glob("*.md")}:
            raise ValueError(f"Unknown reviewer: {name!r}")
        source = ROOT / "agents" / f"pstack-reviewer-{name}.md"
        target = destination / source.name
        data = source.read_bytes()
        if target.is_symlink():
            raise ValueError(f"Refusing symlink: {target}")
        if target.exists() and (not target.is_file() or target.read_bytes() != data):
            raise ValueError(f"Existing reviewer differs; inspect it before updating: {target}")
        sources.append((target, data))
    destination.mkdir(parents=True, exist_ok=True)
    results = []
    for target, data in sources:
        if target.exists():
            results.append(f"Unchanged {target}")
            continue
        # Exclusive creation protects an existing file even if it appears after preflight.
        with target.open("xb") as output:
            output.write(data)
        results.append(f"Installed {target}")
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preset", choices=PRESETS, default="matt")
    parser.add_argument("--only", action="append", help="Reviewer suffix; repeat to select several instead of a preset")
    parser.add_argument("--destination", type=Path, default=Path.home() / ".rho" / "agents")
    args = parser.parse_args()
    try:
        for result in install(args.only or list(PRESETS[args.preset]), args.destination):
            print(result)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Reviewer installation failed: {error}\n")


if __name__ == "__main__":
    main()
