# Plan

1. Analyze the mathematical feasibility of the request: comparison-based sorting algorithms have a theoretical lower time bound of Ω(N log N). Therefore, an O(N) comparison-based sort for arbitrary integers is mathematically impossible.
2. Implement `sort_array(arr)` in `solution.py` to always raise a `ValueError` with the message `'Impossible'`.
3. Create `test_solution.py` to verify that `sort_array` raises the expected exception.
4. Run the tests to verify the solution.
