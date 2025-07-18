# Lambda
import math

print("Hello World")

# def plus (a,b):                   # using function
#     return a+b
# print(plus(500,400))

# plus = lambda a,b : a+b             # using lambda ( write a function in single line using lambda )
# print(plus(300,400))

# def first(a):
#     return b[a]
# b = [[1,14],[5,6],[8,23]]
# print(first(2))

# def first(a):
#     return a[1]
# a = [[1,14],[5,6],[8,23]]
# print(first(a))

def first(a):
    return a[1]
a = [[1,14],[9,7],[5,6],[8,23]]
a.sort(key=first)
print(a)

a.sort(key=lambda x:x[1])
print(a)

# factorial_math = lambda b : math.factorial(b)
#
# print(factorial_math(20))