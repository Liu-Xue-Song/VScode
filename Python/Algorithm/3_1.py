n = input()
num = [int(n) for n in input().split()]
k = 0
n = len(num)


def odd(lst, k, end, n):
    if end - k < 2:
        # if lst[k] > lst[end - 1]:
        #     lst[k], lst[end - 1] = lst[end - 1], lst[k]
        return lst[int((n - 1) / 2)]
    else:
        temp = lst[k]
        b = lst[:]
        e = end - 1
        j = k
        for i in range(k + 1, end):
            if lst[i] < temp:
                b[j] = lst[i]
                j += 1
            else:
                b[e] = lst[i]
                e -= 1
        b[j] = temp
        lst = b.copy()
        if j == int((n - 1) / 2):
            return b[j]
        elif j > int((n - 1) / 2):
            return odd(lst, k, j, n)
        else:
            return odd(lst, j + 1, end, n)


r = (odd(num, 0, n, n))
print('{:.6f}'.format(r))