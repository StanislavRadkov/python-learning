from itertools import permutations
i = input().split()
for s in sorted(list(permutations(i[0], int(i[1])))):
    print(''.join(s))