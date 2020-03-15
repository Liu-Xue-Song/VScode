flag = 0
for i in range(100, 999):
    if i % 37 == 0:
        k = i
        for j in range(2):
            k = 10 * (k % 100) + k // 100
            if k % 37 != 0:
                flag += 1
if flag == 0:
    print("It's a true proposition.")
else:
    print("It's a false proposition.")
