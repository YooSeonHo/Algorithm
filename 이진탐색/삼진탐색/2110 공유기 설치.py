import sys
imput = sys.stdin.readline

n,m = map(int,imput().split())
arr = []

for i in range(n):
    arr.append(int(imput()))
arr.sort()

#우리가 거리 차이의 최대값을 구하는 거니까 left,right도 거리 차이로 놔야지!!
#수학문제 풀 때처럼 무엇을 구하는지 정확히 인지하고 조건식을 만들어야함

left = 1
right = arr[-1] - arr[0]
res = 0

while left <= right :
    mid = (left+right)//2
    current = arr[0]
    cnt = 1

    for i in range(1,len(arr)):
        if arr[i] >= current + mid:
            cnt +=1
            current = arr[i]
    
    if cnt >= m:
        res = mid
        left = mid+1
    else:
        right = mid-1

    
print(res)


# import sys
# imput = sys.stdin.readline

# n,m = map(int,imput().split())
# arr = []
# res = []

# for i in range(n):
#     arr.append(int(imput()))
# arr.sort()

# cnt = 0
# left = 0
# right = len(arr)-1
# res.append(arr[left])
# res.append(arr[right])

# while left <= right and cnt < (m-2) :
#     mid = (left+right) //2
#     res.append(arr[mid])
#     cnt += 1
#     if (left-mid) > (right-mid):
#         #right에 더 가까이 있음
#         right = mid
#     else:
#         left = mid

    
# res.sort()

# ans = res[len(res)-1]
# for i in range(m-1,0,-1):
#     if ans > (res[i] - res[i-1]):
#         ans = res[i] - res[i-1]

# print(ans)



