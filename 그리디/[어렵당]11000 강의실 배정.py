# import sys
# input = sys.stdin.readline

# n = int(input())
# c = []

# for _ in range(n):
#     a,b = map(int,input().split())
#     c.append((a,b))

# c.sort(key= lambda x:(x[1],x[0]))

# num = 0
# tmp = [c[0][1]]

# for i in range(1,n):
#     flag = False
#     for j in range(len(tmp)) :
#         if c[i][0] >= tmp[j] :
#             tmp[j] = c[i][1]
#             flag = True
#             break
#     if not flag :
#         tmp.append(c[i][1])

# print(len(tmp))
#=> 시간 초과

#우선 순위 큐를 이용하면 된덩.............................
import heapq
import sys
input = sys.stdin.readline


n = int(input())
c = []

for _ in range(n):
    a,b = map(int,input().split())
    c.append((a,b))

c.sort()
#시작 시간에 맞춰 정렬
room = []
heapq.heappush(room,c[0][1])
#끝나는 시간을 우선순위 큐에
#만약에 끝나는 시간중에 가장 작은애 [0]보다 시작시간이 작다면 룸이 추가되어야함
#만약에 끝나는 시간중에 가장 작은애보다 크거나 같다면 얘 다음으로 붙이면 됨
#시작시간도 정렬되어있기 때문에 가장 사이 텀이 짧은거
for i in range(1,n):
    if c[i][0] >= room[0] :
        heapq.heappop(room)
        heapq.heappush(room,c[i][1])
    else :
        #룸 추가
        heapq.heappush(room,c[i][1])

print(len(room))
