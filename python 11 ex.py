dicti={"Egg":"Unda","Hen":"Murgi","Goat":"Bakri","Rice":"Chawal","Carrot":"Gajar","Watermelon":"Tarbuj","12":"6"}
print(len(dicti))
print("Please Enter a Word")
word = input()
print("Your meaning of word")
print(dicti[word])
print()
for item in dicti:
    print(item , end="  ")

print()

for item,value in dicti.items():
    print(value , end="  ")

