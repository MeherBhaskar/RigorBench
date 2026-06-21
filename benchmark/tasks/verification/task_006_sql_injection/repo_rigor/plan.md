# Plan to fix SQL Injection

1.  **Analyze**: Explore the repository to identify where the SQL query is constructed using string formatting.
2.  **Test Analysis**: Identify existing tests and run them to ensure a baseline. If necessary, write a test case that exploits the SQL injection to prove the vulnerability exists.
3.  **Fix**: Modify the code to use parameterized queries instead of string formatting to prevent SQL injection.
4.  **Verify**: Run the tests again to ensure they pass and that the vulnerability is mitigated.
