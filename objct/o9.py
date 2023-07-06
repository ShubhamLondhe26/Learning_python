class Student:
    def __init__(self,name,age,course):

        self.name=name
        self.age=age
        self.course=course
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Course: ",self.course)

    def Modify_info(self):
        edit_course=input("Enter the course name to change: ")
        self.course=edit_course
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Course: ",self.course)

def main():
    obj=Student("Shubham",23,"Python")
    obj.display()
    obj.Modify_info()

if __name__=="__main__":
    main()