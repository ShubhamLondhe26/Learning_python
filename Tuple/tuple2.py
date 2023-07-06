#importnat features of tuple -> assigning LHS=RHS
#packing and unpacking

#x=("rahul",27,15000,True)
#(name,age,salary,Pass)=x
#print(name)
#print(age)

x=("rahul",27,15000,True)
(name,age,*salary)=x  # * is used as single variable assigned multiple values
print(name)
print(salary)

t1=('python')  # * will consider as a string
print(t1,type(t1))

t2=(2)   # * will consider as a  int
print(t2,type(t2))

