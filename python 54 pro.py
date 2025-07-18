# Instance and class variable

print("Hello World")

class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"   # Here name,salary,role is an instance
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

# print(harry.__dict__)
# print(rohan.name)
# print(harry.no_of_leaves)    # you can only access class variable with object
# print(rohan.no_of_leaves)
# print(Employee.no_of_leaves)
print(rohan.__dict__)
Employee.no_of_leaves = 10    # you can change class variable with class
# print(Employee.no_of_leaves)
rohan.no_of_leaves = 15      # you can not change class variable with object, rather than that it create another instance.
print(rohan.__dict__)
print(Employee.__dict__)
