s = input()
res = ''

tmp = []
cnt = 0
flag = False
for i in range(len(s)):
    if s[i] == 'X':
        cnt += 1
    else :
        if cnt % 2 != 0 :
            print(-1)
            flag = True
            break

        while cnt > 0 :
            if cnt >= 4 :
                tmp.append('AAAA')
                cnt -= 4
            elif cnt == 2 :
                tmp.append('BB')
                cnt -= 2

        tmp.append('.')

if not flag : 
    if cnt  % 2 != 0 :
        print(-1)

    else : 
        while cnt>0 :
            if cnt >= 4 :
                tmp.append('AAAA')
                cnt -= 4
            elif cnt == 2 :
                tmp.append('BB')
                cnt -= 2


        print(''.join(tmp))










board = input()
board = board.replace('XXXX','AAAA')
board = board.replace('XX','BB')
if 'X' in board :
    print(-1)
else :
    print(board)

#우와..............