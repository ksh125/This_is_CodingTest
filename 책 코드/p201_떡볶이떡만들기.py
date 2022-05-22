# 떡의 개수(n)와 요청된 떡의 길이(m)을 공백으로 구분하여 입력
n, m = list(map(int, input().split()))
# 떡의 개별 높이 입력
h = list(map(int, input().split()))

# 이진탐색을 위한 시작 값(start)과 끝 값(end)를 선언
start = 0
end = max(h) # 배열의 가장 큰 값(마지막 값)을 end 값으로 지정

# 반복적 이진 탐색 수행
result = 0 # 결과 값(출력값)
while(start <= end): # end 값이 start값보다 크거나 같으면 반복
    total = 0 # 떡을 절단하고 나온 떡의 총 길이를 선언
    mid = (start + end) // 2 # 배열의 가운데 값인 mid를 선언
    for x in h: # 개별 높이값을 담은 x을 지정
        if x > mid: # 만약 x 가 mid 값보다 크다면
            total += x - mid # 총 값에 (x - mid)을 더함
        if total < m: # 만약 현재 나온 떡의 길이가 요청된 떡의 길이보다 짧다면
            end = mid - 1 # 끝 값(end)를 mid - 1값으로 잡음
        else: # 그 외(떡의 양이 충분한 경우)
            result = mid # result 값에 기록
            start = mid + 1 # 높이값을 높인다(+ 1)
            
# 결과값 출력
print(result)