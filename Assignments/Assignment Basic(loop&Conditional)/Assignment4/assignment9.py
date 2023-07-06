#Write a program to check whether a number entered is a three-digit
#number or not.
#(Input: 12 Output: Not a three-digit number)

num=int(input("Enter the number: "))
if(num>100 and num<1000):
    print(f"{num} is a three digit number")
else:
    print(f"{num} is not a three digit number")