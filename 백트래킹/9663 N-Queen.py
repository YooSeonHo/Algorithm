# # import itertools
# # n = int(input())
# # game = [[0] * (n+1) for _ in range(n+1)]
# # tmp = [i for i in range(1,n+1)]
# # queens = list(itertools.product(tmp,repeart=2))
# # #queen이 가능한 모든 위치가 적혀 있는거 ㅋ [1][1]~[n][n]

# n = int(input())
# game = [[0] * (n+1) for _ in range(n+1)]
# queens = []
# res = 0

# def dfs(x,y):
#     if len(queens) == n :
#         res += 1
#         return
#     else :
#         for i in range(x,n+1):
#             for j in range(y,n+1):
#                 if game[i][j] == 0:
#                     queens.append((i,j))

#                     for a in range(1,n+1):
#                         game[a][j] = 1
#                         game[i][a] = 1

#                     dfs(i,j)
#                     queens.pop()
#                 # flag = False
#                 # for k in range(len(queens)):
#                 #     a,b = queens.pop()
#                 #     if i == a or b == j :
#                 #         flag = True
#                 #         break
#                 #     elif 


n = int(input())
game = [0] * (n+1)
## index = row , value = column
res = 0

def promising(i):
    for j in range(1,i) :
        # i+1 이 아니라 i임!!!!!!!
        if (game[j] == game[i] or abs(game[i] - game[j]) == abs(i - j) ) :
            return False
    return True
#백트래킹 할 때 프로미싱 잘 짜야함..............

def n_queen(i) :
    global res
    if i > n :
        res += 1
        return
    else :
        for j in range(1,n+1):
            game[i] = j
            if promising(i) :
                n_queen(i+1)


n_queen(1)
print(res)

