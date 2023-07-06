#used to store the dat values but in form key:values
#syntax { : }seprated by ( , )
#ordered ,duplicates not allowed, mutable (can be changed)

#crating dictionary

dict1={"Monday":"Sleeping","Monday":"Python","Wednesday":"Pyhton","Thursday":"django","Friday":"cricket"}
print(dict1,len(dict1))
#print(dict1[Monday])#NameError: name 'Monday' is not defined
#duplicaates allowed in values

print(dict1["Friday"])
print(dict1["Thursday"])

dict={1:"Holiday","True":False,99.99:"pass",100:99}
print(dict,len(dict),type(dict))
print(dict[100])
print(dict[99.99])
print(dict["True"])

#adding
dict2={1:"Monday",2:"Tuesday"}
dict2[3]="sunday"
dict2["day"]="sunday"
print(dict2)

