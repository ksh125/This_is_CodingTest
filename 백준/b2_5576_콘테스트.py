import sys

w = []
k = []

for i in range(10):
    w.append(int(sys.stdin.readline()))
    
for j in range(10):
    k.append(int(sys.stdin.readline()))
    
w.sort(reverse = True)
k.sort(reverse = True)

print(sum(w[:3]), sum(k[:3]))