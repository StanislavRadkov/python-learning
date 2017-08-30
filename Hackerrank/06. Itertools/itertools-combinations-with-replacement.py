from itertools import combinations_with_replacement

i = input().split()
l = list()

for s in list(combinations_with_replacement(sorted(i[0]), int(i[1]))):
    print(''.join(s))