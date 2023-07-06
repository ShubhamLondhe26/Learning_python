#5)Write a program to whether a number (accepted from user ) is divisible by
#2 and 3 both
#Output:
#Enter the number: 343
#Not Divisible
#Enter the number :456
#Divisible

num=int(input("enter the number: "))
if(num%2==0 and num%3==0):
    print(f"{num} is divisible by 2 and 3.")
else:
    print(f"{num} is not divisible by 2 and 3.")
