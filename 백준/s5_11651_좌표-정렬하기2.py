import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n): 
    x, y = map(int, sys.stdin.readline().split(' '))
    arr.append([y, x])

new_arr = sorted(arr)

for x, y in new_arr:
    print(y, x)