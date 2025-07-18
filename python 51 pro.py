# Decorators
from tkinter.font import names

print("Hello World")

# def function1():
#     return "Subscribe now"
# print(function1())
# func2 = function1()
# print(func2)

# def function1():
#     return "Subscribe now"
# print(function1())
# func2 = function1()
# del function1
# print(func2)

# def funcret(num):          # print function using function
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
# a = funcret(0)
# print(a)

# def executor(fun):
#     fun("this is")
# executor(print)

## Decorators

# def dec1(func1):
#     def nowexec():
#         print("Executing Now")
#         func1()
#         print("Executed")
#     return nowexec
#
# def who_is_harry():
#     print("Harry is a good boy")
#
# decorated = dec1(who_is_harry)
# decorated()

# def dec1(func1):
#     def nowexec():
#         print("Executing Now")
#         func1()
#         print("Executed")
#     return nowexec
# @dec1
# def who_is_harry():
#     print("Harry is a good boy")
# who_is_harry()

nick_name = {"Sonu":35,"Monu":38,"Rohan":30,"Harry":35,"Bhanu":40}
nick = ["hitesh","Pawan","lali","Goli","Tappu","Tapsi"]

# def decorator_function(original_function):
#     def wrapper_function(*args,**kwargs):
#         print("Arguments passed:",args,kwargs)
#         return original_function(*args,**kwargs)
#     return wrapper_function
# def greet(name,age):
#     print(f"Hello {name} you are {age} year old.")
# decorated = decorator_function(greet)
# decorated("Hitesh",35)


def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        for key in args:
            print(key,end=" ")
        print()
        original_function(*args,**kwargs)
        for key,value in kwargs.items():
            print(f"{key} is {value} year old")
    return wrapper_function

@decorator_function

def greet(*name,**age):
    for i in name:
        print(f"Hello {i} how are you.")
    for i,j in age.items():
        print(f"{i} are {j}")
greet(*nick,**nick_name)
