n = sorted([int(input()) for _ in range(9)])
sum_n = sum(n)

for i in range(8):
    for j in range(i + 1, 9):
        if sum_n - (n[i] + n[j]) == 100:
            m1, m2 = n[i], n[j]

n.remove(m1)
n.remove(m2)

for h in n:
    print(h)