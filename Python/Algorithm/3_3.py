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


def pivot(lst):
    n = len(lst)
    if n <= 5:
        return short(lst, n, int((n - 1) / 2))
    colNum = n // 5
    table = [[0 for i in range(colNum)] for j in range(5)]
    # table = [0 for i in range(colNum)]
    k = 0
    for i in range(colNum):
        q = lst[k:k + 5]
        k += 5
        mid5(q)
        # table[i] = q[2]
        for j in range(5):
            table[j][i] = q[i]
    more = lst[k:]
    #weird here, maybe wrong
    m = pivot(table[2])
    # m = pivot(table)


def short(lst, n, k):
    lst.sort()
    return lst[k - 1]


def findk(lst, k):
    n = len(lst)
    if n <= 5:
        return short(lst, n, k)
    else:
        b = [0] * n
        p = pivot(lst)
        s = 0
        e = n - 1
        for i in lst:
            if i < p:
                b[s] = i
                s += 1
            elif i > p:
                b[e] = i
                e -= 1
        b[s] = p
        lst = b
        if s == k - 1:
            return p
        elif s > k - 1:
            return findk(lst[:s], k)
        else:
            return findk(lst[s + 1:], k - s - 1)


n = eval(input())
k = int(input())
lst = [eval(n) for n in input().split()]
y = findk(lst, k)
print(y)