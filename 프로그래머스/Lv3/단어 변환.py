from collections import deque

def solution(begin, target, words):
    n = len(begin)
    m = len(words)
    visited = [False] * m
    q = deque([])
    q.append([begin,0])
    
    while q:
        word, cnt = q.popleft()
        if word == target :
            return cnt
        
        for i in range(m) :
            check = 0
            for j in range(n) :
                if check >= 2:
                    break
                if word[j] != words[i][j] :
                    check += 1
            if check == 1:
                if not visited[i] :
                    q.append([words[i],cnt+1])
                    visited[i] = True
        
    return 0