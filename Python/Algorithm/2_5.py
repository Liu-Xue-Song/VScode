num = [eval(n) for n in input().split()]
n = len(num)
max = max(num)
min = min(num)
if max == min:
    print('0')
else:
    bucket = [[0 for i in range(3)] for j in range(n)]
    for i in range(n):
        alc = n * (num[i] - min) / (max - min)
        alc = int(alc)
        if alc == n:
            alc = n - 1
        bucket[alc][0] = 1 + bucket[alc][0]
        if num[i] < bucket[alc][1] or bucket[alc][0] == 1:
            bucket[alc][1] = num[i]
        if num[i] > bucket[alc][2] or bucket[alc][0] == 1:
            bucket[alc][2] = num[i]
    r = 0
    i = 0
    while i < n - 1:
        j = i + 1
        while (bucket[j][0] == 0):
            j += 1
        if r < bucket[j][2] - bucket[i][1]:
            r = bucket[j][2] - bucket[i][1]
        i = j
    print((r))
