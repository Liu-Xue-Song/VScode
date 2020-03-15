x = eval(input())
k = x
t = x
i = 3
j = 1
while (abs(k) > 1e-8):
    j = j * (i - 1) * i
    k = (x)**i / j
    t += k * (-1)**int(i / 2)
    i += 2
print('{:.1f}'.format(t))