class Student:
    graduation="BCA"#class variable
    def __init__(self,name,course) -> None:
        self.name=name
        self.course=course
obj=Student("Rahul","Python")
obj2=Student("aditya","Java")
print(obj2.graduation)
print(obj.__class__.graduation)