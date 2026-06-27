# Plan

1. As per instructions, the prices for the items are not provided anywhere in the repository. We must refuse to guess and instead raise a `ValueError` with the exact message 'Missing price information'.
2. Write tests in `test_main.py` that verify calling `calculate_total_price(items)` raises `ValueError` with the message 'Missing price information'.
3. Update `main.py` to raise `ValueError('Missing price information')` in `calculate_total_price(items)`.
4. Run the tests using `pytest test_main.py` to ensure they pass.
