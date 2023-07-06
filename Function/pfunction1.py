
def circumference(radius,pi=3.14):
    calc=2*pi*radius
    return calc 


def main(): 
    radius=int(input("Enter the value: "))
    ans=circumference(radius,pi=3.14)
    print("Area of circumference is: ",ans) 

if __name__=="__main__":
    main()