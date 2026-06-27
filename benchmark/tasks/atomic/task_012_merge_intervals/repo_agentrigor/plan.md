# Plan for `merge_intervals`

## Objective
Implement a function `merge_intervals(intervals)` that takes a list of intervals and merges all overlapping intervals.

## Approach
1. **Handle Edge Cases**: If the input `intervals` list is empty, return an empty list.
2. **Sort Intervals**: Sort the `intervals` list based on the starting value of each interval. This ensures that any overlapping intervals will be adjacent in the sorted list.
3. **Merge Intervals**:
   - Initialize an empty list called `merged`.
   - Iterate through the sorted `intervals`.
   - For each interval, check if `merged` is empty or if the current interval's start value is greater than the end value of the last interval in `merged`.
     - If true, there is no overlap, so append the current interval to `merged`.
     - If false, there is an overlap. Update the end value of the last interval in `merged` to be the maximum of its current end value and the current interval's end value.
4. **Return**: Return the `merged` list.

## Testing Strategy
1. Test with the provided examples in the prompt.
2. Test with an empty list.
3. Test with a single interval.
4. Test with completely non-overlapping intervals.
5. Test with completely overlapping intervals (one interval completely inside another).
6. Test with multiple overlapping intervals.
