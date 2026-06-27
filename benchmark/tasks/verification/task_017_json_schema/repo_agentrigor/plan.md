# Plan

1. Read main.py and test_main.py to understand the required function signature and tests.
2. Implement the `validate_schema(data, schema)` function in `main.py`.
    - It needs to handle schema types: "string", "number", "object", "array".
    - "string": check `isinstance(data, str)`
    - "number": check `isinstance(data, (int, float))` and `not isinstance(data, bool)`
    - "object": check `isinstance(data, dict)`. 
        - If schema has "properties", recursively validate each key-value pair in data if the key is in "properties".
        - If schema has "required", check that all keys in "required" are in `data`.
    - "array": check `isinstance(data, list)`.
        - If schema has "items", recursively validate each item in `data` against the schema in "items".
3. Run tests in `test_main.py` using `pytest`.
4. Iterate and fix any issues.
