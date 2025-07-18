print("Hello World")

i=0

# while (i<45):
#     print(i+1,end= " ")
#     i=i+1

# while (True):
#     print(i+1 , end=" ")
#     if i==44:
#         break
#     i=i+1

while (True):
    if i+1<5:
        i=i+1
        continue          # below that line not executive and go up in loop until the 'if i+1<5' condition are false.
    print(i+1 , end=" ")
    if i==44:
        break
    i=i+1

print()

#Quiz

# while (True):
#     print("Enter a number \n")
#     inte=int(input())
#     print()
#     if inte > 100:
#         print("Congrats you enter a number greater than 100 \n")
#         break
#     else:
#         print("Try Again \n")
#         continue

