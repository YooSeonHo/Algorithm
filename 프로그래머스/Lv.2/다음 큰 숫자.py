




res = n = 78
# n_bin = sum(map(int,bin(n)[2:]))
n_bin = bin(n).count('1')
while True :
    res += 1
    # res_bin = sum(map(int,bin(res)[2:])) => O(n * k(슬라이싱))
    res_bin = bin(res).count('1') # O(n)
    if n_bin == res_bin :
        break

print(res)