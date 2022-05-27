def binary_search(array, target, start, end):
    mid = (start + end) // 2
    while start <= end:
        if array[mid] == target:
            return mid
        elif array[mid] <= target:
            end = mid - 1
        else:
            end = mid + 1