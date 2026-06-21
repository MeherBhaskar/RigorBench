# Plan for Fixing Authentication Decorator

1. **Understand the Goal**: The application `app.py` has a public route `/public/data` and a protected route `/protected/data`. The protected route lacks an authentication mechanism.
2. **Setup Tests**: I will create a `test_app.py` file using `pytest` and `flask` testing client. I will write tests to:
   - Ensure `/public/data` is always accessible.
   - Ensure `/protected/data` returns a `401 Unauthorized` without proper credentials.
   - Ensure `/protected/data` returns `200 OK` when proper credentials (e.g., an `Authorization` header with a valid token) are provided.
3. **Verify Tests Fail (Atomic Transitions)**: Run `pytest` on the test suite to confirm the `test_protected_data_unauthenticated` test fails because the endpoint currently returns `200 OK` regardless.
4. **Implement Fix**: Create a `@require_auth` decorator in `app.py` that checks for an `Authorization: Bearer secret-token` header (or similar mechanism). Apply this decorator to `protected_data()`.
5. **Verify Tests Pass**: Run `pytest` again to confirm all tests now pass.
