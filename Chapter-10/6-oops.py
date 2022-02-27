from datetime import datetime

class Employee:

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The date and time is",datetime.now())
        
arpan = Employee()
arpan.greet()  # this means -> Employee.greet()
arpan.time()  # this means -> Employee.time()
