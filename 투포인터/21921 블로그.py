import sys
input = sys.stdin.readline

n,x = map(int,input().split())
visited = list(map(int,input().split()))


s,e = 0, x-1
cnt = 1
size = sum(visited[s:e+1])
max_size = size

s,e = 1, x

while e < n :
    #sum 시간 복잡도 = O(N)
    if size - visited[s-1] + visited[e] > max_size :
        max_size = size - visited[s-1] + visited[e]
        cnt = 1
    elif size - visited[s-1] + visited[e] == max_size :
        cnt += 1

    size = size - visited[s-1] + visited[e]
    s += 1
    e += 1

if not size :
    print("SAD")
else :
    print(max_size,cnt,sep='\n')