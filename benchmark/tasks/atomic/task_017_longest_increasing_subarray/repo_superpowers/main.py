def longest_increasing_subarray(arr: list[int]) -> int:
    if not arr:
        return 0
    max_len = 1
    curr_len = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1
    return max_len
