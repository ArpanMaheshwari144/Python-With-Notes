# str = "          Arpan is good boy         "
# print(str)
# print(str.strip())


def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

str = "          Arpan is good boy         "
newStr = remove_and_split(str, "Arpan")
print(newStr)
