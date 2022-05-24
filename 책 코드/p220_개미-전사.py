n = int(input())
arr = list(map(int,input().split()))

for i in range(1, n):
    if i == 1:
        arr[i] = max(arr[i], arr[i - 1])
    else:
        arr[i] = max(arr[i - 1], arr[i - 2] + arr[i])

print(arr[n - 1])