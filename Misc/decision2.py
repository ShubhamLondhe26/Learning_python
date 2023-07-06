#if...elif...else statement:
print("-"*50)

print("Enter any number between 1 to 7 :")
day = int(input())
if (day == 1):
    print(f"Day {day} : Monday working hours 9.30am to 6.30pm")
elif (day == 2):
    print(f"Day {day} : Tuesday - HOLIDAY")
elif (day == 3):
    print(f"Day {day} : Wednesday Meeting with client ")
elif (day == 4):
    print(f"Day {day} : Thursday half day from 9.30am to 2.30pm")
elif (day == 5):
    print(f"Day {day} : Friday Evening shift")
elif (day == 6):
    print(f"Day {day} : Saturday - HOLIDAY")
elif (day == 7) :
    print(f"Day {day} : Sunday - HOLIDAY")
else :
    print("please select day for 1 to 7")

print("-"*50)

print("Check whether the given number is positive,negative or zero")
print("please enter the number :",end ="")
num = float(input())
if (num > 0):
    print(f"{num} is positive number")
elif (num == 0):
    print(f"{num} is zero")
else :
    print(f"{num} is a negative number")

print("-"*50)
