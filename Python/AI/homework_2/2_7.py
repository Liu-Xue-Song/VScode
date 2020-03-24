n = eval(input())
sum = 0
for i in range(n):
    x = [eval(x) for x in input().split()]
    sum += x[i]
    if n - i - 1 == i:
        continue
    sum += x[n - i - 1]
print(sum)
