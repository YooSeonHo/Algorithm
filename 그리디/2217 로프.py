n = int(input())
l = []
for _ in range(n) : 
    l.append(int(input()))


l.sort(reverse=True)

res = []
for i in range(len(l)):
    res.append((i+1) * l[i])
        

print(max(res))