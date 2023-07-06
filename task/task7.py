#numbr=[1,2,4,5,7,8,10]
#output:Even:[2,4,8,10]
#more_even=[2,4,8,10,12,14,16]

number=[1,2,4,5,7,8,10]

del number[0]
del number[2:4]

print(number)

number.append(12)
number.insert(4,14)
number.extend([16])
print(number)



