# # 정수 n 입력
# n = int(input())

# # 가게에 있는 부품 번호 입력
# arr1 = set(map(int, input().split()))

# # 정수 m 입력
# m = int(input())

# # 손님이 요청한 부품 번호 입력
# arr2 = list(map(int, input().split()))

# for i in arr2:
#     if arr1 in i:
#         print("yes")
#     else:
#         print("no")

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 정수 n 입력
n = int(input())

# 가게에 있는 부품 번호 입력
arr1 = list(map(int, input().split()))
arr1.sort()

# 정수 m 입력
m = int(input())

# 손님이 요청한 부품 번호 입력
arr2 = list(map(int, input().split()))

# 요청된 부품 번호를 하나씩 확인
for i in arr2:
    result = binary_search(arr1, 1, 0, n - 1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')