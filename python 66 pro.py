# Diamond Shape Problem

print("Hello World")

class A:
    def get(self):
        print("This is a method from class A")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

a = A()
b = B()
c = C()
d = D()

d.get()

# ----------------------------------
class A:
    def get(self):
        print("This is a method from class A")
class B(A):
    def get(self):
        print("This is a method from class B")
class C(A):
    pass
class D(B,C):
    pass

a = A()
b = B()
c = C()
d = D()

d.get()

# ----------------------------------------------
class A:
    def get(self):
        print("This is a method from class A")
class B(A):
    def get(self):
        print("This is a method from class B")
class C(A):
    def get(self):
        print("This is a method from class C")
class D(B,C):
    pass

a = A()
b = B()
c = C()
d = D()

d.get()

# -----------------------------------------------------
class A:
    def get(self):
        print("This is a method from class A")
class B(A):
    def get(self):
        print("This is a method from class B")
class C(A):
    def get(self):
        print("This is a method from class C")
class D(C,D):
    pass

a = A()
b = B()
c = C()
d = D()

d.get()

#------------------------------------------------
class A:
    def get(self):
        print("This is a method from class A")
class B(A):
    def get(self):
        print("This is a method from class B")
class C(A):
    def get(self):
        print("This is a method from class C")
class D(C,D):
    def get(self):
        print("This is a method from class D")

a = A()
b = B()
c = C()
d = D()

d.get()

