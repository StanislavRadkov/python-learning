import numpy

i = list(map(int, input().split(' ')))

print(numpy.zeros(tuple(i), dtype = numpy.int))
print(numpy.ones(tuple(i), dtype = numpy.int))