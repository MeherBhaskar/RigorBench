def longest_increasing_subarray(arr):
    if not arr:
        return 0

    max_len = 1
    current_len = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
            current_len = 1

    if current_len > max_len:
        max_len = current_len

    return max_len
