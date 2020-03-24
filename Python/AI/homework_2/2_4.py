n = eval(input())
s = ''
for i in range(1, n + 1):
    s = s + str(i)
for i in range(10):
    print(s.count(str(i)), end=' ')
