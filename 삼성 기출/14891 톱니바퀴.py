

arr = [list(map(int,input())) for _ in range(4)]
# [2] - [6] 비교해야함
k = int(input())

def clock(arr) :
    arr = [arr[len(arr)-1]] + arr[:-1]
    return arr

def reverse_clock(arr) :
    arr = arr[1:len(arr)] + [arr[0]]
    return arr


def check(num,arr,direction,visited) :

    visited[num] = True

    if num == 0 :
        if arr[num][2] != arr[num+1][6] and not visited[num+1] :
            arr = check(num+1,arr,1 if direction == -1 else -1,visited)

    elif 1 <= num <= 2 :
        if arr[num][2] != arr[num+1][6] and not visited[num+1] :
            arr = check(num+1,arr,1 if direction == -1 else -1,visited)
        if arr[num][6] != arr[num-1][2] and not visited[num-1] :
            arr = check(num-1,arr,1 if direction == -1 else -1,visited)

    elif num == 3 :
        if arr[num][6] != arr[num-1][2] and not visited[num-1] :
            arr = check(num-1,arr,1 if direction == -1 else -1,visited)
    if direction == 1 :
        arr[num] = clock(arr[num])
    elif direction == -1 :
        arr[num] = reverse_clock(arr[num])

    return arr

        

for _ in range(k):
    visited = [False] * 4
    num, direction = map(int,input().split())
    num -= 1

    arr = check(num,arr,direction,visited)

    
res = 0

for i in range(4):
    if arr[i][0] == 1 :
        res += 2**i


print(res)