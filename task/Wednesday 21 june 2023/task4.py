#4) Write a recursive program which accept number from user and return its factorial
#Input : 5
#Output :  120
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num * factorial(num - 1)
def main():
    value=int(input("Enter the number: "))
    value1=value
    sum=factorial(value)
    print(f"The factorial of {value1} is {sum}")

if __name__=="__main__":
    main()