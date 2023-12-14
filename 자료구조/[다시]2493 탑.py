# #걍 2중 포문 => 시간 초과 ㅋ => n이 50만 ㅋㅋㅋ
# n = int(input())
# tower = list(map(int,input().split()))
# res = []
# #마지막에 0 추가로 append해야함 (맨 처음 탑)

# def add_one(n) :
#     return n + 1

# while len(tower) > 1 :
#     if tower[-1] == max(tower) :
#         res.append(-1)
#         tower.pop()    
#         continue
#     else :
#         for j in range(len(tower)-2,-1,-1) :
#             if tower[j] > tower[-1] :
#                 res.append(j)
#                 tower.pop()
#                 break
#             else :
#                 continue
# res.append(-1)
# res = list(map(add_one,res))[::-1]
# print(*res,sep=' ')


n = int(input())
tower = list(map(int,input().split()))
stack = []
res = [0] * n

for i in range(len(tower)):
    while stack :
        if stack[-1][1] < tower[i] :
            stack.pop()
            continue
        else :
            res[i] = stack[-1][0]
            break

    stack.append([i+1,tower[i]])
print(*res)
