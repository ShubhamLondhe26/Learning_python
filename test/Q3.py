#3.Write a program to reverse the number accepted from user using while loop

num=int(input("Enter the Number: "))
sum=0
while (num>0):
    sum=(sum*10)+num%10
    num=num//10
print(f"The reverse order of {num} is ",sum)