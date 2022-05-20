import sys

n = int(sys.stdin.readline())
for _ in range(n):
    m = list(map(int, sys.stdin.readline().split()))
    m.sort()
    
    if m[3] - m[1] >= 4:
        print("KIN")
    else:
        print(sum(m[1 : 4]))