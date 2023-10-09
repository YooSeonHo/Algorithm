

n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())
cnt = n

for i in range(len(a)):
    a[i] -= b

for s in a:
    if s <= 0 :
        continue
    else :
        cnt += (s // c)
        if s%c :
            cnt += 1
        
print(cnt)


