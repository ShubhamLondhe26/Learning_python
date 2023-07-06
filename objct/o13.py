#class Method
#syntax=classmethod(function)

class Student:
    Graduation="BCA"
    College="DY PATIL"

    def Collegedetails(cls):
        print("College:",cls.College)
        print("Garduation:",cls.Graduation)

def main():
    S1=Student
    S1.Collegedetails=classmethod(S1.Collegedetails)
    S1.Collegedetails()
    
if __name__=="__main__":
    main()
