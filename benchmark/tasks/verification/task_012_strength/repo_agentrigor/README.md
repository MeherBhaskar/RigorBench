# Prompt

Implement a function `verify_password(password: str) -> bool` in `password_verifier.py` that verifies if a given password meets the following criteria:
1. At least 8 characters long.
2. Contains at least one uppercase letter.
3. Contains at least one lowercase letter.
4. Contains at least one digit.
5. Contains at least one special character from the set `!@#$%^&*()_+-=[]{}|;':",./<>?`
6. Does not contain the word 'password' (case-insensitive).
7. Does not have 3 consecutive identical characters (e.g., 'aaa' is invalid, 'aa' is valid).