# Plan to add JWT Authentication

1. **Create a User model**: Define a User model with an ID, username, and password hash, using Flask-SQLAlchemy (with an in-memory SQLite database) or a similar simple store.
2. **Implement user registration endpoint**: Create a `POST /register` endpoint to accept new user credentials, hash the password securely, and save the user.
3. **Implement login endpoint returning a JWT**: Create a `POST /login` endpoint to verify credentials and return a signed JWT token if they are valid.
4. **Protect existing endpoints with JWT middleware**: Use JWT middleware to secure the existing `/protected/data` endpoint, ensuring only authenticated requests can access it.
5. **Write tests**: Write tests to cover the authentication flow (registration, login) and verify that the protected endpoint correctly accepts valid tokens and rejects missing/invalid tokens. Ensure all tests pass.
