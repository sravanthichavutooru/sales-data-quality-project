# Requirements Traceability

This table connects business requirements to implementation and testing.

| Requirement | Business Rule | Implementation | UAT Case | Verification |
| --- | --- | --- | --- | --- |
| BR-01 | Identify duplicate orders | Python and SQL | UAT-01 | Original sample checked |
| BR-02 | Identify missing customer IDs | Python and SQL | UAT-02 | Original sample checked |
| BR-03 | Identify zero or negative quantities | Python and SQL | UAT-03, UAT-06 | Negative quantity checked; zero pending |
| BR-04 | Identify negative prices | Python and SQL | UAT-07 | Negative-price scenario pending |
| BR-05 | Identify incorrect totals | Python and SQL | UAT-04, UAT-09 | Incorrect total checked; separate valid-record scenario pending |
| BR-06 | Identify invalid numeric values | Python checker | UAT-08 | Invalid-value scenario pending |
| BR-07 | Display record count and issues | Python checker | UAT-05 | Original sample checked |

## Automated Coverage
The regression test checks the original sample's record count and five expected issue messages.

## Pending Testing
- Zero quantity
- Negative unit price
- Invalid numeric value
- Separate valid-record scenario

Implementation alone does not confirm that a requirement has been fully tested.
