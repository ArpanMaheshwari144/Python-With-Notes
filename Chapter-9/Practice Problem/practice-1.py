f = open('text/poem.txt', 'r')
text = f.read()
if 'twinkle' in text:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()