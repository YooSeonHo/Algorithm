import sys
imput = sys.stdin.readline

n = int(input().strip())
arr = list(map(int,imput().split()))
m = int(input().strip())
check = list(map(int,imput().split()))

arr.sort()

def binary_search(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            print('yes',end=' ')
            return
        elif arr[mid] > target :
            end = mid-1
            continue
        else : 
            start = mid +1
            continue
    print('no', end=' ')
    return 
        

for i in range(m):
    binary_search(arr,check[i],0,len(arr)-1)

