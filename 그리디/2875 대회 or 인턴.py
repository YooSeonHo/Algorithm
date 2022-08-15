import sys,math

n,m,k = list(map(int,input().split()))

teams = min(n//2,m)

n -= (teams*2)
m -= teams

if n+m-k >0 :
    print(teams)
else:
    k = (k-n-m)/3
    teams -=math.ceil(k)
    print(teams)
