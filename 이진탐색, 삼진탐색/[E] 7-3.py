def binary_search(arr,t,start,end):
    while start <= end :
        mid = (start+end)//2
        if arr[mid] == t:
            return mid
        elif arr[mid] > t :
            end = mid -1
        else :
            start = mid +1

#탐색 범위가 2000만을 넘어가면 이진탐색을 고려
#처리해야할 데이터의 값이나 개수가 1000만개 이상일 때도! => 이때 이진탐색 문제가 아닐지 의심부터 해봐야함

