import sys
imput = sys.stdin.readline

n = int(imput())
cards = list(map(int,imput().split()))
cards.sort()

m = int(imput())
checkList = list(map(int,imput().split()))

for check in checkList:
    left = 0
    right = n-1
    Flag = False

    while left <= right:
        mid = (left+right)//2
        if cards[mid] == check:
            print(1,end=' ')
            Flag = True
            break
        elif cards[mid] > check:
            right = mid -1
        elif cards[mid] < check:
            left = mid +1
    if Flag == False:
        print(0,end=' ')

