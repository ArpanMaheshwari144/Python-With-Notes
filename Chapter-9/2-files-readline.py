f = open('text/sample.txt', 'r')

# Read first line from the file
data = f.readline()  # readline() reads only one line at a time from the file  
print(data)

# Read second line from the file
data = f.readline()
print(data)

# Read third line from the file
data = f.readline()
print(data)

f.close()