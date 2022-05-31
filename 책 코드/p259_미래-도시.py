INF = (1e9) # 무한을 10억으로 설정

n, m = map(int, input().split())
# 2차원 리스트 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    # A, B가 서로에게 가는 비용은 1
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
# 플로이드 워셜 알고리즘 짜면 됨
pass
            
# 수행된 결과를 출력
distance = pass

if distance >= INF:
    print(-1)
else:
    print(distance)