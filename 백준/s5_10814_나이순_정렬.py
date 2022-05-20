inp = int(input())
l = []
for _ in range(inp):
    age, name = map(str, input().split())
    age = int(age)
    l.append((age, name))
    
l.sort(key=lambda a: (a[0]))

for i in l:
    print(i[0], i[1])