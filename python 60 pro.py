# Single Inheritance In python

print("Hello World")

class Employee:
    no_of_leaves = 8

    def __init__(self,nick_name,day_salary,role_play):
        self.name = nick_name
        self.salary = day_salary
        self.role = role_play

    def print_details(self):
        return f"The name is {self.name} and salary {self.salary} and the role is {self.role}."

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves
        pass
    @classmethod
    def fron_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def print_good(string):
        print("This is good"+ string)

class Programmer(Employee):
    no_of_holiday = 10

    def __init__(self,nick_name,day_salary,role_play,languages):
        self.name = nick_name
        self.salary = day_salary
        self.role = role_play
        self.languages = languages

    def print_prog(self):
        return (f"The programmer name is {self.name} and salary {self.salary} and the role is {self.role}."
                f"The language are {self.languages}")

harry = Employee("Harry",455,"Instructor")
rohan = Employee("Rohan",4554,"Student")

shubham = Programmer("Shubham",555,"Programmer",["Python","CPP"])
karan = Programmer("Karan",800,"Programmer",["Python","CPP","Java"])

print(karan.print_prog())
print(shubham.print_prog())
print()
print(karan.no_of_leaves)
print(shubham.no_of_holiday)
print()
harry.change_leaves(30)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(shubham.no_of_leaves)
print(karan.no_of_leaves)
print()
karan.change_leaves(50)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(shubham.no_of_leaves)
print(karan.no_of_leaves)