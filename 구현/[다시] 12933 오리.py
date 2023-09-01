
duck = 'quack'
record = input()
visited = [False] * (len(record))

if len(record) % 5 != 0 or record[0] != 'q' :
    print(-1)
    exit()
# 1. quackq 같은 경우 때문엥!!, 2.시작이 q가 아닐 경우

cnt = 0

def sol(start) : 
    global cnt
    check = True
    index = 0
    for i in range(start,len(record)) :
        if record[i] == duck[index] and not visited[i] :
            visited[i] = True
            if duck[index] == 'k' : 
                if check :
                    cnt += 1
                    check = False
                index = 0
            else :
                index += 1


for i in range(len(record)) : 
    sol(i)

# all 내장함수 사용! -> 배열 및 반복 가능한 객체 요소가 모두 참이면 참 반환

if not all(visited) or cnt == 0 :
    print(-1) 
else : 
    print(cnt)

            

