print("Hello World")

class student():
    pass
harry = student()
marry = student()
# print(harry,marry)

harry.name = "Harry"
harry.std = 12
harry.section = 1
# print(harry.name)
marry.std = 9
# print(marry.std)
# print(harry.name,marry.std)
marry.subjects = ["hindi","physic"]
print(harry.section,marry.subjects)