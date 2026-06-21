# Plan

1. **Understand the Bug**: `config.py` defines `multiplier` as `"5"` (a string) instead of `5` (an int). This causes `get_timeout()` in `utils.py` to multiply an integer by a string, which does string repetition rather than mathematical multiplication (or causes TypeError elsewhere). The underlying fix is to change `"5"` to `5`.
2. **Fix the Bug**: Modify `config.py` to use `5` instead of `"5"`.
3. **Write Tests**: Create a `test_config.py` file to test that `get_timeout()` returns the correct integer `50`.
4. **Verify**: Run `pytest test_config.py` to ensure everything works correctly.
