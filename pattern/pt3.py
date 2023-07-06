#simple pattern
num=int(input("Enter the number: "))
for i in range(0,num):
    for j in range(0,num):
        print("*", end=" ")
    print("\r")

num=int(input("Enter the number: "))
for i in range(0,num):
    for j in range(0,i+1):
        print("*", end=" ")
    print("\r")

num=int(input("Enter the number: "))
for i in range(0,num):
    for j in range(num-i):
        print("*", end=" ")
    print("\r")

num=int(input("Enter the number: "))
for i in range(0,num):
    for j in range(i,num):
        print(" ", end=" ")
    for j in range(i+1):
            print("*", end=" ")
    print("\r") 