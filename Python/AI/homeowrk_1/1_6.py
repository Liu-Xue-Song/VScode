n = int(input())
for i in range(2, n + 1):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s == i:
        print(i)
