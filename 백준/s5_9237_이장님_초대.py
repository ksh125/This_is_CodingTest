import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
m.sort(reverse = True)

for i in range(len(m)):
    m[i] = m[i] + i + 1
    
print(max(m) + 1)