superset = True
s = set(map(int, input().split()))

for i in range(int(input())):
    k = set(map(int, input().split()))
    if(len(k - s) != 0 or len(s - k) == 0):
        superset = False
        break

print(superset)