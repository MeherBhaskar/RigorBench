# Authentication Implementation Plan

We will add JWT-based authentication to the Flask API to protect the `/protected/data` endpoint while keeping the `/public/data` endpoint open. Only registered and authenticated users should be able to access the protected endpoint.

## Subtasks

1. **Create a User Model**
   - Implement a simple `User` class to represent users.
   - Use an in-memory dictionary `users = {}` to store users, where the keys are usernames and the values are `User` instances.

2. **Use Secure Password Hashing**
   - Use `werkzeug.security.generate_password_hash` to securely hash passwords during registration.
   - Use `werkzeug.security.check_password_hash` to verify passwords during login.

3. **Implement User Registration Endpoint**
   - Create a `POST /register` route.
   - Extract username and password from the JSON request payload.
   - Return 400 Bad Request if username or password is missing.
   - Return 400 Bad Request if the user already exists.
   - Save the user with a hashed password and return 201 Created.

4. **Implement Login Endpoint Returning a JWT**
   - Create a `POST /login` route.
   - Extract username and password from the JSON request payload.
   - Return 400 Bad Request if username or password is missing.
   - Return 401 Unauthorized if the user does not exist or the password does not match.
   - Generate and return a JWT signed with a secret key and a 1-hour expiration time.

5. **Protect Existing Endpoints with JWT Middleware**
   - Implement a `@token_required` decorator to protect endpoints.
   - Extract the token from the `Authorization` header, checking for the `Bearer ` prefix.
   - Decode the token using `jwt.decode` with the secret key and the `HS256` algorithm.
   - Verify that the user still exists in the in-memory database.
   - Return 401 Unauthorized if the token is missing, invalid, or expired.
   - Apply the `@token_required` decorator to the `/protected/data` endpoint.

## Verification
- Test all endpoints using `pytest` and `flask.testing.FlaskClient`.
- Verify public endpoint is accessible without authentication.
- Verify protected endpoint is blocked (401) without a token, with an invalid token, and with a missing token.
- Verify user registration works, and duplicate registration is blocked (400).
- Verify user login works with valid credentials and returns a JWT token.
- Verify login fails (401) with invalid credentials.
- Verify protected endpoint is accessible (200) with a valid JWT token.
