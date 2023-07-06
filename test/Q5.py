#5.Write a program which accept one number from user and return its factors 

num=int(input("Enter the Number: "))

for i in range(1,num+1):
    if num%i==0:
        print(f"The factors of {num} is ")
        print(i)

