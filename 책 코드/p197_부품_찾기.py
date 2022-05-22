def binary_search(arr, t, s, e):
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] > t:
            e = mid - 1
        else:
            s = mid + 1

n = int(input())

arr1 = list(map(int, input().split()))
arr1.sort()

m = int(input())

arr2 = list(map(int, input().split()))

for i in arr2:
    p = binary_search(arr1, 1, 0, n - 1)
    if p != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')