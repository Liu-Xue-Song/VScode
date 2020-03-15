lst = input()
lst = lst.split()
m = 0
s = 0
for i in range(5):
    if len(lst[i]) > m:
        m = len(lst[i])
        s = i
print(lst[s])