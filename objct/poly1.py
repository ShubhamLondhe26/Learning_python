class Vehicle:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display(self):
        print(self.brand,"-",self.color)
class Car(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand, color)
class Scooty(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand, color)
class Bike(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand, color)
obj=Car("BMW","Black")
obj.display()
obj=Scooty("Jupiter","indigo")
obj.display()
obj=Bike("Splendor","Black")
obj.display()
