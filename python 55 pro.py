# Self and __init__() constructor

# print("Hello World")
#
# class Employee:
#     no_of_leaves = 8
#
#     def print_details(self):
#         return f"The name is {self.name} and salary is {self.salary} and role is {self.role}."
#
# harry = Employee()
# rohan = Employee()
#
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "student"
#
# print(harry.print_details())
# print(rohan.print_details())

# class Employee:
#     no_of_leaves = 8
#
#     def __init__(self,nickname,day_salary,role_play):
#         self.name = nickname
#         self.salary = day_salary
#         self.role = role_play
#
# harry = Employee("Harry",455,"Instructor")
# rohan = Employee("Rohan",4554,"Student")
# print(rohan.role)

class Employee:
    no_of_leaves = 8

    def __init__(self,nickname,day_salary,role_play,book_read):
        self.name = nickname
        self.salary = day_salary
        self.role = role_play
        self.book = book_read

    def print_details(self):
        return (f"The name is {self.name} and salary per day is {self.salary} and role is {self.role} and he read a book "
                f"{self.book}.")

harry = Employee("Harry",455,"Instructor","Think And Grow Rich")
rohan = Employee("Rohan",4554,"Student","Rich Dad And Poor Dad")

print(rohan.book)
print(rohan.print_details())

