#c) Write a program which accept one number from user and check whether number is prime or not

num=int(input("Enter the number: "))
for i in range(2,num):
    if num%2==0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")