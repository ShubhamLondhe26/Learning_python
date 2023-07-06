import module

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice=input("Select Number: ")

def main():
    num1=int(input("Enter the first Number: "))
    num2=int(input("Enter the Second Number: "))


    if choice=="1":
        ans=module.addition(num1,num2)
        print(ans)

    elif choice=="2":
        ans=module.subtraction(num1,num2)
        print(ans)

    elif choice=="3":
        ans=module.multiplication(num1,num2)
        print(ans)

    elif choice=="4":
        ans=module.division(num1,num2)
        print(ans)

    elif choice=="5":
        print("Thankyou!")
    else:
        print("Invalid Choice select again.")

if __name__=="__main__":
    main()

