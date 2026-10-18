import csv
from collections import Counter
from decimal import Decimal
from pathlib import Path

data_file = Path(__file__).resolve().parents[1] / "data" / "sales.csv"

with data_file.open(newline="", encoding="utf-8-sig") as file:
    rows = list(csv.DictReader(file))

order_counts = Counter(row["order_id"] for row in rows)
issues = []

for line_number, row in enumerate(rows, start=2):
    order_id = row["order_id"]

    if order_counts[order_id] > 1:
        issues.append(f"Line {line_number}: Duplicate order {order_id}")

    if not row["customer_id"].strip():
        issues.append(f"Line {line_number}: Missing customer ID")

    try:
        quantity = int(row["quantity"])
        price = Decimal(row["unit_price"])
        total = Decimal(row["total_amount"])

        if not price.is_finite() or not total.is_finite():
            raise ValueError("Non-finite amount")

    except (ValueError, ArithmeticError):
        issues.append(f"Line {line_number}: Invalid numeric value")
        continue

    if quantity <= 0:
        issues.append(f"Line {line_number}: Quantity must be positive")

    if price < 0:
        issues.append(f"Line {line_number}: Price cannot be negative")

    if quantity * price != total:
        issues.append(f"Line {line_number}: Incorrect total for order {order_id}")

print(f"Checked {len(rows)} sales records.")
print(f"Found {len(issues)} issues.")

for issue in issues:
    print(f"- {issue}")
