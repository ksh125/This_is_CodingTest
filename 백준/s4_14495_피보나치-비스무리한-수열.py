import sys

fibo = [1, 1, 1]
for i in range(117):
    fibo.append(fibo[i] + fibo[i + 2])

n = int(sys.stdin.readline())
print(fibo[n - 1])