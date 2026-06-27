# Plan

1. **Understand current implementation**: View `main.py` and `test_main.py`.
2. **Implement Precondition**: 
   - Check if `arr` is sorted in ascending order.
   - We can do `all(arr[i] <= arr[i+1] for i in range(len(arr)-1))`.
   - If not sorted, raise `ValueError("Array must be sorted")`.
3. **Fix bugs**:
   - `binary_search` might have bugs like `high = len(arr)` instead of `high = len(arr) - 1`, wrong while loop condition, wrong `mid` update, or wrong `low`/`high` updates.
   - We will write the standard correct binary search logic.
4. **Implement Postcondition**:
   - Store the result `idx`.
   - Before returning `idx`, check if `idx != -1`.
   - If so, verify `arr[idx] == target`.
   - If violated, raise `RuntimeError("Postcondition failed")`.
5. **Write/Run tests**: Check if `test_main.py` has sufficient coverage, if not add tests. Run tests.
6. **Finalize**: Ensure everything works.
