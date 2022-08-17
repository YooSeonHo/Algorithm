# import sys
# from collections import deque
# imput = sys.stdin.readline

# def DSLR(A,B):
#     res = ['0'] * 10000
#     q = deque([])
#     q.append(A)

#     while q:
#         x = q.popleft()
#         if x == B:
#             print(res[x][1:])
#             return
#         else:
#             #기존의 res[n]보다 길이가 길어지면 갱신할 필요가 x -> 코드로
#             n = (x*2) % 10000
#             res[n] = res[x]+'D'
#             q.append(n)

#             if x == 0:
#                 q.append(9999)
#                 res[9999] = res[0] + 'S'
#             else:
#                 n = x -1
#                 q.append(n)
#                 res[n] = res[x] + 'S'

#             tmp = str(x)
#             n = tmp[1:4]+tmp[0]
#             n = int(n)
#             res[n] = res[x]+'L'
#             q.append(n)

#             n = tmp[-1] + tmp[0:3]
#             n = int(n)
#             res[n] = res[x] + 'R'
#             q.append(n)
            


# T = int(imput())

# for i in range(T):
#     A,B = map(int,imput().split())

#     DSLR(A,B)
        


import sys
from collections import deque
imput = sys.stdin.readline

def DSLR(a,b):
    visited = [False] * 10001
    visited[a] = True
    q = deque([])
    q.append((a,''))

    while q:
        x,path = q.popleft()

        if x == b:
            print(path)
            return
        else:
            n = (x*2)%10000
            if not visited[n] :
                q.append((n,path+'D'))
                visited[n] = True
        
            if x != 0:
                n = x-1
            else:
                n = 9999
            
            if not visited[n] :
                q.append((n,path+'S'))
                visited[n] = True

            n = (x%1000) * 10 + (x//1000)
            if not visited[n]:
                q.append((n,path+'L'))
                visited[n] = True

            n = (x%10)*1000 + (x//10)
            if not visited[n]:
                q.append((n,path+'R'))
                visited[n] = True


T = int(imput())
for _ in range(T):
    a,b = map(int,imput().split())
    DSLR(a,b)


