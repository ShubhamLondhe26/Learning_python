def addition(num1,num2):
    print("addition",num1,num2)
    add=num1+num2
    return add
def subtraction(num1,num2):
    print("subtraction",num1,num2)
    sub1=num1-num2
    return sub1
def multiplication(num1,num2):
    print("multiplication",num1,num2)
    multi=num1*num2
    return multi

def main():
    num1=int(input("Enter the number: "))
    num2=int(input("Enter the number: "))
    add1=addition(num1,num2)
    print(add1)
    sub1=subtraction(num1,num2)
    print(sub1)
    multi1=multiplication(num1,num2)
    print(multi1)
if __name__=="__main__":
    main()
