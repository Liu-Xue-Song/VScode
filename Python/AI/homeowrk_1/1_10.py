L = input().split()
t, n = int(L[0]), int(L[1])
k = 0
s = 0
for i in range(n):
    k = k * 10 + t
    s += k
print(s)