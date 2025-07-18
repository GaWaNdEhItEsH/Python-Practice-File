# Globle Variable
print("Hello World")

l = 10 # Globle variable

# def function1(n):
#     print(l)
#     print(n,"I have printed")
#
# function1("This is me")
# print(l)

# def function1(n):
#     l = 5
#     m = 8
#     print(l,m)
#     print(n,"I have printed",l)
#
# function1("This is me")
# print(l)

# def function1(n):
#     #l = 5
#     m = 8
#     global l
#     l = l+10
#     print(l,m)
#     print(n,"I have printed",l)
#
# function1("This is me")
# print(l)

def harry():
    x=20
    def rohon():
        global x
        x=88
    print("before calling rohan",x)
    rohon()
    print("after calling rohon", x)
harry()

print(x)
