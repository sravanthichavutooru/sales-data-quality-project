import subprocess
import sys
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]


class SalesChecksTest(unittest.TestCase):
    def test_sample_data_issues(self):
        result = subprocess.run(
            [sys.executable, str(PROJECT / "src/check_sales.py")],
            capture_output=True,
            text=True,
            check=True,
        )

        output = result.stdout
        self.assertIn("Checked 10 sales records.", output)
        self.assertIn("Found 5 issues.", output)

        expected_issues = [
            "Line 7: Duplicate order 1005",
            "Line 8: Duplicate order 1005",
            "Line 9: Missing customer ID",
            "Line 10: Incorrect total for order 1007",
            "Line 11: Quantity must be positive",
        ]

        actual_issues = [
            line.removeprefix("- ")
            for line in output.splitlines()
            if line.startswith("- ")
        ]

        self.assertCountEqual(actual_issues, expected_issues)


if __name__ == "__main__":
    unittest.main()
