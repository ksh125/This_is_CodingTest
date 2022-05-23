def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# n = int(input())
# print(fib(n))
# # 0 1 2 3 4 5 6 7  8
# # 0 1 1 2 3 5 8 13 21
# def dfs(n):
#     if n < 2 :
#         return n
    
#     return dfs(n-1) + dfs(n-2)


# print(dfs(5))