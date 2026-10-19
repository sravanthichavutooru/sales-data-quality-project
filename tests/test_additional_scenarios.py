import csv
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]


class AdditionalSalesTests(unittest.TestCase):
    def run_checker(self, quantity="2", price="20", total="40"):
        # Run a copy of the checker against separate test data.
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "src").mkdir()
            (root / "data").mkdir()

            shutil.copy2(
                PROJECT / "src/check_sales.py",
                root / "src/check_sales.py",
            )

            with (root / "data/sales.csv").open(
                "w", newline="", encoding="utf-8"
            ) as file:
                writer = csv.writer(file)
                writer.writerow([
                    "order_id", "order_date", "customer_id",
                    "product", "quantity", "unit_price",
                    "total_amount",
                ])
                writer.writerow([
                    "2001", "2026-01-10", "C010",
                    "Mouse", quantity, price, total,
                ])

            result = subprocess.run(
                [sys.executable, str(root / "src/check_sales.py")],
                capture_output=True,
                text=True,
                check=True,
            )

            return [
                line.removeprefix("- ")
                for line in result.stdout.splitlines()
                if line.startswith("- ")
            ]

    def test_zero_quantity(self):
        self.assertEqual(
            self.run_checker(quantity="0", total="0"),
            ["Line 2: Quantity must be positive"],
        )

    def test_negative_price(self):
        self.assertEqual(
            self.run_checker(quantity="1", price="-20", total="-20"),
            ["Line 2: Price cannot be negative"],
        )

    def test_invalid_quantity(self):
        self.assertEqual(
            self.run_checker(quantity="abc"),
            ["Line 2: Invalid numeric value"],
        )

    def test_valid_record(self):
        self.assertEqual(self.run_checker(), [])


if __name__ == "__main__":
    unittest.main()
