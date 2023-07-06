#parent
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname,self.lname)
#child
class Student(Person):
    def __init__(self, fname, lname,percentage):
        super().__init__(fname, lname)
        self.percentage=percentage
    def studentinfo(self):
        print("Welcome to hematite",self.fname,self.lname)
p1=Student("Shubham","Londhe",75)
p1.studentinfo()
print(p1.percentage)
