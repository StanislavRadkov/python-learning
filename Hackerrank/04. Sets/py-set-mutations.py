input()
s = set(map(int, input().split()))

n = int(input())

for i in range(0, n):
    a = input().split()[0]
    s2 = set(map(int, input().split()))

    if a == 'intersection_update':
        s &= s2
    elif a == 'update':
        s |= s2
    elif a == 'symmetric_difference_update':
        s ^= s2
    elif a == 'difference_update':
        s -= s2

print(sum(s))

