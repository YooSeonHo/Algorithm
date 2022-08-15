import sys
imput = sys.stdin.readline

arr = []
n = int(imput())
for i in range(n):
    arr.append(int(imput()))

arr.sort(reverse=True)
ans = 0
minus = -1


if n == 1:
    print(arr[0])

else:
    #양수 
    for i in range(0,n,2):
        if i+1 < n :
            if arr[i+1] > 1 : 
                ans += arr[i] * arr[i+1]
            elif arr[i+1] == 1:
                ans += arr[i+1] + arr[i]
                minus = i + 2
                continue
            elif arr[i] > 0 :  
                ans += arr[i]
                minus = i + 1
                break
            else:
                minus = i
                break
        else:
            if arr[i] > 0:
                ans += arr[i]
            else:
                minus = i
    if minus >= 0 :
        for i in range(n-1,-1,-2):
            if i > minus:
                ans += arr[i] * arr[i-1]
            elif i == minus:
                ans += arr[i]

    print(ans)



#시발.........모범답안 
#1은 애초에 arr에 추가 안하고 ans로 넣어버림..
#pop활용.....

#import sys

# input = sys.stdin.readline
# n = int(input())
# parr = []
# marr = []
# res = 0
# for i in range(n):
#     a = int(input())
#     if a == 1:
#         res += 1
#     elif a > 0:
#         parr.append(a)
#     else:
#         marr.append(a)
# parr.sort()
# marr.sort(reverse=True)
# while len(parr) != 0:
#     if len(parr) == 1:
#         res += parr.pop()
#     else:
#         res += parr.pop() * parr.pop()
# while len(marr) != 0:
#     if len(marr) == 1:
#         res += marr.pop()
#     else:
#         res += marr.pop() * marr.pop()
# print(res)