class Cars:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display(self):
        print(self.brand,"-",self.color)

class Scooty:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display(self):
        print(self.brand,"-",self.color)  
class Bike:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display(self):
        print(self.brand,"-",self.color)      

obj=Cars("BMW","White")
obj1=Scooty("Jupiter","purple")
obj2=Bike("Splendor","balck")

for vehicle in (obj,obj1,obj2):
    vehicle.display()