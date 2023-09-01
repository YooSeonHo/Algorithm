

money = int(input())
price = list(map(int,input().split()))

junMoney = money
seongMoney = money
junStock,seongStock = 0 , 0
plusCount, minusCount = 0 , 0

for i in range(len(price)) :
    # 준현이부터
    if (junMoney // price[i]) > 0 :
        junStock += (junMoney // price[i])
        junMoney -= (junMoney // price[i]) * price[i]


    if i == 0 :
        continue
    else :
        if price[i] > price[i-1] :
            minusCount = 0
            plusCount += 1
        elif price[i] < price[i-1] :
            plusCount = 0
            minusCount += 1
        elif price[i] == price[i-1] :
            minusCount = 0
            plusCount = 0

    if plusCount >= 3 :
        seongMoney += (price[i] * seongStock)
        seongStock = 0

    elif minusCount >= 3 :
        if (seongMoney // price[i]) > 0 :
            seongStock += ( seongMoney // price[i] )
            seongMoney -= ( seongMoney // price[i] ) * price[i]


seongRes = seongMoney + (seongStock * price[len(price)-1])
junRes = junMoney + (junStock * price[len(price)-1])


if seongRes == junRes :
    print("SAMESAME")
else :
    print("BNP" if junRes > seongRes else "TIMING" )