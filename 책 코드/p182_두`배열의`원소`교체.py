# N, K 를 입력받기
n, k = map(int, input().split())
# 배열 a의 모든 원소를 입력받기
a = list(map(int, input().split()))
# 배열 b의 모든 원소를 입력받기
b = list(map(int, input().split()))

# 배열 a를 오름차순으로 정렬
a.sort()
# 배열 b를 내림차순으로 정렬
b.sort(reverse=True)

# 두 배열의 값을 첫번째 부터 K번 비교
for i in range(k):
    # a의 원소가 b의 원소보다 작은경우
    if a[i] < b[i]:
        # 두 원소를 스왑
        a[i], b[i] = b[i], a[i]
    # 그 외의 경우(a의 원소가 b의 원소보다 크거나 같을 경우)
    else:
        break
    
# a의 모든 원소의 합을 출력
print(sum(a))