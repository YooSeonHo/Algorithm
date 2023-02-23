# import sys
# input = sys.stdin.readline

# n,m,r = map(int,input().split())

# arr = [list(map(int,input().split())) for _ in range(n)]
# res = []
# def rotate(startx,endx,starty,endy) :
#     if startx >= endx or starty >= endy :
#         return
#     else :
#         for i in range(startx,endx):
#             for j in range(starty,endy):
#                 if i == startx and j == starty :
#                     res[i+1][j] = arr[i][j]
#                 else :
#                     res[i][j] = arr[i][j-1]
