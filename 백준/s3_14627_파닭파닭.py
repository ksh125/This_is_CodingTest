s, c = list(map(int, input().split()))

h = []

for _ in range(s):
    h.append(list(map(int, input().split())))

start = 0
end = max(h)

result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2
    
    for x in h:
        if x > mid:
            total += x - mid
            
        if total < c:
            end = mid - 1
            
        else:
            result = mid
            start = mid + 1
            
print(result)