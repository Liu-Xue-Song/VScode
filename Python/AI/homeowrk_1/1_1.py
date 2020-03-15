for i in range(1, 20):
    for j in range(1, 30):
        for k in range(1, 98):
            if 5 * i + 3 * j + k / 3 == 100 and i + j + k == 100:
                print('rooster={},hen={},chick={}'.format(i, j, k))