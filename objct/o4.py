class Student:
    def __init__(self,name,course):
        self.name=name
        self.course=course

    def __str__(self):
        return f"{self.name}  is learning {self.course}"
object1=Student("Shubham","python")
print(object1)