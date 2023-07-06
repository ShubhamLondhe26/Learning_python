num=int(input("Enter the first number: "))
num1=int(input("Enter the Second number: "))
num2=int(input("Enter the third number: "))

if(num>num1 or num2):
    print(f"{num} is greater than {num1} and {num2}.")
elif(num1>num2 or num):
    print(f"{num1} is greater than {num} and {num2}.")
elif(num2>num1 or num):
    (f"{num2} is greater than {num1} and {num}.")