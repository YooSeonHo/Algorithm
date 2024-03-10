def solution(array, commands):
    res = []
    for c in commands :
        i,j,k = c
        arr = array[i-1:j]
        arr.sort()
        res.append(arr[k-1])
        
    return (res)