import itertools

k, m = map(int, input().split(" "))
arrays = [map(int, input().split(" ")[1:]) for _ in range(k)]

def f(*nums):
    return sum(x * x for x in nums) % m

print(max(itertools.starmap(f, itertools.product(*arrays))))