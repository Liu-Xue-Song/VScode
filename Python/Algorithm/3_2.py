def findmax(lst, a, left, right):
    if a < lst[left]:
        return -1
    mid = int((left + right) / 2)
    if lst[mid] <= a and lst[mid + 1] > a:
        return mid
    elif lst[mid] > a:
        return findmax(lst, a, left, mid)
    else:
        return findmax(lst, a, mid + 1, right)


def ismid(lst, a, t):
    count = 0
    r = 0
    for i in lst[1:]:
        count += findmax(lst, i - a, 0, len(lst)) + 1  #+1 or keeplike this
    #count is the number that the difference not less than a

    if count == int(t / 2):
        return -1
    elif count > int(t / 2):  #mid in the left
        return 1
    else:
        return 0


while input():
    lst = [int(n) for n in input().split()]
    n = len(lst)
    lst = sorted(lst)
    t = n * (n - 1) / 2
    left = 0
    right = lst[n - 1] - lst[0]
    while left < right - 0.5:
        mid = (left + right) / 2
        if ismid(lst, mid, t) == -1:
            right = mid
            break
        if ismid(lst, mid, t) == 0:  #mid is in the right
            right = mid
        else:
            left = mid
    print(int(right))
