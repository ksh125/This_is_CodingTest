import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n): 
    x, y = map(int, sys.stdin.readline().split(' '))
    arr.append([x, y])

new_arr = sorted(arr)

for x, y in new_arr:
    print(x, y)