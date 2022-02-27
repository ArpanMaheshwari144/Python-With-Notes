class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name of Passenger is {self.name}")
        print(f"Train of Passenger is {self.train}")


arpansform = RailwayForm()
arpansform.name = "Arpan"
arpansform.train = "GaribRath Express"
arpansform.printData()