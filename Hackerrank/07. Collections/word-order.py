from collections import OrderedDict

n = int(input())
od = OrderedDict()

for i in range(n):
    w = input()
    if w not in od:
        od[w] = 1
    else:
        od[w] += 1

print(len(od))        
print(' '.join(map(str, od.values())))