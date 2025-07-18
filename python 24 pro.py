print("Hello World")

print("Enter num1")
num1=input()
print("Enter num2")
num2=input()         # if you type latter insted of number it will gives you an error,
                     # for passing error we used "try:" and "except"
try:
    print("The sum of these two number is",
      int(num1)+int(num2))
except Exception as e:
    print(e)

print()

print("This is important line")