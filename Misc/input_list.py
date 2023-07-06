#Dynamic input in list:
print("Get a list as input from user:")

data_input = []
print("Enter the number of elements:")
size = int(input())

print("please enter the values")

for i in range(0,size):
    no = int(input())
    data_input.append(no)

print(data_input)
print(type(data_input))