#3) Write a program which accepts number and display whether the number is
#positive ,negative or zero
#Output:
#Enter the number : 567
#567 is positive number
#Enter the number : -34
#-34 is negative number

num=int(input("enter the number: "))
if(num>0):
    print(f"{num} is an positive number.")
elif(num==0):
    print("please enter the higher number than 0")
else:
    print(f"{num} is an ngative number.")