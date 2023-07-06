#2)Write a program which contains one class named as Circle
#Circle class contains three instance variables as Radius,Area ,Circumference.
#That class contains one class variable as PI which is initialize to 3.14
#Inside init method initialize all instance variables to 0.0
#There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference( ),
#,Display( )
#Accept method will accept value of Radius from user.
#CalculateArea () method will calculate area of circle and store it into instance variable Area.
#CalculateCircumference () method will calculate circumference of circle and store it into instance variable 
#Circumference.
#And Display( ) method will display value of all the instance variables as radius , Area , Circumference.
#After designing the above class call all instance methods by creating multiple objects

class Circle:
    PI=3.14

    def __init__(self) :
        self.radius=0
        self.area=0
        self.Circumference=0
        #self.Accept()
    def Accept(self):
        self.radius=float(input("Enter the radius of a circle:"))
    def CalculateArea(self):
        self.area = Circle.PI * self.radius * self.radius
        #self.area=self.__class__.PI*self.radius*self.radius
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.radius
    def display(self):
        print("Radius:",self.radius)
        print("Area:",self.area)
        print("Circumference:",self.Circumference)

def main():
    obj=Circle()
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.display()
if __name__=="__main__":
    main()
