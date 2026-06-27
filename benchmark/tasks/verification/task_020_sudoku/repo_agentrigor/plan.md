# Plan for is_valid_sudoku

1.  **Row Validation**:
    *   Iterate through each row (0 to 8).
    *   Check if the current row contains 9 unique elements. We can do this by converting the row to a `set` and checking if its length is 9.

2.  **Column Validation**:
    *   Iterate through each column index (0 to 8).
    *   Extract the column by taking the `i`-th element of each row.
    *   Check if the extracted column contains 9 unique elements (again, using a `set`).

3.  **Sub-box Validation**:
    *   Iterate through the start indices of the 9 sub-boxes. The row start indices will be 0, 3, 6, and the column start indices will be 0, 3, 6.
    *   For each sub-box, extract the 9 elements.
    *   Check if these 9 elements are unique using a `set`.

4.  **Return result**:
    *   If any of the checks fail, return `False`.
    *   If all checks pass, return `True`.
