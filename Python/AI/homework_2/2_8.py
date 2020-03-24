s = input()
h = 0
sum = 0
for i in s:
    if i == 'A':
        h += 1
        sum += h
    else:
        h = 0
print(sum)