import re

n = int(input().strip())
temp =[]
a = re.compile(r'<[a-z0-9][\w._-]+@[a-z]+\.[a-z]{1,3}>', re.I)
for _ in range(n):
    temp.append(input().strip())
for i, x in enumerate(temp):
    v =  a.search(x)
    if v:
        print(temp[i])