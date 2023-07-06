#set-> built in function, stores multiple values
#syntax-> { } sperated by comma
#unordered, unindexed, not allow duplicat values 
#mutable boject(changes using methods)

#set creation
#integer
whole_numbers={0,1,2,3,4,5,6}

#string
Course={"Python","mongo","Angular"}

#Boolean
Is_pass={True,False,False}

#Htrogenous
mixed={"Python",True,12.3,11}


print("Creating set using integer:",whole_numbers,"Datatype:",type(whole_numbers),"length:",len(whole_numbers))
print("Creating set using string :",Course,"Datatype:",type(Course),"length:",len(Course))
print("Creating set using Boolean:",Is_pass,"Datatype:",type(Is_pass),"length:",len(Is_pass))
print("Creating set using Hetrogenous:",mixed,"Datatype:",type(mixed),"length:",len(mixed))

#Example1

example={True,1,1,2,3}
print(example)

