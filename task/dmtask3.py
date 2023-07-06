#4) Write a program to find the largest number out of two numbers excepted
#from user
#Output:
#Enter First Number: 345
#Enter Second Number : 678
#Greater Number is 678

num=int(input("enter the number: "))
num1=int(input("enter the second number: "))

if(num>num1):
    print(f"{num} is greater than {num1}.")
elif(num1>num):
    print(f"{num1} is greater than {num}.")