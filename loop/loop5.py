#dict
course={"python":25000,"java":24000,"angular":23000}
for i in course:
    print(i)
for i in course:
    print(i,course[i])

for i in course:
    print(i,course.get(i))

course1=course.keys()
print(course1,type(course1))

