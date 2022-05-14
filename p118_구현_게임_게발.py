# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장할 맵 생성하고 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x좌표, y좌표, 방향을 입력
x, y, move = map(int, input().split())
d[x][y] = 1

# 전체 맵 정보를 입력받기
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
# 북, 동, 남, 서 방향 선언
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회정
def turn():
    global move
    move -= 1
    if move == -1:
        move = 3
        
# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn()
    nx = x + dx[move]
    ny = y + dy[move]
    # 회전 후 정면에 가보지 않은 칸이 있을 경우 이동
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 후 정면에 가보지 않은 칸이 있거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[move]
        ny = y - dy[move]
        # 뒤로 갈 수 있다면 이동
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다인 경우
        else:
            break
        turn_time = 0
        
# 출력
print(count)