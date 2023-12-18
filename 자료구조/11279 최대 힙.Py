import sys
from heapq import heappush,heappop
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    num = int(input())

    if num == 0 :
        if arr :
            print(heappop(arr)[1])
        else :
            print(0)
    else :
        heappush(arr,(-num,num))

