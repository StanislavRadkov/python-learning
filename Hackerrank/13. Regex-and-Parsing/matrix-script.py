import re
import itertools

N, M = [int(x) for x in input().split()]
matrix = [input() for _ in range(N)]
cols = itertools.zip_longest(*matrix, fillvalue=' ')
fragments = [''.join(cs) for cs in cols]
phrase = ''.join(fragments)

r = re.compile(r'(?<=[a-z0-9])[^a-z0-9]+(?=[a-z0-9])', re.I)
print(r.sub(' ', phrase))