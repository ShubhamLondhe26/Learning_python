#5) Write a program to print a table of a number entered by the user
#Output: Multiplication of table: 5
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15


num=int(input("Enter the number: "))

for i in range(1,11):
    multi=num*i
    print(f"{num} x {i} = ",multi)
