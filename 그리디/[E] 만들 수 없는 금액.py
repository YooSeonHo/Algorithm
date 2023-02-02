n = int(input())
coins = list(map(int,input().split()))

#가능한 합 경우의 수를 다 만들어서 -> 최솟값의 -1 ?(1이 아닐시)

coins.sort()
target = 1
#1 ~ target-1까진 모두 만들 수 ㅇ

for coin in coins :
    if coin <= target :
        #새로 들어올 코인이 target보다 작거나 같다? => (target-1) + coin까지 모든 수를 만들 수 있다는 뜻 => 타겟 업데이트 
        target += coin
    else :
        break

print(target)

#아니 너무 어렵덩.......