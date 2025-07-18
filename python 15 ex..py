# Faulty Calculator
# 45 * 3 = 555 , 56+9 = 77, 56/9 = 4

print("Hello World")
print("You want to calculate something \nplease type y for YES and n for NO")
while (True):
    alp = input()
    if alp == "y":
        break
    elif alp == "n":
        exit()
    else:
        print("please enter y or n")
print("Enter your first number")
num1 = float(input())

while (True) :
    print("Enter your operator")
    ope = input()
    if ope == "+":
        break
    elif ope == "-":
        break
    elif ope == "*":
        break
    elif ope == "/":
        break
    elif ope == "**":
        break
    else:
        print("Please enter +,-,*,/,** only")
        continue


print("Enter your secound number")
num2 = float(input())

print("your ans is")

if (num1==45 and ope=="*" and num2==3):
    print("555")
elif (num1==3 and ope=="*" and num2==45):
    print("555")
elif (num1==56 and ope=="+" and num2==9):
    print("77")
elif (num1==9 and ope=="+" and num2==56):
    print("77")
elif (num1==56 and ope=="/" and num2==9):
    print("4")
elif (num1==9 and ope=="/" and num2==56):
    print("4")
elif ope == "+":
    print(num1 + num2)
elif ope == "-":
    print(num1 - num2)
elif ope == "*":
    print(num1 * num2)
elif ope == "/":
    print(num1 / num2)
elif ope == "**":
    print(int(num1)**int(num2))
else:
    print()

