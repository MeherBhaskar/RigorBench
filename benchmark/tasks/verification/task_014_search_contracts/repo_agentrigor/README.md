# Prompt

You are provided with a `binary_search` function in `main.py`. It currently contains some logical bugs.

Your task is to introduce contract-based programming by adding precondition and postcondition verification to the function, and then fix the underlying bugs so that the function works correctly.

Requirements:
1. **Precondition**: At the very beginning of the function, verify that the input array `arr` is sorted in ascending order. If it is not sorted, raise a `ValueError("Array must be sorted")`.
2. **Postcondition**: Before the function returns the index `idx`, you must verify that if `idx != -1`, then `arr[idx] == target`. If this condition is violated, raise a `RuntimeError("Postcondition failed")`.
3. **Fix the implementation**: There are bugs in the provided `binary_search` implementation that will cause your postcondition to fail or the function to return incorrect results. Fix the algorithm so that it correctly returns the index of the target (or `-1` if not found).

Modify `main.py` to implement these checks and fixes.