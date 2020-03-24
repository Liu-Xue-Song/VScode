n = eval(input())
lst = [1]
for i in range(n):
    if i == 0:
        print('1 ')
    else:
        lst1 = [1]
        for i in range(len(lst) - 1):
            lst1.append(lst[i] + lst[i + 1])
        lst1.append(1)
        for i in lst1:
            print(i, end=' ')
        lst = lst1
        print()
