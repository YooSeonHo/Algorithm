

t = int(input())
calls = []
# (zero, one 순서)
calls.append((1,0))
calls.append((0,1))
calls.append((1,1))

for i in range(3,41) :
    zero, one = calls[i-1]
    z, o = calls[i-2]
    calls.append((zero+z,one+o))

for _ in range(t):
    n = int(input())
    print(calls[n][0],calls[n][1])