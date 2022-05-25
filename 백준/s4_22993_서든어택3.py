n = int(input())
arr = list(map(int, input().split()))

def play():
    a = arr.pop(0)
    arr.sort()

    for i in arr:
        if a > i: 
            a += i
        else :
            return "No"
    return "Yes"

print(play())