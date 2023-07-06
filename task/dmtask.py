#1) Write a Program to check if a given year is leap year or not
#Output:
#Enter the year :2000
#Given year is leap year

intro=int(input("enter the year: "))

if(intro%4==0 and intro%100!=0):
    print(f"{intro} is the leap year.")
elif(intro%400==0 and intro%100==0):
    print(f"{intro} is the leap year.")
else:
    print(f"{intro} is not a leap year.")