a, b = map(int, input().split(' '))
l = list()
for i in range(a):
    l.append(list(map(int, input().split(' '))))

sort = int(input())

sortedList = sorted(l, key=lambda value: value[sort])

for q in sortedList:
    print(' '.join(map(str, q)))

