with open('text/this.txt', 'r') as f:
    content = f.read()

with open('text/copyofthis.txt', 'w') as f:
    f.write(content)
    