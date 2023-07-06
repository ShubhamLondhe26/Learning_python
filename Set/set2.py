#Remove and discard method

#num={1,2,3,4,5}

#remove
#num.remove(1)
#num.remove(10) #KeyError: 10
#print("using remove method: ",num)

#discard method

num1={1,2,3,4,50}
num1.discard(50)
print("using discard method: ",num1)

#union and intersection method

set1={2,4,6,8,10,12,14}
set2={1,2,3,4,5,6,7,8,9}
#using pip (|) operator
set3 = set1|set2
print("using pip |  operator: ",set3)

#also using union method

set4=set1.union(set2)
print("using union method: ",set4)
print()

#intersection method

#using & operator

set5=set1&set2
print("using & operator:",set5)

#also using intersection method

set6=set1.intersection(set2)
print("using intersection method:",set6)

#difference method

course1={'Python','Java','Power bi','angular','react'}
course2={'Tableau','Java','Data Analytics','angular','react'}

#using Operator

print("using - operator: ",course1-course2)#using - operator:  {'Power bi', 'Python'}
course3=course1.difference(course2)
print("using difference method ", course3)#using difference method  {'Power bi', 'Python'}
print()
print('using - operator',course2-course1)#using - operator {'Data Analytics', 'Tableau'}