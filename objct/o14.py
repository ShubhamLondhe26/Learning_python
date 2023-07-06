class Student:
    Graduation="BCA"
    College="DY PATIL"

    @classmethod
    def Collegedetails(cls):
        print("College:",cls.College)
        print("Garduation:",cls.Graduation)

def main():
    Student.Collegedetails()
if __name__=="__main__":
    main()