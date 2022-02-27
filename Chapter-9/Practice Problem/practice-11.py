import os

with open('text/sample6.txt', 'r') as f:
    content = f.read()

with open('text/renamed_by_python.txt', 'w') as f:
    f.write(content)

os.remove('text/sample6.txt')
