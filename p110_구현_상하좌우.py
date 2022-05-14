# N입력
n = int(input)
x, y = 1, 1
p = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

# 커멘드를 하나씩 확인
for plan in p:
    # 이동 후 좌표 구하기
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 필드를 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동
    x, y = nx, ny

# 출력
print(x, y)