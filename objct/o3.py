class Student:
    #constructor
    def __init__(self,name,course) -> None:
        self.name=name
        self.course=course
object1=Student("Rahul","Python")
print(object1.name)
object2=Student("Rahul","Python")
print(object1.course)
