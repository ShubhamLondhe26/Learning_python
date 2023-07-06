#string
course={"python","java","Angular","python"}
print(len(course))#3 because of duplicates
#print(course[0])#TypeError: 'set' object is not subscriptable

#add method -> add an items to the set
course.add("Nodejs")
print(course)

#update method -> add items from another set to current set

more_course={"reactjs","mongodb"}
course.update(more_course)
print(course)

more_course=["reactjs","mongodb"]#adding list
course.update(more_course)
print(course)

more_course=("reactjs","mongodb")#adding tuple
course.update(more_course)
print(course)