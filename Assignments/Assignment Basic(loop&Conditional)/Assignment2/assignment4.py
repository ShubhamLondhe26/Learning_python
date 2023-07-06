#d) Write a program which accept number from user and return addition of digits in that number (ex:input:45555 output:5)

num=int(input("Enter the number: "))
sum=0
while(num>0):
    sum=sum+1
    num=num//10
print(sum)
    







