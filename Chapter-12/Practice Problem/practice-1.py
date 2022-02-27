def readFile(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")

readFile('text/1.txt')
readFile('text/2.txt')
readFile('text/3.txt')