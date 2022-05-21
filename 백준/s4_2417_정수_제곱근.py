n = int(input())

a, b = 0, n

while True:
    mid = (a + b) // 2
    if b < a:
        break
    if mid ** 2 < n:
        a = mid + 1
    else:
        b = mid - 1

print(b+1)