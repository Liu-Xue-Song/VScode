n = eval(input())
a = [int(i) for i in input().split(',')]


def sort(a, l, r):
    if (r - l <= 1):
        return
    mid = int((r + l) / 2)
    sort(a, l, mid)
    sort(a, mid, r)
    merge(a, l, r)
    return


def merge(a, l, r):
    mid = int((l + r) / 2)
    k = mid
    b = a.copy()
    i = l
    while (l < mid and k < r):
        if (b[l] <= b[k]):
            a[i] = b[l]
            l += 1
        else:
            a[i] = b[k]
            k += 1
        i += 1
    while (l < mid):
        a[i] = b[l]
        l += 1
        i += 1
    while (k < r):
        a[i] = b[k]
        k += 1
        i += 1
    return


sort(a, 0, n)
print(' '.join(str(i) for i in a))
