#2) Write a program to check if a given number is even or odd
#Enter the number: 24
#24 is even number

intro=int(input("Enter the number: "))

if(intro%2==0):
    print(f"{intro} is a even number.")
else:
    print(f"{intro} is not an even number.")