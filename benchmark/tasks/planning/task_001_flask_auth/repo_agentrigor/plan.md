# Implementation Plan - JWT Authentication for Flask API

This plan outlines the approach to add secure, JWT-based authentication to the Flask API.

## Subtasks

1. **Create User Model**: Define a `User` class to store user details, specifically storing the `username` and `password_hash` to ensure we do not store plain-text passwords.
2. **Implement User Registration**: Create a `/register` POST endpoint that accepts JSON containing `username` and `password`. It will check for missing fields or duplicate usernames, securely hash the password using `werkzeug.security.generate_password_hash`, and store the new user.
3. **Implement User Login**: Create a `/login` POST endpoint that accepts `username` and `password`, verifies the credentials using `werkzeug.security.check_password_hash`, and returns a signed HS256 JWT token containing the username and an expiration timestamp (1 hour).
4. **Protect Endpoints with JWT Middleware**: Implement a `@token_required` decorator that extracts the JWT from the `Authorization` header (supporting both `Bearer <token>` and raw token formats), decodes it, and validates the user. Apply this decorator to the `/protected/data` endpoint.
5. **Develop and Run Verification Tests**: Write a comprehensive suite of tests using `pytest` to verify all behaviors, including successful register/login, duplicate registration prevention, missing fields handling, unauthorized access to protected endpoints, access with valid/invalid tokens, and public endpoint accessibility.

## Verification Strategy
- We will run the tests using `poetry run pytest test.py` to ensure high test coverage and validation of all edge cases.
