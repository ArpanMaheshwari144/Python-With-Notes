class Animals:
    animalType = "Mammal"

class Pets(Animals):
    color = "White"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!!")


husky = Dog()
print(husky.animalType)
print(husky.color)
husky.bark()