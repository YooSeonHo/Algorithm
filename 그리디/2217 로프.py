n = int(input())
l = []
for _ in range(n) : 
    l.append(int(input()))

res = []
for i in range(len(l)):
    res.append((i+1) * l[i])
        

print(max(res))