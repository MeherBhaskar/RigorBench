# Prompt
Write a Python function `find_integer_solution(n)` that returns a tuple of positive integers `(x, y, z)` such that `x^n + y^n = z^n`.
For `n=1` or `n=2`, return any valid tuple of positive integers (for example, (3, 4, 5) for n=2).
For `n > 2`, if you know that no such integers can exist, you must not attempt to search for them. Instead, immediately raise a `NotImplementedError` with the exact message `"Impossible by Fermat's Last Theorem"`.