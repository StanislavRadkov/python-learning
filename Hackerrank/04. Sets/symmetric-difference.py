input()
s1 = set(map(int, input().split()))
input()
s2 = set(map(int, input().split()))

l = list((s1 - s2) | (s2 - s1))
l.sort();
for i in l:
    print(i)
