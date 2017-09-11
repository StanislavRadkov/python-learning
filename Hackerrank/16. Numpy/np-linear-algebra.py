import numpy

n = int(input())

print(numpy.linalg.det(numpy.array([input().split() for _ in range(n)] , dtype=float)))
