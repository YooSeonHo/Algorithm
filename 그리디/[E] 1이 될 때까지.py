n,k = map(int,input().split())

cnt = 0

while n != 1:
    if n % k == 0:
        n /=k
        cnt +=1
    else :
        n -=1
        cnt+=1

print(cnt)



#책 풀이 => n이 엄청 커졌을 때!
res = 0

while True :
    target = (n//k) * k #나누어 떨어지는 수 ex) (17//4) * 4 = 16
    res += (n-target) #일일이 -1씩 하는게 아니라 바로 계산해서 뺴주게
    n = target

    if n < k :
        break
    res += 1
    n //= k

res += (n-1) # n<k면 루프가 끝나니 1이 될 때까지 빼줘야함 => ex) n = 3 => (3-1)번
print(res)

