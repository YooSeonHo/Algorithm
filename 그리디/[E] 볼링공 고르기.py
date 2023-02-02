n,m = map(int,input().split())
balls = list(map(int,input().split()))

#1. 완탐
balls.sort()
cnt = 0
for i in range(len(balls)):
    for j in range(i+1,len(balls)):
        if balls[i] == balls[j] :
            continue
        else :
            cnt +=1

print(cnt)


#2. 그리디
arr = [0] * (m+1)
#무게 별 공 개수 세기

for i in balls :
    arr[i] += 1

res = 0

for i in range(len(balls)):
    sameNum = arr[balls[i]]
    if sameNum == 1:
        res += len(balls) - 1 - i
    else :
        res += len(balls) -1 -i -(sameNum-1)
        arr[balls[i]] -= 1
print(res)

#3. 그리디 해답
result = 0
for i in range(1,m+1) :
    n -= arr[i]
    result += n * arr[i]

print(result)
