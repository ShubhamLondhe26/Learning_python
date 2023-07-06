class Student:
    def __init__(self,name,course):
        self.name=name
        self.course=course

    def display(self):#using user defined function
        print(self.name," is learning ",self.course)
object1=Student("Shubham","python")
object1.display()