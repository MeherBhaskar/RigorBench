def binary_search(arr, target):
    if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Array must be sorted")
    
    left, right = 0, len(arr) - 1
    idx = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            idx = mid
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    if idx != -1 and arr[idx] != target:
        raise RuntimeError("Postcondition failed")
        
    return idx
