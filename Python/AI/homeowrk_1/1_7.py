s = input()
s = s.upper()
c = [0] * 26
for i in s:
    if i.isalpha():
        c[ord(i) - 65] += 1
print(c)