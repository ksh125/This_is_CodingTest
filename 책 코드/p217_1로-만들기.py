result = 0
n = int(input())
while n > 1:
    if n % 3 == 0:
        n = n / 3
        result += 1
        continue
    
    elif n % 5 == 0:
        n = n / 5
        result += 1
        continue
    
    else:
        n = n - 1
        result += 1
        continue
    
print(result)