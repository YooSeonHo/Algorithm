arr = list(map(int,input().split()))
n = max(arr)

while True:
    if (n - arr[0])%15 == 0 and (n - arr[1])%28 == 0 and (n -arr[2])%19 == 0:
        break
    else:
        n+=1
        
print(n)