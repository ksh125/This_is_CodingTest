import sys

n = int(sys.stdin.readline())

a = [1 for _ in range(91)]
a[1] = 1
a[2] = 1

for i in range(1, n + 1):
    if i == 1 or i == 2:
        a[i] = 1
    else:
        a[i] = a[i - 1] + a[i - 2]

print(a[i])