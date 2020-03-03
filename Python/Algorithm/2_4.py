num = [eval(n) for n in input().split()]
thisMax = 0
max = 0
for i in range(len(num)):
    if thisMax + num[i] < 0:
        thisMax = 0
    else:
        thisMax = thisMax + num[i]
    if thisMax > max:
        max = thisMax
print(max)