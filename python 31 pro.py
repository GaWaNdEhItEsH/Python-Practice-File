print("Hello World")
print()
# with open("hitesh.txt") as f:
#     a = f.read(6)
#     print(a)

with open("hitesh.txt") as f:
    d = f.read()
    print(d)

print()

f= open("hitesh.txt")
print(f.readline())
print(f.tell())
f.close()

with open("hitesh.txt") as f:
    print(f.readline())
    print(f.readline())
    print(f.readlines())

