# def mid5(lst):
#     if lst[0] > lst[1]:
#         lst[1], lst[0] = lst[0], lst[1]
#     if lst[2] > lst[3]:
#         lst[2], lst[3] = lst[3], lst[2]
#     if lst[1] > lst[3]:
#         lst[1], lst[4] = lst[4], lst[1]
#         if lst[0] > lst[1]:
#             lst[1], lst[0] = lst[0], lst[1]
#     else:
#         lst[3], lst[4] = lst[4], lst[3]
#         if lst[2] > lst[3]:
#             lst[2], lst[3] = lst[3], lst[2]
#     if lst[1] > lst[3]:
#         lst[0], lst[2] = lst[2], lst[0]
#         lst[1], lst[3] = lst[3], lst[1]
#     if lst[1] > lst[2]:
#         lst[2], lst[1] = lst[1], lst[2]
#     return lst


def pivot(lst):
    n = len(lst)
    if n <= 5:
        lst.sort()
        return lst[int(n / 2)]
    colNum = n // 5
    table = []
    k = 0
    for i in range(colNum):
        table.append(sorted(lst[k:k + 5])[2])
        k += 5
    # if k < n:
    #     table.append(sorted(lst[k:])[int((n - k) / 2)])
    # m = pivotRow([i[2] for i in table])
    #m = findk([i[2] for i in table], int((colNum + 1) / 2))
    m = findk(table, int((colNum + 1) / 2))
    s = 1
    e = n - 1
    # for i in table:
    #     if i[2] < m:
    #         lst[s:s + 3] = i[:3]
    #         more.extend(i[3:])
    #         s += 3
    #     elif i[2] > m:
    #         lst[e - 3:e] = i[2:]
    #         more.extend(i[:2])
    #         e -= 3
    #     else:
    #         lst[s:s + 2] = i[:2]
    #         lst[e - 2:e] = i[3:]
    #         s += 2
    #         e -= 2
    for i in range(n):
        if lst[i] == m:
            lst[0], lst[i] = lst[i], lst[0]
            break
    while s <= e:
        while lst[s] < m and s < e:
            s += 1
        while lst[e] > m:
            e -= 1
        if s >= e:
            break
        lst[s] = lst[e]
    # for i in more:
    #     if i <= m:
    #         lst[s] = i
    #         s += 1
    #     else:
    #         lst[e - 1] = i
    #         e -= 1
    lst[s], lst[0] = lst[0], lst[s]
    return s, m


def findk(lst, k):
    n = len(lst)
    if n <= 5:
        lst.sort()
        return lst[k - 1]
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