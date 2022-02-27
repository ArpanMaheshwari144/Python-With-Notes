content = True
i = 1
with open('text/log.txt', 'r') as f:
    while content:
        content = f.readline()
      
        if 'python' in content.lower():
            print(content)
            print(f"Yes, python is present on line number {i}\n")
        i = i+1