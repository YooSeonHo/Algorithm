dx = [1,-1,1,-1,2,-2,2,-2]
dy = [2,2,-2,-2,1,1,-1,-1]
col = ['a','b','c','d','e','f','g','h']

loc = input()
#열과 행으로 입력 ex)a1
column = col.index(loc[0])+1
row = int(loc[1])
cnt = 0

for i in range(8):
    nx = column + dx[i]
    ny = row + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        cnt +=1

print(cnt)