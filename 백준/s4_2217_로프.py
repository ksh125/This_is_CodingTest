import sys
input = sys.stdin.readlines

n = int(input())
m = []
result = []

for i in range(n):
    x = int(input())
    m.append(x)

m.sort(reverse = True)

for i in range(n):
    result.append((i + 1) * m[i])

print(max(result))