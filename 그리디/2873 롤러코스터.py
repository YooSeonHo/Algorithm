import sys
imput = sys.stdin.readline

c,r = map(int,imput().split())
#시발 row column r행 c열 이라며............ 시발시발

joys = []

for i in range(c):
    li = list(map(int,imput().split()))
    joys.append(li)

if c % 2 == 1 :
    n = (c-1)//2
    for i in range(n):
        print('R'*(r-1)+'D'+'L'*(r-1)+'D',end='')
    print('R'*(r-1),end="")

elif r % 2 == 1:
    n = (r-1) // 2
    for i in range(n):
        print('D'*(c-1)+'R'+'U'*(c-1)+'R',end='')
    print('D'*(c-1),end='')

else:
    min = 1000
    loc = []
    for i in range(c):
        if i%2 == 0 :
            for j in range(1,r,2):
                if min > joys[i][j]:
                    min = joys[i][j]
                    loc = [i,j]
        else:
            for j in range(0,r,2):
                if min > joys[i][j]:
                    min = joys[i][j]
                    loc = [i,j]
    #여기부터 답 봄 ㅈㄴ 어디 피해가야되는지는 구할 수 있는데 이걸 어케 출력해야될지 모르겠음
    ans = ('D'*(c-1)+'R'+'U'*(c-1)+'R')* (loc[1]//2)

    #x를 짝수로 만드는 과정
    x = 2 * (loc[1]//2)
    y = 0 #무조건 맨 위에서 시작
    xbound = x+1

    while x != xbound or y != c-1:
        #[y,xbound(-1)] 하는 이유 : 내 옆에가 loc인지 체크해보는거 맞으면 걍 따운 
        # 아니면 좌우로 왔다갔다 ㅋ
        if x < xbound and [y,xbound] != loc :
            x +=1
            ans += 'R'
        elif x == xbound and [y,xbound-1] != loc:
            x -=1
            ans += 'L'
        if y != c-1:
            y +=1
            ans += 'D'

    ans += ('R'+'U'*(c-1)+'R'+'D'*(c-1)) * ((r - loc[1] -1)//2)
    # 1더 빼주는 이유 : r은 걍 개수고 loc은 0부터 시작하니께 ㅋ
    print(ans)

