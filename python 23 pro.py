# Function and Docstring

a= 9

b= 10

c=sum((a,b))
#print(c)

def function1():
    print("My name is Hridaan")
# function1()
# function1()
# function1()

def function2(a,b):
    print("The sum of a and b is",(a+b))
# function2(5,7)
# function2(50,20)

def function3(a,b):
    average=(a+b)/2
    #print(average)
    return average

v=function3(4552,45)
#print(v)

def function4(a,b,c):
    """This is a function which will calculate average of three number"""
    average=(a+b+c)/3
    return average

q=function4(2,8,14)
print(q)

print(function4.__doc__)