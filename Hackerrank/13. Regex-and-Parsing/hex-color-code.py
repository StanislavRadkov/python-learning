import re

in_block = False
for x in range(int(input())):
    line = input()
    if '{' in line:
        in_block = True
        continue
    if '}' in line:
        in_block = False
        continue
        
    if in_block == True:
        m = re.findall(r'(#[a-fA-F0-9]{3,6})', line)
        if m:
            print(*m, sep='\n')
            