## SQL Data Quality Checks
The project loads sample sales data into a temporary SQLite database and runs five SQL checks.

- Duplicate order IDs
- Missing customer IDs
- Zero or negative quantities
- Negative unit prices
- Incorrect totals

Both Python and SQL checks run through GitHub Actions.

### SQL Files
- [SQL queries](sql/data_quality_checks.sql)
- [Python SQL runner](src/run_sql_checks.py)d created for this portfolio project.
