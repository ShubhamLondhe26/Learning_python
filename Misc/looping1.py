#for loop using range() function
print("-"*50)
print("It will display number from 0 to 9")
for i in range(10):
    print(i)  

print("-"*50)
print("It will display number from 1 to 20")
for i in range(1,21):
    print(i)

print("-"*50)
print("It will display number from 2 to 20")
for i in range(2,21,2):
    print(i)

print("-"*50)
print("It will display number in list")
print(list(range(5,10,1)))
print(list(range(5,-5,-1)))
