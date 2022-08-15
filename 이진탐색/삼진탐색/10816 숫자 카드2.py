import sys
from bisect import bisect_left,bisect_right
imput = sys.stdin.readline

n = int(imput())
cards = list(map(int,imput().split()))
cards.sort()

m = int(imput())
checkList = list(map(int,imput().split()))

for check in checkList:
    cnt = bisect_right(cards,check) - bisect_left(cards,check)
    print(cnt,end=' ')
