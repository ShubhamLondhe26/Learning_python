#a)Write a program to find the sum of the digits of a number accepted by the user

number=int(input("enter the number: "))

sum=0
while(number>0):
    remainder = number%10
    sum = sum + remainder
    number = number//10
print("sum of digits: ",sum)
















