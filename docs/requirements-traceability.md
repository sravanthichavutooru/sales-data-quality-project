# Requirements Traceability

This table connects business requirements with implementation and verification.

| ID | Business Rule | Implementation | Verification |
| --- | --- | --- | --- |
| BR-01 | Identify duplicate orders | Python and SQL | Original sample regression test |
| BR-02 | Identify missing customer IDs | Python and SQL | Original sample regression test |
| BR-03 | Identify zero or negative quantities | Python and SQL | Negative quantity in sample; separate zero-quantity test |
| BR-04 | Identify negative prices | Python and SQL | Separate negative-price test |
| BR-05 | Identify incorrect totals | Python and SQL | Incorrect total in sample; separate valid-record test |
| BR-06 | Identify invalid numeric values | Python | Separate invalid-quantity test |
| BR-07 | Display record count and issues | Python | Original sample regression test |

## Automated Test Coverage
Five Python tests passed:
1. Original sample results
2. Zero quantity
3. Negative unit price
4. Invalid quantity
5. Valid record

Additional scenarios use temporary data and leave the original sample unchanged.

## Coverage Limits
The additional scenario tests verify the Python checker.
SQL queries run in the workflow, but their results do not yet have automated assertions.
Invalid numeric testing currently covers quantity only.
