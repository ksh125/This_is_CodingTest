from bisect import bisect_left, bisect_right
import sys
 
n, m = map(int, sys.stdin.readline().rstrip().split())
p = list(map(int, sys.stdin.readline().rstrip().split()))
p.sort()
 
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    lidx = bisect_left(p, a)
    ridx = bisect_right(p, b)
    print(ridx - lidx)