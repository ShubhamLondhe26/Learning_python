class Animals:
    def __init__(self,breed,color) -> None:
        self.breed=breed
        self.color=color
    def display(self):
        print(self.breed,"-",self.color)
class Dog(Animals):
    def __init__(self, breed, color) -> None:
        super().__init__(breed, color)
class Cat(Animals):
    def __init__(self, breed, color) -> None:
        super().__init__(breed, color)
class Rabbit(Animals):
    def __init__(self, breed, color) -> None:
        super().__init__(breed, color)
obj=Dog("Shiba Inu","Brown")
obj.display()
obj1=Cat("Persian","White")
obj1.display()
obj2=Rabbit("Rex","Black")
obj2.display()
