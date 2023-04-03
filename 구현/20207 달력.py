# import sys
# input = sys.stdin.readline

# n = int(input())

# cal = [[[]]]
# cnt = 0
# #3차원으로 -> 떨어진 직사각형 수가 3차원 , 나머지 2차원은 연속된 날짜와 몇 행인지
# for _ in range(n):

#     a,b = map(int,input().split())
#     if len(cal) == 0 :
#         cal[cnt][0][0].append([i for i in range(a,b+1)])
#         cnt += 1
#     else :
#         flag = False
#         for c in cal :
#             li = [i for i in range(a,b+1)]
#             for d in c :
#                 if li not in d :
#                     d.append(li)
#                     flag = True
#                     break
#         if flag :
#             break
#         else :
#             c.append(li)
            
