n,m,k = list(map(int,input().split()))
arr = list(map(int,input().split()))
#입력

res = 0 
arr.sort()
#정렬
""" 
tmp = m // k
tmp *= k
m -= tmp #m값 갱신
res += arr[-1] * tmp
#가능한 최대 수 다 더해두기
res += arr[-2] * m

print(res)

이렇게 풀면 안됨........... 왜냐면 5 6 3 / 2 4 5 4 6 일 때 6+6+6+5+6+6 인데 이렇게 하면 6+6+6+6+6+6 이 됨................
아예 반복문을 쓰던가 반복되는 수열을 찾던가!
 """

cnt = 0
cnt += int(m / (k+1)) * k
#수열이 반복되는 횟수
cnt += m % (k+1)
#나누어 떨어지지 않았을 때 가장 큰 수를 더 더해줘야하는 횟수

res += arr[-1] * cnt
res += arr[-2] * (m - cnt)
print(res)