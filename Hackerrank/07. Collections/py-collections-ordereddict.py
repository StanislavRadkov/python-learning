from collections import OrderedDict

d = dict()
od = OrderedDict()
k = 0

n = int(input())
for i in range(0, n):
    a = input().split()
    name = ' '.join(a[:-1])
    value = int(a[-1])

    if name not in od.values():
        od[k] = name
        k += 1

    if name in d:
        d[name] += value
    else:
        d[name] = value

for key, value in od.items():
    print(value + ' ' + str(d[value]))