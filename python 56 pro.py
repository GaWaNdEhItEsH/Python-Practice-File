# Class Method

print("Hello World")

class Employee:
    no_of_leaves = 8

    # def __init__(self,nike_name,day_salary,role_play,read_book):
    #     self.name = nike_name
    #     self.salary = day_salary
    #     self.role = role_play
    #     self.read = read_book

    def print_details(self):
        return (f"The name is {self.name} and salary per day is {self.salary} and role is {self.role} and he read a book "
                f"{self.book}.")

    @classmethod               # this method used to change class variable using class Employee or object.
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves
        return "hello"


# harry = Employee("Harry",455,"Instructor","Think and Grow Rich")
# rohan = Employee("Rohan",4454,"Student","Rich Dad And Poor Dad")
harry = Employee()
rohan = Employee()
# print(harry.name)
print(harry.no_of_leaves)
Employee.no_of_leaves = 20
print(harry.no_of_leaves)

print()

rohan.change_leaves(35)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)

print()

print(Employee.change_leaves(50))
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)
print(harry.no_of_leaves)
