import re


name = input()
regex = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
matches = re.findall(regex, name)

for name in matches:
    print(name, end=' ')