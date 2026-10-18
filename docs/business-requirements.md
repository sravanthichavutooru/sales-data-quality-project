# Sales Data Quality — Business Requirements

## Project Purpose
Check sales records before using them in reports so that incorrect data can be reviewed.

This is a practice project using fictional sales data.

## Business Problem
Duplicate orders, missing customer details, and incorrect amounts can make sales reports unreliable.

## Users
- Sales analysts who prepare reports
- QA analysts who check data quality
- Data engineers who maintain data pipelines

## Requirements
| ID | Requirement |
| --- | --- |
| BR-01 | Identify every row with a repeated order ID. |
| BR-02 | Identify records with a missing customer ID. |
| BR-03 | Identify quantities that are zero or negative. |
| BR-04 | Identify negative unit prices. |
| BR-05 | Check that total amount equals quantity multiplied by unit price. |
| BR-06 | Identify invalid numeric values. |
| BR-07 | Display the number of records checked and all issues found. |

## User Story
As a sales analyst, I want sales records checked before reporting so that I can review data problems and avoid incorrect totals.

## Acceptance Criteria
- The checker reads the sales CSV file.
- Each issue includes its row number.
- The original data remains unchanged.
- The sample file produces 10 records checked and 5 issues.
- Both rows containing duplicate order 1005 are reported.
- A successful script run does not mean the data has no issues.

## Scope
The project identifies and reports data issues.

Correcting records, approving changes, and creating sales dashboards are outside the current scope.
