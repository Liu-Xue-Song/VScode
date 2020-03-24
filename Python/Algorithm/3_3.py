def mid5(lst):
    if lst[0] > lst[1]:
        lst[1], lst[0] = lst[0], lst[1]
    if lst[2] > lst[3]:
        lst[2], lst[3] = lst[3], lst[2]
    if lst[1] > lst[3]:
        lst[1], lst[4] = lst[4], lst[1]
        if lst[0] > lst[1]:
            lst[1], lst[0] = lst[0], lst[1]
    else:
        lst[3], lst[4] = lst[4], lst[3]
        if lst[2] > lst[3]:
            lst[2], lst[3] = lst[3], lst[2]
    if lst[1] > lst[3]:
        lst[0], lst[2] = lst[2], lst[0]
        lst[1], lst[3] = lst[3], lst[1]
    if lst[1] > lst[2]:
        lst[2], lst[1] = lst[1], lst[2]
    return lst


def pivot(lst):
    n = len(lst)
    if n <= 5:
        return int((n + 1) / 2), short(lst, n, int((n + 1) / 2))
    colNum = n // 5
    # table = [[0 for i in range(5)] for j in range(colNum)]
    # table = [0 for i in range(colNum)]
    table = []
    k = 0
    for i in range(colNum):
        table.append(mid5(lst[k:k + 5]))
        k += 5
    more = lst[k:]
    sp, m = pivot([i[2] for i in table])  # is there has to be a return valure?
    s = 0
    e = n
    for i in table:
        if i[2] == m:
            lst[s:s + 2] = i[:2]
            lst[e - 2:e] = i[3:]
            s += 2
            e -= 2
        elif i[2] < m:
            lst[s:s + 3] = i[:3]
            more.extend(i[3:])
            s += 3
        else:
            lst[e - 3:e] = i[2:]
            more.extend(i[:2])
            e -= 3
    for i in more:
        if i <= m:
            lst[s] = i
            s += 1
        else:
            lst[e - 1] = i
            e -= 1
    lst[s] = m
    return s, m


def short(lst, n, k):
    lst.sort()
    return lst[k - 1]


def findk(lst, k):
    n = len(lst)
    if n <= 5:
        return short(lst, n, k)
    else:
        s, m = pivot(lst)
        if s == k - 1:
            return m
        elif s > k - 1:
            return findk(lst[:s], k)
        else:
            return findk(lst[s + 1:], k - s - 1)


n = eval(input())
k = int(input())
lst = [eval(n) for n in input().split()]
y = findk(lst, k)
print(y)