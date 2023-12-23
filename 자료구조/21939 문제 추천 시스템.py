import sys
import heapq
input = sys.stdin.readline

max_heap = []
min_heap = []
idx = [False] * 100001

n = int(input())

for _ in range(n):
    num,rate = map(int,input().split())
    heapq.heappush(max_heap,(-rate,-num))
    heapq.heappush(min_heap,(rate,num))
    idx[num] = True

cmds = int(input())

for i in range(cmds) :
    cmd = list(input().split())

    if cmd[0] == 'recommend' :
        if cmd[1] == '1':
            while max_heap and not idx[-(max_heap[0][1])] :
                heapq.heappop(max_heap)

            if max_heap :
                print(-(max_heap[0][1]))

        else :
            while min_heap and not idx[min_heap[0][1]] :
                heapq.heappop(min_heap)
            if min_heap :
                print(min_heap[0][1])

    elif cmd[0] == 'add' :
        num,rate = map(int,cmd[1:3])
        heapq.heappush(max_heap,(-rate,-num))
        heapq.heappush(min_heap,(rate,num))
        idx[num] = True

    else :
        idx[int(cmd[1])] = False
        while max_heap and not idx[-(max_heap[0][1])] :
            heapq.heappop(max_heap)
        while min_heap and not idx[min_heap[0][1]] :
            heapq.heappop(min_heap)