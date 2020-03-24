child = [eval(x) for x in input().split()]
biscuit = [eval(x) for x in input().split()]
biscuit.sort()
child.sort()
c = 0
b = 0
while c < len(child) and b < len(biscuit):
    if biscuit[b] >= child[c]:
        b += 1
        c += 1
    else:
        b += 1
print(c)