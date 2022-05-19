import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr = sorted(arr)
arr = reversed(arr)

print(*arr, sep="\n")