#Creating string
# enclosed in single, double, triple quote
print("-"*50)
line1 = 'python is a programming language.'
line2 = "Python is designed by Guido Van Rossum and released in 1991."
line_3 = '''python syntax is easy as compared to other languages.
Python supports OOPS concept'''
print("About Python :", line1,line2,line_3)
print("Data type :", type(line1))
print("-"*50)
#Using different quotes in same statement
line1 = "'python is a programming language.'"
line2 = " 'Python is designed by Guido Van Rossum and released in 1991. ' "
line_3 =  '''python syntax is easy as compared to other languages.
Python supports OOPS concept'''
print("About Python :", line1,line2,line_3)
print("-"*50)
#index and slicing
line = "it's 7.30pm"
print(line[0])
print(line[2])
print(line[3])
print(line[4])
print(line[-3])
print(line[5:])
print("-"*50)
#same quote in same statement
#backslash \ is used as an escape character
print("print(\"hello world\")")
line = 'it\'s 7.30pm'
print(line)
print("length of line:",len(line))
print("-"*50)
# \n is a newline
line1 = 'python \nis a \nprogramming language.'
print(line1)
print("-"*50)
# \t is a tab
line1 = 'python\t is a\t programming language.'
print(line1)
print("-"*50)
# \r is a carriage return
line1 = 'python is a\r programming language.'
print(line1)
print("-"*50)
#string concatenation
Name = "Python "
Surname = "Version3"
Full_Name = Name +" " +Surname
print(Full_Name)
#String Formatting:
#String formatting is the process of infusing things in the string dynamically and presenting the string
Self = input("Enter your Name :")
print(f"My name is {Self}")#My name is kasturi
print("My name is {}".format(Self))#My name is kasturi
print('{0}{2}{1}'.format("kasturi", "is my ", "name"))#kasturinameis my










