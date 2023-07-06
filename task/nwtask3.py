#3) Write a program that accepts details from user and display also check type() of FullName,RollNumber,Percentage Student details: FullName , Course ,RollNumber, Percentage

fullname=input("Enter your name: ")
roll_no=int(input("Enter your Roll No.: "))
course=input("Enter your Course name: ")
percentage=float(input("Enter your Percentage: "))

print("Student Details/n")
print("Student Name: ",fullname,type(fullname))
print("Student Roll No.: ",roll_no,type(roll_no))
print("Student Course: ",course,type(course))
print("Student Percentage: ",percentage,type(percentage))