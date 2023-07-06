#Write a program which accept one number from user and return its factorial

count=int(input("Enter The number: "))
factorial=1
if(count<0):
    print("Negative does not exist")
elif(count==0):
    print(" factorial of 0! is 1")
else:
    for i in range(1,count+1):
        factorial=factorial*i

    print(f"{count} factorial is: ",factorial)

    







































