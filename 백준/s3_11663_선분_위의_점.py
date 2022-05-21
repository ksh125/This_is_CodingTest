import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

def na(a):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1

def nna(b):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if b < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end

for i in range(m):
    g, h = map(int, sys.stdin.readline().split())
    print(nna(h) - na(g) + 1)