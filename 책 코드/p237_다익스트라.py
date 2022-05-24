import heapq  # 우선순위 큐 구현을 위함

def dijkstra(dir, start):
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

print(dijkstra(dir, 'A'))
'''
문제를 봤을 때 모든 칸의 거리가 1이다
그렇다면 BFS, DFS 탐색
근데 거리가 1이 아니야 칸마다 달라
그럼 가까운거부터 가야겠지 
가까운걸 어떻게 판4단해? heapq.heappop으로 가까운애부터 뽑는거지 
가깝다 = 현재까지 온 위치 값 + 걔까지 가는 거리 = 거리의 합 < 요게 가장 작은애부터 탐색


'''