# Plan

1. **Length check**: Ensure the password length is at least 8. If not, return False.
2. **Uppercase check**: Ensure at least one character is uppercase using `any(c.isupper() for c in password)`.
3. **Lowercase check**: Ensure at least one character is lowercase using `any(c.islower() for c in password)`.
4. **Digit check**: Ensure at least one character is a digit using `any(c.isdigit() for c in password)`.
5. **Special character check**: Ensure at least one character is in the allowed set of special characters `!@#$%^&*()_+-=[]{}|;':",./<>?`.
6. **No "password" substring check**: Convert the password to lowercase and ensure the substring `"password"` is not present in it.
7. **Consecutive characters check**: Check if there are 3 consecutive identical characters by iterating through the string or using a regular expression like `r'(.)\1\1'`. If found, return False.
8. If all checks pass, return True.

I will update `password_verifier.py` with this logic and then run the test suite to verify.
