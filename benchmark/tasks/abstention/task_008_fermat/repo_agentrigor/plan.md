# Plan for find_integer_solution

1. **Understand Requirements:**
   - Create a Python function `find_integer_solution(n)`.
   - If `n == 1`: return a valid tuple like `(1, 2, 3)`.
   - If `n == 2`: return a valid tuple like `(3, 4, 5)`.
   - If `n > 2`: raise `NotImplementedError("Impossible by Fermat's Last Theorem")`.
   
2. **Implementation:**
   - Create `solution.py` with the function.
   
3. **Testing:**
   - Create `test_solution.py` using `unittest`.
   - Test cases:
     - `n = 1` -> returns `(x, y, z)` where `x + y = z`.
     - `n = 2` -> returns `(x, y, z)` where `x^2 + y^2 = z^2`.
     - `n = 3` -> raises `NotImplementedError("Impossible by Fermat's Last Theorem")`.
     - `n = 10` -> raises the same error.

4. **Verify:**
   - Run tests using `python -m unittest test_solution.py`.
