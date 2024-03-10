def solution(citations):
    res = 0
    citations.sort(reverse = True)
    idx = 0
    
    while citations :
        if idx <= len(citations) :
            res = idx
        while citations and citations[-1] <= idx :
            citations.pop()
        idx += 1
    return (res)
