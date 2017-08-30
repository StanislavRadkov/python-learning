from collections import *

input()
sizes = Counter(map(int, input().split(' ')))
money = 0

n = int(input())
for i in range(n):
    a, b = list(map(int, input(). split(' ')))
    if a in sizes:
        sizes[a] -= 1
        if sizes[a] == 0:
            del sizes[a]
        money += b

print(money)