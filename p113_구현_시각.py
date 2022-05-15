# H(hour) 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # i, j, k에 3이 들어가면 count에 +1
            if '3' in str(i) + str(j) + str(k):
                count += 1
  
print(count)