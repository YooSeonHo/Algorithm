
import sys
input = sys.stdin.readline



n,m = map(int,input().split())
arr = list(map(int,input().split()))
start, end = 0, 0
cnt = 0

while start < n :
    if end >= n :
        start += 1
    # end가 끝까지 가면 계속 start + 1 해주면서 부분합 체크

    if sum(arr[start:end+1]) > m :
        start += 1
    elif sum(arr[start:end+1]) < m :
        end += 1
    # m보다 작고, end가 n이 됐으면 결코 m보다 더 작아질 일은 없어서 이 조건문 실행이 안될거!
    
    else :
        cnt += 1
        start += 1


print(cnt)

##############################################
sub_total = 0
for start in range(n) :
    while sub_total < m and e < n :
        sub_total += arr[end]
        end += 1
    if sub_total == m :
        cnt += 1
    sub_total -= arr[start]

###############################################