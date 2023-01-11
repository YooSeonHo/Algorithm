n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))


# for _ in range(k):
#     a.sort()
#     b.sort(reverse=True)
#     # 매번 이런식으로 반복문 마다 정렬? O(n^2 logn)가 되는듯? 처음에 한번만 정렬하고 일일이 비교
#     tmp = a[0]
#     a[0] = b[0]
#     b[0] = tmp

# print(sum(a))


a.sort()
b.sort(reverse=True)

for i in range(k):
    #최대 k번 바꿔치기니까 a가 b보다 클 땐 안바꿔도 됨

    if a[i] < b[i]:
        tmp = a[i]
        a[i] = b[i]
        b[i] = tmp

        # a[i],b[i] = b[i],a[i] 로 교환 가능
    else : 
        break

print(sum(a))
