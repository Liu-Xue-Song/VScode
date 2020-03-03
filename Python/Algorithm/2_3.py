num = [int(n) for n in input().split()]
n = len(num)
ma = max(num)
mi = min(num)
lst = [0 for i in range(ma - mi + 1)]
for i in range(n):
    ele = num[i]
    lst[ele - mi] += 1
print('N    Count')
for i in range(ma - mi, -1, -1):
    if lst[i] != 0:
        print(i + mi, '    ', lst[i], sep='')
