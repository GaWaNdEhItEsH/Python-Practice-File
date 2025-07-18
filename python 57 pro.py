# Class Method As Alternative Constructor

class Employee:
    no_of_leaves = 8

    def __init__(self,nick_name,day_salary,role_play):
        self.name = nick_name
        self.salary = day_salary
        self.role = role_play

    @classmethod
    def from_dash(cls,string):              # Create Instance from string
        # params = string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

harry = Employee("Harry",455,"Instructor")
rohan = Employee("Rohan",4454,"Student")
karan = Employee.from_dash("Karan-5000-Coder")
# karan = rohan.from_dash("Karan-5000-Coder")
# karan = harry.from_dash("Karan-5000-Coder")

print(karan.name)
print(harry.salary)
print(rohan.role)

print()

print(karan.name)
print(karan.salary)
print(karan.role)
print(karan.no_of_leaves)