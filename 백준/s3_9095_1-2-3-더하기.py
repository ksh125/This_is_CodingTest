import sys

arr = [0] * (12)
arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4, 12):
    arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
    
for _ in range(int(sys.stdin.readline().rstrip())):
    result = int(sys.stdin.readline().rstrip())
    print(arr[result])