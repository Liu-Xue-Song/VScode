x = input()
lst = []
for i in range(len(x)):
    if x[i].isalpha() and x[i].upper() == x[i]:
        if ord(x[i]) <= 85:
            lst.append(chr(ord(x[i]) + 5))
        else:
            lst.append(chr(ord(x[i]) + 5 - 91 + 65))
    else:
        lst.append(x[i])
print(''.join(lst))
