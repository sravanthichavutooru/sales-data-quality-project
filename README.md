## Automated Testing

Five automated Python tests cover:
- Expected issues in the original sample
- Zero quantity
- Negative unit price
- Invalid quantity
- A valid sales record

Additional scenarios use temporary data, leaving the original sample unchanged.

Run all tests:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs these tests before the Python and SQL checks.

SQL query results do not yet have automated assertions.
- 
