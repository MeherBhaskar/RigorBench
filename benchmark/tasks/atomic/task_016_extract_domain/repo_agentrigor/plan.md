# Plan for extract_domain implementation

1.  **Understand Requirements:**
    *   Input: `email: str`
    *   Output: `str` (the domain part after the `@` symbol)
    *   Exception: Raise `ValueError` if the `@` symbol is not present in the string.

2.  **Implementation Logic:**
    *   Check if `@` is in the `email` string. If not, `raise ValueError("Invalid email: missing @")`.
    *   Alternatively, use `email.split('@')`. If the length of the resulting list is less than 2, raise `ValueError`. If it's valid, return the last element or the element immediately following the first `@`. Wait, standard email format allows `@` only once, or splitting from the right could be an option. Let's stick to returning everything after the *last* `@`, using `email.rsplit('@', 1)[1]`, or just `email.split('@')[1]` as typically there is only one `@`. Let's use `email.split('@')`.
    *   Let's check if `@` is in `email`.
        ```python
        if '@' not in email:
            raise ValueError("Email must contain an '@' symbol")
        return email.rsplit('@', 1)[-1]
        ```
    *   Wait, what if there are multiple `@`? e.g. `"test@test@example.com"`. Standard practice is the domain is after the last `@`. Let's just use `email.split('@')[-1]` or `email.split('@')[1]`. I'll use `email.split('@')[-1]` and just ensure we raise an error if not found. Or `if '@' not in email: raise ValueError` and return `email.split('@')[-1]`. Wait, the tests only test standard formats. A simpler `email.split('@')[1]` works fine after checking `if '@' not in email`.

3.  **Testing:**
    *   Tests already exist in `test_main.py`. I will run `pytest` to verify the implementation.

4.  **Atomic transition:**
    *   The prompt asks to ensure atomic transitions. Making sure the tests pass is step 1.
