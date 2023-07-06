print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice=input("Select Number: ")

if choice=="1":
    num=int(input("Enter th5 first Number: "))
    num1=int(input("Enter th5 first Number: "))
    num2=num+num1
    print(f"The addition of {num} and {num1} is",num2)

elif choice=="2":
    num=int(input("Enter the first Number: "))
    num1=int(input("Enter the first Number: "))
    num2=num-num1
    print(f"The subtracion of {num} and {num1} is",num2)

elif choice=="3":
    num=int(input("Enter the first Number: "))
    num1=int(input("Enter the first Number: "))
    num2=num*num1
    print(f"The multiplication of {num} and {num1} is",num2)

elif choice=="4":
    num=int(input("Enter the first Number: "))
    num1=int(input("Enter the first Number: "))
    num2=num/num1
    print(f"The division of {num} and {num1} is",num2)

elif choice=="5":
    print("Thankyou!")
else:
    print("Invalid Choice select again.")
