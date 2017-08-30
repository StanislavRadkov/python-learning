from itertools import combinations
i = input().split()
l = list()
for z in range(1, int(i[1]) + 1):
    for s in list(combinations(sorted(i[0]), z)):
        print(''.join(s))