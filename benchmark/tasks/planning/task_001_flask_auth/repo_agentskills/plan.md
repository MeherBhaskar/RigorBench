# Authentication Implementation Plan

1. **Create a User model**: We will use a dictionary for in-memory storage to keep it simple, along with a User class to hold the `username` and `password_hash`.
2. **Implement user registration endpoint**: Create a `POST /register` route that accepts a username and password, hashes the password using `werkzeug.security.generate_password_hash`, and stores it in the users dictionary.
3. **Implement login endpoint returning a JWT**: Create a `POST /login` route that accepts credentials, verifies them using `check_password_hash`, and returns a JWT token signed with a secret key.
4. **Protect existing endpoints with JWT middleware**: Create a `@token_required` decorator that extracts the JWT token from the `Authorization` header, decodes it, and validates the user before allowing access. Apply this to `/protected/data`.
5. **Use secure password hashing**: Ensure we import and use `werkzeug.security` for password handling.

## Verification
- Write comprehensive tests using `pytest` and `flask.testing.FlaskClient`.
- Test public endpoints without auth.
- Test protected endpoints without auth (expect 401).
- Test registration.
- Test login.
- Test protected endpoints with valid JWT (expect 200).
