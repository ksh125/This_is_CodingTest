n = int(input())

arr = [1] * (n + 1)

for i in range(2, n + 1):
    arr[i] = arr[i - 1] * 1 + arr[i - 2] * 2

print(arr[n], end = '\n')