import sys
imput = sys.stdin.readline

n = int(imput())
meeting = []

for i in range(n):
    meet = list(map(int,imput().split()))
    meeting.append(meet)

meeting.sort(key=lambda x: (x[1],x[0]))

cnt = 1
time = meeting[0][1]

for i in range(1,n):
    if time <= meeting[i][0]:
        cnt +=1
        time = meeting[i][1]
    
print(cnt)
