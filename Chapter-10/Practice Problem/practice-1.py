class Programmer:
    company = "Microsoft"

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def getInformation(self):
        print(f"The name of the {self.company} Programmer is {self.name} and his working language is {self.language}")


arpan = Programmer("Arpan", "Java")
adarsh = Programmer("Adarsh", "Python")
arpan.getInformation()
adarsh.getInformation()