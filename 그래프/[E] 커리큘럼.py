# from collections import deque

# n = int(input())

# curries = [0]
# indegrees = [0] * (n+1)

# for i in range(1,n+1):
#     cur = list(map(int,input().split()))
#     curries.append((cur[0:len(cur)-1]))

#     indegrees[i] = len(curries[i]) -1

# print(curries)


#time과 graph로 커리를 분리 해봐야할듯?

from collections import deque

n = int(input())
time = [0] * (n+1)
indegree = [[] for _ in range(n+1)]
for i in range(1,n+1):
    a = list(map(int,input().split()))
    time[i] = a[0]

    for j in range(1,len(a)-1):
        indegree[i].append(a[j])


res = [0] * (n+1)
for i in range(1,n+1):
    res[i] += time[i]

def topology_sort() :
    q = deque([])

    for i in range(1,n+1) :
        if len(indegree[i]) == 0:
            q.append(i)
    
    while q:
        index = q.popleft()

        for i in range(1,n+1):
            if index in indegree[i]:
                res[i] = max(time[i]+ res[index],res[i])
                indegree[i].remove(index)

                if len(indegree[i]) == 0 :
                    q.append(i)

topology_sort()

for i in range(1,n+1):
    print(res[i])

#테케는 맞는데 정답 처리 될까......................?