"""Behavior checks for the evidence-log helper."""
import csv
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


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

    def test_quoted_untrusted_cells_round_trip_without_becoming_formulas(self):
        with tempfile.TemporaryDirectory() as directory:
            log = Path(directory) / "decisions.tsv"
            helper = ROOT / "skills/show-me-your-work/scripts/log.sh"
            subprocess.run(["bash", str(helper), str(log), "check", '"=1+1"', 'a "quoted" reason', "  =1+1", "open"], check=True)
            with log.open(newline="") as stream:
                row = next(csv.DictReader(stream, delimiter="\t"))
            self.assertEqual(row["decision"], '"=1+1"')
            self.assertEqual(row["why"], 'a "quoted" reason')
            self.assertEqual(row["evidence"], "'  =1+1")


if __name__ == "__main__":
    unittest.main()
