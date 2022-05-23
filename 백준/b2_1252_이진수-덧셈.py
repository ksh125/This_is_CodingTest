a, b = input().split()

a = int(a, 2)
b = int(b, 2)
result = bin(a + b)[2:]

print(result)