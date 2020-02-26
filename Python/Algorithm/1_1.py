p = 0
n = 0
num = [eval(n) for n in input().split()]
for i in num:
    x = i
    if x > 0:
        p += x
    else:
        n += x
print(format(p, '.2f'), format(n, '.2f'), format(p+n, '.2f'),sep=',')
