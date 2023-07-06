#c) Write a program to reverse the number accepted by the user using a while loop

num= int(input("Enter a number: "))
rev=0
while(num>0):
    rev=(rev*10)+num%10
    num=num//10
print("The reverse order of  is ",rev)
