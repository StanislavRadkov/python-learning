input()
s = set(map(int, input().split()))

n = int(input())

for i in range(0, n):
    values = input().split()
    a = values[0]
    b = 0
    if len(values) > 1:
        b = int(values[1])

    if a == 'pop':
        s.pop()
    elif a == 'remove':
        s.remove(b)
    elif a == 'discard':
        s.discard(b)

print(sum(s))

