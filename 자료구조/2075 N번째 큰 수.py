import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n) :
    tmp = list(map(int,input().split()))
    for t in tmp :
        heapq.heappush(arr,t)
    while len(arr) > n :
        heapq.heappop(arr)

print(arr[0])
# 메모리 초과 => 12MB = 1,500 * 2 * 4Byte = 1차원 배열 2개가 최대
