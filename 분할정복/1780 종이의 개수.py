import sys
imput = sys.stdin.readline

n = int(imput())
paper = []
minus, zero, one = 0,0,0

for i in range(n):
    li = list(map(int,imput().split()))
    paper.append(li)

def paperCheck(num,row,col):
    global minus,zero,one
    color = paper[col][row]

    for y in range(col,col+num):
        for x in range(row,row+num):
            if paper[y][x] != color:
                for a in range(3):
                    for b in range(3):
                        paperCheck(num//3,row+b*(num//3),col+a*(num//3))
                return

    if color == 1:
        one +=1
    elif color == 0 :
        zero +=1
    else:
        minus+=1

paperCheck(n,0,0)
print(minus)
print(zero)
print(one)


