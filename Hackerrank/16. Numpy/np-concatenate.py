import numpy

d = list(map(int, input().split(' ')))

l1 = []
for i in range(d[0]):
    l1.append(list(map(int, input().split(' '))))

l2 = []
for i in range(d[1]):
    l2.append(list(map(int, input().split(' '))))

print(numpy.concatenate((numpy.array(l1), numpy.array(l2)), axis = 0))