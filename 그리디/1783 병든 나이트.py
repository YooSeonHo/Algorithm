n,m = map(int,input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min((m-1)//2+1,4))
else:
    if m > 6:
        print(m-2)
    else:
        print(min(4,m))

