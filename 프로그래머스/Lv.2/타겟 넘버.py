answer = 0

def dfs(numbers,target,tmp,idx) :
    global answer
    if len(numbers) == idx:
        if tmp == target :
            answer += 1
        return
    else :
        tmp += numbers[idx]
        dfs(numbers,target,tmp,idx+1)
        tmp -= 2 * numbers[idx]
        dfs(numbers,target,tmp,idx+1)
        tmp += numbers[idx]

def solution(numbers, target):
    global answer
    dfs(numbers,target,0,0)
    
    return answer