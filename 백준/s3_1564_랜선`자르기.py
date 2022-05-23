import sys

n, m = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

cnt = 0 
start, end = 1, (1 << 31) - 1
ans = 0
while start <= end:
    mid = (start + end) // 2
    line = 0
    for i in arr:
        line += i // mid
    if line >= m:
        start = mid + 1
        ans = max(ans, mid)
    else:
        end = mid - 1

print(ans)