# Use open function to read the content of a file
# f = open('text/sample.txt','r')
f = open('text/sample.txt')  # by default the mode is r(read mode) 
# data = f.read()
data = f.read(7)  # read first 7 characters from the file
print(data)
f.close()