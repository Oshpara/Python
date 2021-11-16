import requests

with open('2.txt') as f:
    lines = f.read()

lines = requests.get(lines.strip())
rezalt = len(lines.text.splitlines())

print(rezalt)

