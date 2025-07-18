# Enumerate Function

print("Hello World")

l1 = ["Bhindi","Vadapow","Aaloo","Tomato","Ladyfinger","Onion"]
# i = 0
# for item in l1:
#     if i%2 == 0:    # Take the reminder if i is divided by 2
#         print(item)
#     i+=1

# i = 0
# for item in l1:
#     print(i % 2)
#     i+=1

# i = 0
# for item in l1:
#     if i%2 == 1:    # Take the reminder if i is divided by 2
#         print(item)
#         print(i % 2)
#     i+=1

# i = 1
# for item in l1:
#     if i%2 == 1:    # Take the reminder if i is divided by 2
#         print(item)
#         print(i % 2)
#     i+=1

# i = 1
# for item in l1:
#     if i%2 == 0:    # Take the reminder if i is divided by 2
#         print(item)
#         print(i % 2)
#     i+=1

# i = 1
# for item in l1:
#     if i%2 != 0:    # Take the reminder if i is divided by 2
#         print(f"Please buy {item}")
#     i+=1
# print()

# l1 = ["Bhindi","Vadapow","Aaloo","Tomato","Ladyfinger","Onion"]
for index,item in enumerate(l1):
    if index%2 == 0:
        print(f"Please Sell {item}")

print()

for index,item in enumerate(l1):
    if index == 0:
        # print(f"Please Sell book")
        index +=1
    if index%2 == 0:
        print(f"Please hold {item}")

print()

for index,item in enumerate(l1):
    print(index,item)

print()

for index,item in enumerate(l1):
    index+=1
    print(index,item)