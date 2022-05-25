import sys
input = sys.stdin.readline

n = int(input())
me = list(map(int, input().split()))
me.sort()

you = list(map(int, input().split()))
you.sort()

result = 0

for i in range(n // 2 + 1):
    if me[i] < you[n // 2 + i]:
        result += 1

if result > n // 2:
    print("YES")
else:
    print("NO")