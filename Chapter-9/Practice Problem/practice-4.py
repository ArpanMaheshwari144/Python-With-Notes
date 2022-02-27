with open('text/sample3.txt','r') as f:
    content = f.read()

content = content.replace("donkey", "########")

with open('text/sample3.txt','w') as f:
    f.write(content)
