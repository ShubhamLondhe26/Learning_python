#4.Write a program which will sort a dictionary by value in python using lambda function

values=[{"name":"Shreya","age":15},{"name":"Pratiksha","age":13},{"name":"Bala","age":14}]

sorted_data = sorted(values, key=lambda x: (x["age"], x["name"]))
print("Sorting by age and name:")
print(sorted_data)

# Sorting by age in descending order
sorted_data_descending = sorted(values, key=lambda x: x["age"], reverse=True)
print("Sorting by age in descending order:")
print(sorted_data_descending)
