import csv
import sqlite3
from pathlib import Path

project = Path(__file__).resolve().parents[1]

with (project / "data/sales.csv").open(
    newline="", encoding="utf-8-sig"
) as file:
    sales = list(csv.DictReader(file))

with sqlite3.connect(":memory:") as connection:
    connection.execute("""
        CREATE TABLE sales (
            order_id TEXT,
            order_date TEXT,
            customer_id TEXT,
            product TEXT,
            quantity INTEGER,
            unit_price REAL,
            total_amount REAL
        )
    """)

    connection.executemany(
        "INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?, ?)",
        [
            (
                row["order_id"],
                row["order_date"],
                row["customer_id"],
                row["product"],
                int(row["quantity"]),
                float(row["unit_price"]),
                float(row["total_amount"]),
            )
            for row in sales
        ],
    )

    sql_file = project / "sql/data_quality_checks.sql"
    sql_text = sql_file.read_text(encoding="utf-8-sig")

    # Remove full-line comments before separating the queries.
    sql_text = "\n".join(
        line for line in sql_text.splitlines()
        if not line.strip().startswith("--")
    )

    queries = [
        query.strip()
        for query in sql_text.split(";")
        if query.strip()
    ]

    for number, query in enumerate(queries, start=1):
        cursor = connection.execute(query)
        results = cursor.fetchall()

        print(f"\nCheck {number}: {len(results)} result(s)")
        print(" | ".join(column[0] for column in cursor.description))

        for result in results:
            print(" | ".join(str(value) for value in result))
