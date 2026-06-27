# Plan

1. **Understand the Goal**: We need to write a function `longest_increasing_subarray(arr)` that finds the length of the longest continuous strictly increasing subarray. Return 0 if the array is empty.
2. **Implementation Strategy**:
   - Create a file `solution.py` (or whatever the typical name is, I will just call it `longest_increasing_subarray.py`).
   - Iterate through the array, keeping track of the current increasing subarray length (`current_len`) and the maximum length seen so far (`max_len`).
   - If the current element is strictly greater than the previous element, increment `current_len`.
   - Otherwise, update `max_len` (if `current_len` is greater) and reset `current_len` to 1.
   - At the end of the loop, update `max_len` one last time.
3. **Testing Strategy**:
   - Create a file `test_longest_increasing_subarray.py`.
   - Use standard asserts to test cases:
     - Empty array
     - Single element
     - All increasing
     - All decreasing
     - Mixed with multiple increasing subarrays
     - Elements equal to previous (not strictly increasing)
4. **Execution**:
   - Run tests.
   - Validate correctness.
