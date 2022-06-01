'''
- 입력될 것들 -
도시의 개수: n
통로의 개수: m
메시지를 보낼 도시: c

- 통로에 대한 것들-
특정 도시: x
특정 도시: y
메세지가 전달되는 시간(distance와 같은 역할): z

- 입력 정보 -
첫째 줄에 n, m, c가 주어진다
둘째 줄부터 m + 1번째 줄에 걸쳐 통로에 대한 정보 x, y, z가 주어진다
(특정 도시 x에서 다른 특정 도시 y로 이어지는 통로가 있으며, 메세지 전달 시간이 z라는 의미)

- 출력 정보 -
c에서 보낸 메세지를 받는 도시의 총 개수와
걸리는 시간을 공백으로 구분하여 출력한다

- 입력 예시 -
3 2 1
1 2 4
1 3 2

- 출력 예시 -
2 4
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0

max_distance = 0

for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)
        
print(count - 1, max_distance)