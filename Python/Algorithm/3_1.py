# n = input()
# num = [int(n) for n in input().split()]
# k = 0
# n = len(num)

# def odd(lst, k, end, n):
#     if end - k < 2:
#         # if lst[k] > lst[end - 1]:
#         #     lst[k], lst[end - 1] = lst[end - 1], lst[k]
#         return lst[int((n - 1) / 2)]
#     else:
#         temp = lst[int((k + end) / 2)]
#         b = [0] * n
#         e = end - 1
#         j = k
#         for i in range(k, end):
#             if lst[i] < temp:
#                 b[j] = lst[i]
#                 j += 1
#             elif lst[i] > temp:
#                 b[e] = lst[i]
#                 e -= 1
#         b[j] = temp
#         lst = b.copy()
#         e = j
#         if e == int((n - 1) / 2):
#             return lst[e]
#         elif e > int((n - 1) / 2):
#             return odd(lst, k, e, n)
#         else:
#             return odd(lst, e + 1, end, n)
'''
wrong code
correct answer in cpp 3_1.cpp
'''
r = (odd(num, 0, n, n))
print('{:.6f}'.format(r))