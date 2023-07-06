#nested statement:
print("-"*50)
print("check whether the number is positive , negative or zero:")
print("enter the number :",end ="")
num = float(input())
if num >= 0 :
    if num == 0 :
        print("It is zero!")
    else:
        print("Number is positive number")
else:
    print("Number is Negative number")
print("-"*50)
print("Enter the number:",end ="")
num1 = int(input())
if (num1 > 10) :
    print(f"{num1} is greater than 10")
    if (num1 > 20):
        print(f"{num1} also above 20")
    else:
        print(f"{num1} not above 20")

