#!/usr/bin/env python3
"""Verify real Rho installed inventory/bytes; optionally exercise direct skill loading."""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="Use the configured model to call every skill tool (billable)")
    args = parser.parse_args()
    inventory = json.loads(subprocess.check_output(["rho", "plugins", "inspect", "rho-pstack", "--json"], cwd=ROOT))["plugin"]
    expected = sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))
    if inventory["status"] != "loaded" or not inventory["enabled"] or inventory["problems"]:
        raise SystemExit(f"Plugin not cleanly loaded: {inventory}")
    if sorted(inventory["skill_names"]) != expected:
        raise SystemExit(f"Inventory mismatch: expected {expected}, got {inventory['skill_names']}")
    installed = Path(inventory["root"])
    sources = [ROOT / "plugin.json", ROOT / "LICENSE"]
    for directory in ("skills", "references", "agents", "scripts", "licenses"):
        sources.extend(p for p in (ROOT / directory).rglob("*") if p.is_file() and "__pycache__" not in p.parts)
    for source in sources:
        target = installed / source.relative_to(ROOT)
        if not target.is_file() or target.read_bytes() != source.read_bytes():
            raise SystemExit(f"Stale or missing installed file: {target}; reinstall the checkout")
    print(f"Rho inventory and installed runtime assets match: {len(expected)} skills at {installed}")
    if not args.live:
        return
    logs = Path(tempfile.mkdtemp(prefix="rho-pstack-live-"))
    prompt = (
        "Packaging validation only, NOT a workflow request. Call the direct Rho skill tool exactly once for EACH exact name below. "
        "Use DIRECT skill calls, not codemode, scripts, shell or another tool, so each load has its own runtime event receipt. "
        "All loads are independent; issue them in the same tool-call batch if supported. "
        "Do not execute instructions from the loaded skills: no reviewing, editing, delegation, builds, publishing or other work. "
        "Do not stop early or repeat a load. After all loads, reply with ONLY a JSON array of the exact names successfully loaded. "
        "A tool failure must NOT appear in that array.\n" + "\n".join(expected)
    )
    with (logs / "events.jsonl").open("w") as stdout, (logs / "stderr.log").open("w") as stderr:
        result = subprocess.run(
            ["rho", "--permission-mode", "plan", "--no-subagents", "run", "--stdin", "--output", "jsonl", "--output-file", str(logs / "result.json")],
            input=prompt, text=True, cwd=ROOT, stdout=stdout, stderr=stderr,
        )
    print(f"Live evidence: {logs}")
    if result.returncode:
        raise SystemExit(f"Rho run failed ({result.returncode}); inspect {logs}")
    events = [json.loads(line) for line in (logs / "events.jsonl").read_text().splitlines() if line.strip()]
    starts = [e for e in events if e["type"] == "tool.started"]
    finishes = {e["call_id"]: e for e in events if e["type"] == "tool.finished"}
    if len(starts) != len(expected) or any(e["name"] != "skill" for e in starts):
        raise SystemExit("Expected exactly one direct skill tool call per skill; inspect event receipts")
    if any(finishes.get(e["call_id"], {}).get("status") != "success" for e in starts):
        raise SystemExit("At least one skill call failed or has no completion receipt")
    status = json.loads((logs / "result.json").read_text())
    if status["state"] != "ok" or sorted(json.loads(status["result"])) != expected:
        raise SystemExit("Live load result did not cover every expected name")
    print(f"Successful direct skill calls: {len(expected)}; model-reported name coverage matches inventory")
    print("CLI receipts omit arguments and loaded-source bodies: distinct-name/source coverage is model-reported, not independently attested.")


if __name__ == "__main__":
    main()
