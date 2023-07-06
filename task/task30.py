#wap to find the sum of first ten even numbers

num=int(input("Enter the number: "))
sum=0

for i in range(1,num+1):
    if i%2==0:
        sum=sum+i
print(f"The sum of {num} even number is",sum)



