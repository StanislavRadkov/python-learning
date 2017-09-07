import numpy

l = []

for n in range(int(input().split(' ')[0])):
    l.append(list(map(int, input().split(' '))))

print(numpy.transpose(l))
print(l.flatten())