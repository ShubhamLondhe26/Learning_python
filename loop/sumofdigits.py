print("Enter the number from user for sum of digits: ")
number=int(input("enter the number: "))

sum=0
while(number>0):
    remainder = number%10
    sum = sum + remainder
    number = number//10
print("sum of digits: ",sum)


#multiplication

print("Enter the number from user for sum of digits: ")
number=int(input("enter the number: "))

multi=1
while(number>1):
    remainder = number%10
    multi = multi * remainder
    number = number//10
print("sum of digits: ",multi)
