def solution(food_times, k):
    answer = 0
    
    
    cnt = k // len(food_times)
    times = list(map(lambda x: x-cnt , food_times))
    
    now = k % len(food_times)
    
    for i in range(now):
        times[i] -= 1
        
    if sum(times) <= 0 :
        print(-1)
        return
        
    for i in range(len(times)):
        if times[i] < 0 :
            now += (-times[i])
    ans = now = now % len(times) +1
    print(ans)

solution(list(map(int,input().split())),5)