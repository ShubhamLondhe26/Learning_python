string1="I'll do it tomorrow"
#type
print(type(string1))
#len
print(len(string1))
#index
print(string1[0])
print(string1[2])
print(string1[3])
#slicing
print(string1[10:])
#concatenation

intro=input("enter your first name: ")
intro1=input("enter your last name: ")
print("your full name is: ",intro+" "+intro1)

#Escape character

string2='he\'ll talk to you later'
print(string2)

#\n

string2='he\'ll talk to you\n later'
print(string2)

#\t
string2='he\'ll talk to\t you\t later'
print(string2)

#list
l1=["Chicken","Noodles","Non-Veg momos","Chilly paneer"]

#add
l1.append("Veg-Momos")
l1.append("chilly chicken")
print(l1)

#item not available
print("Items not available: ",l1[2:4])

#size
print(l1.__sizeof__())

#tuple
#index

l2=("Chicken","Noodles","Non-Veg momos","Chilly paneer")
l3=l2.index("Noodles")
print(l3)

#count
l3=l2.count("Noodles")
print(l3)

