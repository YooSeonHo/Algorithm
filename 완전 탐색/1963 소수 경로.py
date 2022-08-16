# import sys
# from collections import deque
# imput = sys.stdin.readline

# prime = [True] * 10000
# cmp = [1,10,100,1000]

# def is_prime():
#     global prime
#     prime[0] = False
#     prime[1] = False
    
#     for i in range(2,int(9999**0.5)+1):
#         if prime[i] == True:
#             for j in range(2*i,10000,i):
#                 prime[j] = False

# def compare(now,target):
#     q = deque([])
#     q.append(now)
#     cnt = [0] * 10001

#     while q:
#         x = q.popleft()
#         if x == target:
#             print(cnt[x])
#             return
#         else:
#             for i in cmp:
#                 if i == 1:
#                     if 1000<=(x-i)<=9999 and not cnt[x-i] and prime[x-i]:
#                         cnt[x-i] = cnt[x]+1
#                         q.append(x-i)

#                     if 1000<=(x+i)<=9999 and not cnt[x+i] and prime[x+i]:
#                         cnt[x+i] = cnt[x]+1
#                         q.append(x+i)
#                 else:
#                     for j in range(1,10):
#                         if 1000<=(x-i*j)<=9999 and not cnt[x-i*j] and prime[x-i*j]:
#                             cnt[x-i*j] = cnt[x]+1
#                             q.append(x-i*j)

#                         if 1000<=(x+i*j)<=9999 and not cnt[x+i*j] and prime[x+i*j]:
#                             cnt[x+i*j] = cnt[x]+1
#                             q.append(x+i*j)
                        
        
#     print('Impossbile')

# is_prime()

# T = int(imput())

# for i in range(T):
#     now,target = list(map(int,imput().split()))

#     compare(now,target)
# #1차 도전 
# #잘못 된점 -> 10,20,30,40,,,, 더하고 빼면 같은 1033 -> 1043 -> 1053 .. 까진 ㄱㅊ은데
# #1103 되면 한자리만 달라진게 아니덩 ㅋ


import sys
from collections import deque
imput = sys.stdin.readline

prime = [True] * 10000

def is_prime():
    global prime
    prime[0] = False
    prime[1] = False

    for i in range(2,int(9999**0.5)+1):
        if prime[i] == True:
            for j in range(2*i,10000,i):
                prime[j] = False

is_prime()

def trace(now,target):
    q = deque([])
    q.append(now)
    cnt = [0] * 10000
    

    while q:
        x = q.popleft()
        if x == target :
            print(cnt[int(x)])
            return
        else:
            for i in range(4):
                tmp = list(x)
                for j in range(10):
                    if x[i] != str(j):
                        tmp[i] = str(j)
                        ans = ''.join(tmp)
                        if 1000<=int(ans)<=9999 and not cnt[int(ans)] and prime[int(ans)]:
                            cnt[int(ans)] = cnt[int(x)]+1
                            q.append(ans)

    print('Impossible')

T = int(imput())

for i in range(T):
    now,target = list(imput().split())

    trace(now,target)
