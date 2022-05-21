def binary_search(a, b):
    target = b
    while True:
        mid = (a + b) // 2
        if (mid ** 2) == target:
            return mid
        if mid ** 2 > target:
            b = mid
        elif mid ** 2 < target:
            a = mid

n = int(input())
print(binary_search(1, n))