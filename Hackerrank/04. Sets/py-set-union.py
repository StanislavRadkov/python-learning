input()
s1 = set(map(int, input().split()))
input()
s2 = set(map(int, input().split()))

print(len(s1 | s2))