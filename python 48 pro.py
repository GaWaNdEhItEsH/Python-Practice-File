# Map , Filter & Reduce function
print("Hello World")

# ______________________Map_________________

numbers = ["3","5","8","15","20"]
# print(numbers[2]+str(1))
# print(int(numbers[2])+1)
# numbers[3] = int(numbers[3])

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# print(numbers)
# numbers[4] = numbers[4] + 5
# print(numbers[4])

# map with function

# numbers_result = list(map(int,numbers))
# print(numbers_result)
# numbers_result[3] = numbers_result[3]+5
# print(numbers_result)

# numbers_result = tuple(map(int,numbers))
# print(numbers_result)
#numbers_result[3] = numbers_result[3]+5   # tuple is immutable
# print(numbers_result)

# map with lambda

# num = [2,3,8,5,4,9,65,9,9,3,10]

# square = list(map(lambda x:x*x , num))
# print(square)

# map with user define function

def sq(a):
    return a*a

def cube(a):
    return a*a*a

# numb = [2,3,5,7,8,3,6,5]
#
# squares = list(map(sq,numb))
# print(squares)
#
# cubes = list(map(cube,numb))
# print(cubes)

func = [sq,cube]
for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)

a = [1,2,3]
b = [4,5,6]

result = list(map(lambda x,y:x+y,a,b))
print(result)

result = list(map(lambda x,y:[x**2,y**3],a,b))
print(result)

# ____________________Filter_________________

list_1 = [1,2,3,4,5,6,7,8,9,10]

def is_greater_5(num):
    return num > 5
print(is_greater_5(150))

gr_than_5 = list(filter(is_greater_5,list_1))
print(gr_than_5)

# ____________________Reduce_________________

from functools import reduce

list1 = [1,2,3,4,5,6]
num = 0
for item in list1:
    num = num + item
print(num)

numb = reduce(lambda x,y:x+y,list1)
print(numb)