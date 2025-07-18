# File Writing

print("Hello World")

# f = open("hridaan.txt","w")
# f.write("Hridaan is a little boy\n")
# f.write("Hridaan is a goob boy\n")
# f.close()

# f = open("hridaan.txt","w")
# content = f.write("Hridaan is a cleaver boy\n")
# cont = f.write("Hridaan is a goob boy\n")
# f.close()
#
# f = open("hridaan.txt","a")
# content = f.write("Hridaan is a little boy\n")
# print(content)
# f.close()
#
f = open("hridaan.txt","r+")
print(f.read())
f.write("Thank you\n")
f.close()