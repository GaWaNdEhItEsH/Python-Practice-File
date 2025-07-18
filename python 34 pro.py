# Iterative and Recursion Approach
print("Hello World")

# n! = n * n-1 * n-2 * n-3 * n-4 ______1
# n! = n * (n-1)!

# Iterative Method
# def factorial_iterative(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#         #print(fac)
#     return fac
#
# n = int(input("Enter a number\n"))
#
# print("Factorial using Iterative method",factorial_iterative(n))

print()

# Recursion Method
# def factorial_recursion(n):
#     if n == 1:
#         return 1
#     else:
#         v = n * factorial_recursion(n-1)
#         #print(v)
#         return v
#
# n = int(input("Enter a number\n"))
#
# print("Factorial using Recursion method",factorial_recursion(n))

# fibonacci using recursion method
# 0 1 1 2 3 5 8 13

def fibonacci_recursion(n):

    if n == 1 :
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

n = int(input("Enter a number\n"))

print("Fibonacci using Recursion method",fibonacci_recursion(n))


