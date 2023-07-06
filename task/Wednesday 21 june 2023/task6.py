#6)Write a program which contains one lambda function which accepts two parameters and return its multiplication
multiplication=lambda x,y: x*y
def main():
    value=int(input("Enter the number: "))
    value1=int(input("Enter the number: "))
    result=multiplication(value,value1)
    print(f"The multiplication is {result} ")
if __name__=="__main__":
    main()