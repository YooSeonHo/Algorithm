

a = [1, 4, 2]	
a.sort()
b = [5,4,4]
b.sort(reverse=True)
res = 0

for i in range(len(a)) :
    res += a[i] * b[i]

print(res)