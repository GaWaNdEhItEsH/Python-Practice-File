# Public Protected and Private Access Specifier & Name Mangling In Python

print("Hello World")

class Employee:
    no_of_leaves = 8        # Public variable
    var = 15
    _protect = 20           # Protect is a Protected variable
    __private = 60          # It's a private variable

    def __init__(self,a_name,a_salary,a_role):
        self.name = a_name
        self.salary = a_salary
        self.role = a_role

    def print_details(self):
        return f"The name is {self.name} and salary {self.salary} with role {self.role}"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod

    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod

    def print_statement(string):
        print(f"This is multiple inheritance method {string}")

harry = Employee("Harry",455,"Instructor")

print(harry._protect)

print(harry._Employee__private)