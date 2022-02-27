words = ["donkey", "kaddu", "mote"]

with open('text/sample4.txt','r') as f:
    content = f.read()

for word in words:
    content = content.replace(word, "########")
    with open('text/sample4.txt','w') as f:
        f.write(content)
