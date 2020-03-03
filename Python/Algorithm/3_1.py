n = input()
num = [int(n) for n in input().split()]
k = 0
n = len(num)


def odd(lst, k, end, n):
    if end - k <= 2:
        if lst[k] > lst[end - 1]:
            lst[k], lst[end - 1] = lst[end - 1], lst[k]
        return lst[int((n - 1) / 2)]
    else:
        temp = lst[k]
        b = lst.copy()
        e = end - 1
        j = k
        for i in range(k + 1, end):
            if num[i] < temp:
                b[j] = num[i]
                j += 1
            else:
                b[e] = num[i]
                e -= 1
        b[j] = temp
        lst = b.copy()
        if j == (n - 1) / 2:
            return b[j]
        elif j > (n - 1) / 2:
            return odd(lst, k, j, n)
        else:
            return odd(lst, j + 1, end, n)


def even(lst, k, end, n):
    temp = lst[k]
    b = lst.copy()
    e = end - 1
    j = k
    for i in range(k + 1, end):
        if num[i] < temp:
            b[j] = num[i]
            j += 1
        else:
            b[e] = num[i]
            e -= 1
    b[j] = temp
    lst = b.copy()
    if j == n / 2 - 1:
        return b[j]
    elif j > n / 2 - 1:
        return odd(lst, k, j, n)
    else:
        return odd(lst, j + 1, end, n)


if n % 2 == 1:
    print(odd(num, 0, n, n))
else:
    print(even(num, 0, n, n))
