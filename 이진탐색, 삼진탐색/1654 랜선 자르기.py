import sys
imput = sys.stdin.readline

k,n = map(int,imput().split())
arr = []
for i in range(k):
    arr.append(int(imput()))

left = 1
right = sum(arr)//n
result = 0

while left<=right:
    # left > right이 될 때 이분 탐색 종
    middle = (left+right)//2
    cnt = 0
    for i in range(k):
        cnt += arr[i]//middle
    if cnt < n:
        right = middle- 1
    elif cnt >= n:
        result = middle
        left = middle + 1

print(result)

#cnt == n인 값중 최대 값을 찾아야함 단순히 탐색해서 미들을 반환하는게 아님
#이분 탐색이 끝났을 때 right가 최대값이 보장되는지?
#반복문이 끝나면 무조건 n+1, n으로 역전? n,n-1이 될 수도 있는거 아닌가??
#여러 테스트 케이스 돌려보면 무조건 n+1, n으로 역전되고 
