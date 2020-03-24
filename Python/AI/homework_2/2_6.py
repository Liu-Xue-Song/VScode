x = [eval(x) for x in input().split()]
y = [eval(x) for x in input().split()]
max = 1000
for i in x:
    for j in y:
        if abs(i - j) < max:
            max = abs(i - j)
print(max)