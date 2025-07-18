# Static Method In Python

print("Hello World")

class Employee:
    no_of_leaves = 8

    # def __init__(self, nick_name, day_salary, role_play):
    #     self.name = nick_name
    #     self.salary = day_salary
    #     self.role = role_play

    @staticmethod              # This method used for regular define function in class but work on only Employee class.
    def print_good(string):
        print("This is good",string)

# harry = Employee("Harry",455,"Instructor")
# rohan = Employee("Rohan",4554,"Student")

harry = Employee()
rohan = Employee()

Employee.print_good("Marry")
harry.print_good("Ritesh")
rohan.print_good("Ram")