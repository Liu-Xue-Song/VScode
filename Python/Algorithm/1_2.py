import numpy
n = eval(input())
bee = numpy.zeros((n, 2))
for i in range(0, n):
    bee[i] = [eval(n) for n in input().split()]
f = numpy.zeros((50))
f[1] = 1
f[2] = 2
for i in range(3, 50):
    f[i] = f[i - 1] + f[i - 2]
for i in range(0, n):
    x = bee[i][1] - bee[i][0]
    x = int(x)
    print(int(f[x]))