import re

tester = re.compile(
    r'^' 
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")

for i in range(int(input())):
    print('Valid' if tester.search(input()) else 'Invalid')
    