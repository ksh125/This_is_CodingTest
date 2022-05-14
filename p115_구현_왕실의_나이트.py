# 나이트 위치
knight = input()
location = int(knight[1])
coordinate = int(ord(knight[0])) - int(ord('a')) + 1

# 이동 가능한 방향 선언
move = [(-2, -1), (2, 1), (1, -2), (-1, 2), (-2, 1), (2, -1), (-1, -2), (1, 2)]

# 이동 가능한 좌표인지 확인
result = 0
for i in move:
    # 이동할 좌표 확인
    next_location = location + i[0]
    next_coordinate = coordinate + i[1]
    # 이동이 가능한 좌표라면 +1
    if next_location >= 1 and next_location <= 8 and next_coordinate >= 1 and next_coordinate <= 8:
        result += 1
        
# 출력
print(result)