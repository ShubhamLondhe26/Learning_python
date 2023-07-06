#Write a program which accept number from user and return number of digits in that number(ex:input:45555 output:24)


num=int(input("Enter the number:"))
sum=0
while(num>0):
    remainder = num%10
    sum = sum + remainder
    num = num//10
print("sum of digits: ",sum)