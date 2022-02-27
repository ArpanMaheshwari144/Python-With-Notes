# with open('text/log.txt', 'r') as f:
#     content = f.read().lower()

# if 'python' in content:
#     print("python is present")
# else:
#     print("python is not present") 


with open('text/log.txt', 'r') as f:
    content = f.read()

if 'python' in content.lower():
    print("python is present")
else:
    print("python is not present") 