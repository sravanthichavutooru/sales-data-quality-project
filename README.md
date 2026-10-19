## Automated Testing

A regression test checks that the original sample produces:
- 10 records checked
- 5 issues found
- The expected messages for duplicates, a missing customer ID, an incorrect total, and a negative quantity

Run the test locally:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs this test automatically before running the Python and SQL checks.

This test covers the original sample. Additional scenarios, including invalid numeric values and negative prices, still need separate tests.
