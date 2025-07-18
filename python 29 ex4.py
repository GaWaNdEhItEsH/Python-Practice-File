# from logging import exception

print("Hello World")

# Basic Rectangle Pattern
# rows = 5
# cols = 3
# for i in range(rows):          # range(start,stop,step)
#     for j in range (cols):     # default value of start = 0 & step = 1
#         print("*",end=" ")
#     print()
# print()

# Triangle Pattern
# rows = 5
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# print()

# Inverted Triangle
# rows = 5
# for i in range(rows, 0 , -1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# print()

#Number Patterns
# rows = 5
# for i in range(rows):
#     for j in range(i + 1):
#         print(j + 1,end=" ")
#     print()
# print()

#Space Patterns
# rows = 5
# for i in range(rows):
#     print(" " * (rows - i - 1),end=" ")
#     for j in range(i + 1):
#         print("*",end=" ")
#     print()

# Exercise 4

# rows = int(input("Enter a logic number\n"))
# boolen = int(input("Enter a boolen value 1 or 0\n"))
# if boolen == True:
#     for i in range(rows):
#         for j in range(i + 1):
#             print("*",end=" ")
#         print()
# elif boolen == False:
#     for i in range(rows,0,-1):
#         for j in range(i):
#             print("*",end=" ")
#         print()

# Triangle Star Pattern
# n = 5
# for i in range (1 , n+1):
#     print("*" * i)
#
# print()

# Invert Triangle star Pattern

# for i in range (5 , 0 ,-1):
#     print("*" * i)
#
# print()

# Triangle number pattern

# for i in range (1,n+1):
#     print(str(i) * i)
#
# print()

# Triangle number pattern

# rows = 5
# for i in range(1,rows+1):
#     for j in range(1,i + 1):
#         print(j ,end=" ")
#     print()
# print()

# Invert Triangle number pattern

# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(j , end=" ")
#     print()

# Pyramid Star Pattern

# rows = 5
# for i in range(1,rows+1):
#     print(" " * (rows - i),end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# Pyramid Star Pattern

# for i in range(1,rows+1):
#     print(" " * (rows-i),"* " * i )
#
#
# print()

# Invert Pyramid Star Pattern

# for i in range(rows,0,-1):
#     print(" " * (rows - i),"* " * i)
#
# print()

# Pyramid Number Pattern

# rows = 5
# for i in range(1,rows+1):
#     print(" " * (rows-i),end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# Exercise 4

# try:
#     rows = abs(int(input("Enter a magic number\n")))        # 'abs' function convert negative value in positive one.
#     def retry():
#         boolen = int(input("Enter a boolen value 1 or 0\n"))
#         if boolen == True:
#             for i in range(1, rows + 1):
#                 print("* " * i)
#         elif boolen == False:
#             for i in range(rows, 0, -1):
#                 print("* " * i)
#         elif boolen != True or False:
#             retry()
#     retry()
# except:
#     print("Try again")

try:
    n = abs(int(input("Enter a magic number\n")))
    boolen = int(input("Enter a boolen value 1 or 0\n"))

    if boolen == True:
        i = 1
        while (i <= n):
            print("* " * i)
            i = i + 1

    elif boolen == False:
        i = n
        while (i != 0):
            print("* " * i)
            i = i - 1
    else:
        print("Try Again")

except:
    print("Try Again ")
