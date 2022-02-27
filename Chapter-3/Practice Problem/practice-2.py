letter = '''Dear <|NAME|>,
Greetings from ABC Coding House. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>'''

name = input("Enter Your Name: ")
date = input("Enter Date: ")

letter=letter.replace("NAME", name)
letter=letter.replace("DATE", date)

print(letter)