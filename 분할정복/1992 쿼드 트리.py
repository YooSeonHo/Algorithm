import sys
imput = sys.stdin.readline

n = int(imput())
arr = []

for i in range(n):
    li = list(map(int,imput().rstrip()))
    arr.append(li)

def quad(num,row,col):

    check = arr[col][row]

    for y in range(col,col+num):
        for x in range(row,row+num):
            if arr[y][x] != check:
                print('(',end='')
                for a in range(2):
                    for b in range(2):                       
                        quad(num//2,row+b*(num//2),col+a*(num//2))
                print(')',end='')        
                return
    print(check,end='')
    


quad(n,0,0)