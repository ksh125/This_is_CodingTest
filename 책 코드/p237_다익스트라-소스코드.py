import heapq  # 우선순위 큐 구현을 위함

def dijkstra1(dir, start):
  dist = {node: float('inf') for node in dir}  # start로 부터의 거리 값을 저장하기 위함
  dist[start] = 0  # 시작 값은 0이어야 함
  arr = []
  heapq.heappush(arr, [dist[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

  while arr:  # arr에 남아 있는 노드가 없으면 끝
    n_d, n_dest = heapq.heappop(arr)  # 탐색 할 노드, 거리를 가져옴.

    if dist[n_dest] < n_d:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
      continue
    
    for ndest, ndist in dir[n_dest].items():
      dist = n_d + ndist  # 해당 노드를 거쳐 갈 때 거리
      if dist < dist[ndest]:  # 알고 있는 거리 보다 작으면 갱신
        dist[ndest] = dist
        heapq.heappush(arr, [dist, ndest])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
  return dist

dir = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra1(dir, 'A'))



# 책 코드 작성

import sys 
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = int(input())
# 시작 노드 번혼를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] + (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = INF

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map((int, input().split()))
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))
    
# 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_ndoe():
    min_value = INF
    index =  0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[1]:
            min_value = distance[i]
            index = 1
    return index
  
def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 써내서, 방문 처리
        now = get_smallest_ndoe()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + [j[0]]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘을 수행                    
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print('INFINITY')
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])