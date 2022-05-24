n, m = int(input())

for _ in range(n):
    a = int(input())

arr = [10001] * (m + 1)
arr[0] = 0

for i in range(n):
    for j in range(a[i], m + 1):
        if arr[j - a[i]] != 1001:
            arr[j] = min(arr[j], arr[j - a[i]] + 1)

if arr[m] == 10001:
    print(-1)
else:
    print(arr[m])