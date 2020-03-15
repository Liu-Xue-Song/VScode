x = int(input())
while x != 1:
    if x % 2 == 0:
        print('{:d}/2={:d}'.format(int(x), int(x / 2)))
        x = x / 2
    else:
        print('{:d}*3+1={:d}'.format(int(x), int(x * 3 + 1)))
        x = x * 3 + 1
