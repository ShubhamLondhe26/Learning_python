#b) Write a program which accept one number from user and return addition of its factors
num=int(input("Enter the number: "))
for i in range(1,num+1):
    if num%i==0:
        print(i)

#addition of factors        
num=int(input("Enter the number: "))
sum=1
for i in range(1,num+1):
    if num%i==0:
        sum=sum+i
print(f"The addition of factor {num} is ",sum)



