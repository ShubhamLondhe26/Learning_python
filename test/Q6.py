#6.Write a program which accept year from user and check whether the given year is leap year or not?

num=int(input("Enter the Year: "))

if(num%4==0 and num!=100):
    print(f"{num} is a leap year.")
elif(num%400==0 and num%100==0):
    print(f"{num} is a leap year.")
else:
  print(f"{num} is not a leap year.")

