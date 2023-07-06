#using for loop
num=int(input("Enter the number: "))
factorial=1
if(num<0):
    print("negative does not exist")
elif(num==0):
    print(" factorial of 0! is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(f"{num} factorial is: ",factorial)

#using while loop

num=int(input("Enter the number: "))
i=1
while(i<=int(num/2)):
    if(num%i==0):
        print(i)
    i=i+1
