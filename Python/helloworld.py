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
# month = [
#     'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
#     'Nov', 'Dec'
# ]
# days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# monthdays = dict(zip(month, days))
# print(list(monthdays.keys()))
# print(list(monthdays.values()))
# print(list(monthdays.items()))
# print(monthdays['Mar'])
# print(monthdays.get('Abc', 'No Found!'))
# monthdays['Feb'] = 29
# x = {'a1': 21, 'a2': 34}
# monthdays.update(x)
# monthdays.pop('a1')
# print(monthdays)
# a = {"Tom.py", "Mike.py", "Anne.py", "Denny.py", "Jack.py", "Fan.py"}
# b = {"Tom.py", "Lily.py", "Anne.py", "Richard.py", "Jack.py"}
# print(a - b)
# print(a & b)
# print(a ^ b)
# print(a | b)
# set1 = {1, 2, 3, 4, 5}
# set2 = {6, 7, 8, 9, 10}
# vote = {4, 7, 9, 1, 2, 2, 6, 2, 2, 1, 6, 9, 7, 4, 5, 5, 7, 9, 5, 5, 4}
# print(vote)
# print(set1 & vote)
# print(set2 - vote)
# set2.update({11})
# s = eval(input())
# print(s in vote)
# s = eval(input())
# print(s.items())
# d = sorted(s.items())
# print(d)
x = [eval(n) for n in input().split(',')]
s = set(x)
l = list(s)
l.sort(key=x.index)
print(l)