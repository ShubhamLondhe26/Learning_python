count=int(input("Enter the number"))

for i in range(0,count):
    for j in range(count-i):
        print("*",end=" ")
    print("\r")