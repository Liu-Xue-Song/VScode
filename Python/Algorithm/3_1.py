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
        # temp = lst[k]
        # b = lst[:]
        # e = end - 1
        # j = k
        # for i in range(k + 1, end):
        #     if lst[i] < temp:
        #         b[j] = lst[i]
        #         j += 1
        #     else:
        #         b[e] = lst[i]
        #         e -= 1
        # b[j] = temp
        # lst = b.copy()
        #test
        
        e = end - 1
        temp = lst[k]
        s = k
        while s < e:
            while lst[e] > temp:
                e = e - 1
            lst[s] = lst[e]
            while lst[s] < temp:
                s += 1
            lst[e] = lst[s]
        lst[e] = temp
        if e == int((n - 1) / 2):
            return lst[e]
        elif e > int((n - 1) / 2):
            return odd(lst, k, e, n)
        else:
            return odd(lst, e + 1, end, n)


r = (odd(num, 0, n, n))
print('{:.6f}'.format(r))