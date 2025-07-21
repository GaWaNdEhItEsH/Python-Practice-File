# Overriding and Super

print("Hello World")

class A:
    classvar1 = "I am Harry in class A"

    def __init__(self):
        self.var1 = "I am Harry in class A constructor"
        self.classvar1 = "Instance variable in class A"
        self.special = "Special variable in class A"
class B(A):
    pass
    classvar1 ="I am Merry in class B"

    def __init__(self):
        super().__init__()
        self.var1 = "I am Merry in class B constructor"
        self.classvar1 = "Instance variable in class B"
        print()
        print(super().classvar1)


harry = A()
merry = B()
print(merry.classvar1)
print(merry.special,merry.var1,merry.classvar1)
