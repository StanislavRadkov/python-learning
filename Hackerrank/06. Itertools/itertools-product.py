from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

AxB = product(A, B)

print(" ".join(map(str, AxB)))
