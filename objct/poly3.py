class Mobile:
    def __init__(self,Model,color) -> None:
        self.breed=Model
        self.color=color
    def display(self):
        print(self.breed,"-",self.color)
class Apple(Mobile):
    def __init__(self, breed, color) -> None:
        super().__init__(breed, color)
class Vivo(Mobile):
    def __init__(self, breed, color) -> None:
        super().__init__(breed, color)
class Oppo(Mobile):
    def __init__(self, breed, color) -> None:
        super().__init__(breed, color)
obj=Apple("Iphone 14","Balck")
obj.display()
obj1=Vivo("V51","White")
obj1.display()
obj2=Oppo("Reno","Grey")
obj2.display()