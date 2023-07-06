#Result

percentage=float(input("Enter your percentage: "))
if(percentage>=90):
    print(f"{percentage} falls under A grade")
elif(percentage>=80 and percentage<=90):
    print(f"{percentage} falls under B grade")
elif(percentage>=60 and percentage<=80):
    print(f"{percentage} falls under C grade")
else:
    print(f"{percentage} falls under D grade")
    