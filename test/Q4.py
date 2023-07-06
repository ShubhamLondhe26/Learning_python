#4.Write a program which accept one number from user and   return its factorial

num=int(input("Enter the Number: "))
factorial=1
if (num==0):
    print("0 factorial is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(factorial)
    