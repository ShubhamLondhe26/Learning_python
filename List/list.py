#list is a sequence data type which is used to store the collection
#create list

Roll_no=[122,123,123,124]#using integer
Percentage=[95.90,50.50,12.5,52.50]#using float
name=["rahul","shubham","aadesh"]#using string
mixed=["shubham",True,5j,23.22,123,123]

#ordered , sequence ,allow duplicates

print("Given List : ",mixed)
print("datatype : ",type(mixed))
print("its length : ",len(mixed))
print("its index ",mixed[0])
print("its index ",mixed[1])
print("its index ",mixed[2])
print("its index ",mixed[3])
print("its index ",mixed[4])
print("its index ",mixed[5])

print("its index ",mixed[3:5])#slicing

#concatenation

concatenation=Roll_no+Percentage
print(concatenation)


