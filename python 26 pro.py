# File Reading

# f = open("hitesh.txt")
# content = f.read()
# print(content)
# f.close()

# f = open("hitesh.txt","r") # read default mode
# content = f.read()
# print(content)
# f.close()

# f = open("hitesh.txt","rb") # read default mode and "b" is binary mode
# content = f.read()
# print(content)
# f.close()

# f = open("hitesh.txt","rt") # read default mode and text is also default mode
# content = f.read()
# print(content)
# f.close()

# f = open("hitesh.txt","rt") # read default mode and text is also default mode
# content = f.read(4)
# print(content)
#
# content = f.read(4)
# print(content)        # It print another next letter
# f.close()

# f = open("hitesh.txt","rt") # read default mode and text is also default mode
# content = f.read(400)
# print("1",content)
#
# content = f.read(400)
# print("2",content)
# f.close()

# f = open("hitesh.txt","rt")
# content = f.read()
# for line in content:
#     print(line)
# f.close

# f = open("hitesh.txt","rt")
# content = f.read()
# for line in content:
#     print(line,end="")
# f.close

# f = open("hitesh.txt","rt")
# for line in f:
#     print(line,end="")
# f.close

# f = open("hitesh.txt","rt")
# print(f.readline())
# f.close()

# f = open("hitesh.txt","rt")
# print(f.readline(3),end="")
# f.close()

# f = open("hitesh.txt","rt")
# print(f.readline(),end="")
# print(f.readline(),end="")
# print(f.readline(),end="")
# print(f.readline(),end="")
# f.close()


f = open("hitesh.txt","rt")
# print(f.readlines())
content=f.readlines()
print(content)
f.close()
#
print(content[::])