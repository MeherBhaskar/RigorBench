def binary_search(arr, target):
    # TODO: Add precondition check here
    
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            idx = mid + 1
            # TODO: Add postcondition check here
            return idx
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    idx = -1
    # TODO: Add postcondition check here
    return idx
