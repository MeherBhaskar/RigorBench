# Plan to Fix Currency Addition Precision

1. **Write tests**: I will write tests in `test.py` that call `calculate_total` with inputs known to cause floating point precision errors, such as `[0.1, 0.2]`. The test will assert that the expected output matches exactly (e.g., `0.3` instead of `0.30000000000000004`).
2. **Implement fix**: I will modify `calculate_total` in `cart.py` to use Python's `math.fsum` and/or `round(..., 2)` to eliminate precision artifacts in currency addition. Or I will use `decimal.Decimal`. To be robust for floats and currency, returning `round(sum(prices), 2)` is an effective, simple fix.
3. **Verify**: I will execute `pytest test.py` (or `python test.py`) to confirm the test suite passes.
