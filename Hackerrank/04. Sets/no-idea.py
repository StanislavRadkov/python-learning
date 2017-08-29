input()
arr = list(map(int, input().split()))
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

h = 0
for i in arr:
  if i in s1:
    h += 1
  if i in s2:
    h += -1

print(h)
