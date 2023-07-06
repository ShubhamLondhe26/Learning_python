print("-"*50)
n = int(input("Enter Number:"))
for i in range(0,n):
    for j in range (0,n):
        print("*",end = " ")
    print("\r")
print("-"*50)
n = int(input("Enter Number:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end = " ")
    print("\r")
print("-"*50)
n = int(input("Enter the number of rows:"))
for i in range (n):
    for j in range(n-i):
        print("*",end =" ")
    print("\r")
print("-"*50)
