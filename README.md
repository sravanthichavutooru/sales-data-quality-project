# Sales Data Quality Project

A practice project that combines Python data validation, QA checks, and business analysis documentation.

## Business Problem
Sales reports can become unreliable when records contain duplicate orders, missing customer details, or incorrect amounts.

This project checks fictional sales data and reports issues for review.

## Tools Used
- Python: CSV processing and validation
- GitHub Actions: Automatic script execution
- Markdown: Business requirements and UAT documentation

No additional Python packages are required.

## Data Quality Checks
- Duplicate order IDs
- Missing customer IDs
- Zero or negative quantities
- Negative unit prices
- Incorrect order totals
- Invalid numeric values

## Project Files
- [Sample sales data](data/sales.csv)
- [Python checker](src/check_sales.py)
- [GitHub Actions workflow](.github/workflows/check-sales.yml)
- [Business requirements](docs/business-requirements.md)
- [UAT test cases](docs/uat-test-cases.md)

## Run Locally
Install Python 3.12, download this repository, and run this command from the repository folder:

```bash
python src/check_sales.py
```

## Run on GitHub
Open Actions, select Sales Data Quality Check, and view the latest run.

The workflow also runs when changes are pushed or a pull request is opened.

## Verified Sample Results
The initial run checked 10 records and found 5 issues:
- Two rows containing duplicate order 1005
- One missing customer ID
- One incorrect order total
- One negative quantity

Both duplicate rows are counted separately.

## Skills Demonstrated
- Data Engineering: Reading CSV data and applying validation rules
- QA: Checking expected results and documenting test scenarios
- Business Analysis: Defining requirements and acceptance criteria
- Automation: Running Python through GitHub Actions

## Current Limitations
The checker reports issues without correcting the source data.
A green workflow means the script completed successfully, even when data issues are found.

Additional UAT scenarios are documented but have not yet been executed.
SQL analysis is planned for a future update.

## Data Source
All sample records are fictional and created for this portfolio project.
