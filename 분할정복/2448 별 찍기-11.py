import sys
sys.setrecursionlimit(10**6)

n = int(input())

def star(n):
    if n == 3:
        return ['*', '* *','*****']
    arr = star(n//2)
    stars = []

    for i in arr:
        stars.append(i)
    for i,j in zip(arr,range(1,len(arr)+1)):
        stars.append(i+' '*len(arr[-j])+i)
    
    return stars

ans = star(n)

for i in range(len(ans)):
    print(' '*(n-i-1)+ans[i]+' '*(n-i-1))