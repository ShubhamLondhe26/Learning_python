#course=["python","angular","react","java","nodejs"]
#output  frontend=["angular","react"]  backend=["python","java","nodejs"]

course=["python","angular","react","java","nodejs"]
course.pop(0)
course.pop(2)
print("Frontend =",course)

course1=[]
course1.insert(2,"nodejs")
course1.insert(1,"java")
course1.insert(0,"python")


print("Backend =",course1)



 