def solution(arr):
    res = []
    while arr :
        a = arr.pop()
        if not res :
            res.append(a)
            continue
        if res[-1] == a :
            continue
        else :
            res.append(a)
    res.reverse()
    return res