"""Behavior checks for the companion installer and evidence-log helper."""
import csv
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts/install-agents.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def test_install_is_idempotent_and_preserves_local_edits(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory)
            installer.install(["local"], destination)
            target = destination / "pstack-reviewer-local.md"
            first = target.read_bytes()
            installer.install(["local"], destination)
            self.assertEqual(target.read_bytes(), first)
            target.write_text("local customization\n")
            with self.assertRaisesRegex(ValueError, "differs"):
                installer.install(["local", "openai"], destination)
            self.assertEqual(target.read_text(), "local customization\n")
            self.assertFalse((destination / "pstack-reviewer-openai.md").exists())

    def test_refuses_symlinks_and_invalid_names_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory)
            victim = destination / "custom.md"
            victim.write_text("keep me")
            (destination / "pstack-reviewer-local.md").symlink_to(victim)
            with self.assertRaisesRegex(ValueError, "symlink"):
                installer.install(["openai", "local"], destination)
            with self.assertRaisesRegex(ValueError, "Unknown"):
                installer.install(["../custom"], destination)
            self.assertEqual(victim.read_text(), "keep me")
            self.assertFalse((destination / "pstack-reviewer-openai.md").exists())


class DecisionLogTests(unittest.TestCase):
    def test_append_and_sanitize_untrusted_cells(self):
        with tempfile.TemporaryDirectory() as directory:
            log = Path(directory) / "nested" / "decisions.tsv"
            helper = ROOT / "skills/show-me-your-work/scripts/log.sh"
            subprocess.run(["bash", str(helper), str(log), "check", "=1+1", "why\tline\nnext", "@artifact", "open"], check=True)
            subprocess.run(["bash", str(helper), str(log), "verify", "+formula", "reason", "-path", "pass"], check=True)
            with log.open(newline="") as stream:
                rows = list(csv.DictReader(stream, delimiter="\t"))
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["decision"], "'=1+1")
            self.assertEqual(rows[0]["why"], "why line next")
            self.assertEqual(rows[0]["evidence"], "'@artifact")
            self.assertEqual(rows[1]["decision"], "'+formula")
            self.assertEqual(rows[1]["evidence"], "'-path")
            self.assertEqual(rows[1]["result"], "pass")


if __name__ == "__main__":
    unittest.main()
