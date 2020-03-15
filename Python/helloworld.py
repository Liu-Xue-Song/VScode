# lst = [
#     35, 78, 91, 35, 20, 10, 20, 80, 10, 90, 80, 10, 25, 35, 56, 72, 98, 43, 10,
#     38
# ]
# m = sum(lst) - min(lst) - max(lst)
# m = m / 18
# if m - int(m) >= 0.5:
#     print(int(m) + 1)
# else:
#     print(int(m))
# import numpy
# x = numpy.mean(lst)
# x = x * 20 - 108
# x = x / 18
# print(x)
a = [eval(n) for n in input().split()]
a.sort()
x = a[0]
y = a[1]
n = len(a)
for i in range(int(n / 2)):
    c = a[2 * i]
    d = a[2 * i + 1]
    if x + d >= y + c:
        y = d
    else:
        x, y = y, c
print(x, y, x + y)
