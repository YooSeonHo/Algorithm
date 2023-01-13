import sys
imput = sys.stdin.readline

n,m =  map(int,imput().split())
arr = list(map(int,imput().split()))

arr.sort()

def binary_search(arr,t,start,end):
    for i in range(len(arr)) :
        tmp = []
        for j in range(len(arr)) :
            if arr[j] > arr[i] :
                tmp.append(arr[j] - arr[i]) 

        if sum(tmp) == t:    
            return arr[i]
        elif sum(tmp) > t :
            start = i
        else : 
            end = i
            start = i-1
            break
    
    while start <= end:
        mid = (start+end)//2

        tmp = []
        for i in range(len(arr)) :
            if arr[i] > arr[mid] : 
                tmp.append(arr[i] - arr[mid]) 

        if sum(tmp) == t:
            return arr[mid]

        elif sum(tmp) > t :
            end = mid -1

        else : 
            start = mid +1
        
    return arr[end]

res = binary_search(arr,m,0,len(arr)-1)
print(res)

#2805번이랑 같은 문제임!!!!!!!!!!! 이렇게 풀면 시간초과 날거같은뎅