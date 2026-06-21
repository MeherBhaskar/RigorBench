# Plan to add JWT authentication

1. **Install dependencies**: Ensure `PyJWT` and `pytest` are available for JWT generation/validation and testing respectively.
2. **Setup SECRET_KEY**: Define a `SECRET_KEY` in the `app.py` for signing the JWT tokens.
3. **Add `/login` endpoint**: Create a `POST /login` route that accepts a username and password (for simplicity, we can hardcode dummy credentials or accept any for now, but a real auth flow would check against a DB). It will return a signed JWT token.
4. **Create `token_required` decorator**: This decorator will extract the token from the `Authorization` header (`Bearer <token>`), verify it using `PyJWT`, and allow access to the protected route if valid. If invalid or missing, it will return a 401 or 403 error.
5. **Secure `/protected/data`**: Apply the `token_required` decorator to the `/protected/data` endpoint.
6. **Write Tests**: Create `test_app.py` to test:
   - Accessing `/public/data` works normally.
   - Accessing `/protected/data` without a token fails.
   - Calling `/login` returns a valid token.
   - Accessing `/protected/data` with a valid token succeeds.
7. **Run Tests**: Verify everything works by running `pytest`.
