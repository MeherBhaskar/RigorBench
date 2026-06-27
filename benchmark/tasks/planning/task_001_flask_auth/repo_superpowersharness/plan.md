# Implementation Plan - Add JWT Authentication to Flask API

This plan outlines the steps required to secure the Flask API using JWT-based authentication. The implementation ensures that only registered, authenticated users can access the protected routes, using secure password hashing and JWT token verification.

## Identified Subtasks

1. **Define User Schema and Mock Database**: Set up a `User` model class to represent user accounts and use a thread-safe or local memory-based dictionary `users` for storing user data.
2. **Secure Password Hashing**: Integrate `werkzeug.security.generate_password_hash` and `check_password_hash` to store passwords securely rather than in plain text.
3. **Implement Registration Endpoint (`/register`)**: Create a POST endpoint that validates that both `username` and `password` are provided, prevents duplicate registrations, hashes the password, and saves the user.
4. **Implement Login Endpoint (`/login`)**: Create a POST endpoint that validates user credentials, generates a JWT token using `PyJWT` signed with HS256, sets an expiration time, and returns the token.
5. **Create JWT Authentication Middleware (`token_required` decorator)**: Develop a custom decorator to extract the `Authorization` header (supporting `Bearer <token>`), decode the JWT, verify the signature/expiration, and retrieve the corresponding user.
6. **Protect Endpoints and Construct Test Suite**: Apply the `token_required` decorator to the `/protected/data` endpoint and write comprehensive test cases covering success/failure scenarios (duplicate registration, invalid tokens, missing fields).
