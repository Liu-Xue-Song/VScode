x = int(input())
i = 1
while i <= 100:
    p = 1
    lst = []
    while p <= 10:
        if i > 100:
            break
        if i % x != 0:
            s = str(i)
            if s.find(str(x)) == -1:
                lst.append(s)
                p += 1
        i += 1
    print(','.join(lst))