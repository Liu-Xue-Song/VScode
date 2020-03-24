def findmax(lst, a, left, right):
    if a < lst[left]:
        return -1
    if a >= lst[right - 1]:
        return right - 1
    mid = int((left + right) / 2)
    if lst[mid] <= a and lst[mid + 1] > a:  #can equal
        return mid
    elif lst[mid] > a:
        return findmax(lst, a, left, mid)
    else:
        return findmax(lst, a, mid + 1, right)


def ismid(lst, a, t):
    count = 0
    r = 0
    for i in range(0, len(lst)):
        count += findmax(lst, lst[i] + a, 0, len(lst)) - i  #
    #count is the number that the difference <= a
    if count < t:  #mid in the left
        return 0
    else:  #mid in the right of midian
        return 1


# def sort(lst, low, high):
#     left = low
#     right = high
#     if right <= left:
#         return
#     p = lst[left]
#     while left < right:
#         while left < right and lst[right] >= p:
#             right -= 1
#         lst[left] = lst[right]
#         while left < right and lst[left] < p:
#             left += 1
#         lst[right] = lst[left]
#     lst[left] = p
#     sort(lst, low, left - 1)
#     sort(lst, left + 1, high)

n = eval(input())
lst = [eval(n) for n in input().split()]
# n = len(lst)
lst.sort()
t = int(n * (n - 1) / 2)
t = int((t + 1) / 2)  # the number of mididle in the set
left = 0
right = lst[n - 1] - lst[0]
while left < right:
    mid = int((left + right) / 2)
    r = ismid(lst, mid, t)
    if r == 0:
        left = mid + 1
    else:
        right = mid
print(right)

# lst2 = []
# for i in range(len(lst) - 1):
#     for j in lst[i + 1:]:
#         lst2.append(j - lst[i])
# lst2.sort()
# print(lst2[int((len(lst2) - 1) / 2)])
