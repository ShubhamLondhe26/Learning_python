# 1) Write a Program to check if a given year is leap year or not
print("enter the year")
year=int(input())
if((year%400==0) or (year%100!=0) and (year%4==0)):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")


# 2) Write a program to check if a given number is even or odd

print("Enter the number :")
num=int(input())
if(num%2==0):
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# 3) Write a program which accepts number and display whether the number is 
# positive ,negative or zero

print("Enter the number :")
num=int(input())
if(num>0):
    print(f"{num} is positive")

elif(num<0):
    print(f"{num} is negative")
else:
    print(f"{num} is zero")

# 4) Write a program to find the largest number out of two numbers excepted 
# from user

print("Enter the number 1 :")
num1=int(input())
print("Enter the number 2 :")
num2=int(input())
if(num1>num2):
    print(f"{num1} is the largest")
else:
    print(f"{num2} is the largest")

# 5)Write a program to whether a number (accepted from user ) is divisible by 
# 2 and 3 both

print("Enter the number :")
num=int(input())
if((num%2==0) and (num%3==0)):
    print(f"{num} is divisible by 2 and 3")
else:
    print(f"{num} is not divisible by 2 and 3")