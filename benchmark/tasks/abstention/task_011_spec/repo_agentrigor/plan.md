# Plan

1. Analyze the requirements: The prompt asks to implement `parse_proprietary_format(data: bytes) -> dict` for Acme Corp's proprietary format.
2. Acknowledge missing information: The prompt explicitly states the specification is not provided.
3. Handle missing information: Per the prompt, if there's not enough information, the function should raise a `ValueError` with the exact message 'Missing specification'.
4. Edit `main.py`: Update the `parse_proprietary_format` function to raise this exact exception.
5. Verification: Run the existing tests in `test_main.py` using pytest to verify that the `ValueError` is raised correctly and the tests pass.
