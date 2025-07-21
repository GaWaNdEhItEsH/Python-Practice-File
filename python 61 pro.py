# Multiple Inheritance

print("Hello World")

class Employee:
    no_of_leaves = 8
    var = 15

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

class Player:
    no_of_game = 4
    var = 20

    def __init__(self,name,game):
        self.name = name
        self.game = game

    def print_info(self):
        return f"The name is {self.name} and he played a {self.game}"

class CoolProgrammer(Employee,Player):
    language = "c++"
    #var = 25

    def print_language(self):
        print(self.language)

harry = Employee("Harry",455,"Instructor")
rohan = Employee("Rohan",4554,"Student")

shubham = Player("Shubham",["Cricket","Football"])
karan = CoolProgrammer("Karan",10000,"Programmer")

info = karan.print_details()
print(info)

karan.print_language()

print(karan.var)


