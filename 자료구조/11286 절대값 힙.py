import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n) :
    num = int(input())
    if num == 0 :
        if not heap :
            print(0)
        else :
            print(hq.heappop(heap)[1])
    else :        
        hq.heappush(heap,(abs(num),num))



