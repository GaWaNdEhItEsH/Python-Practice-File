# For loop in python

# list1 = ["Hridaan","Hitesh","Nitesh","Shital","Pen","Paper","Pencil"]
# print(list1)
# print(len(list1))

# for item in list1:
#     print(item)

list1 = [["Hridaan",5],["Hitesh",4],["Nitesh",6],["Shital",8],["Pen",10],["Paper",12],["Pencil",15]]

# for item in list1:
#     print(item)

# for item,candi in list1:
#     print(item,"eat chocolate",candi)

# for item,candi in list1:
#     print(candi)


# out_list1 = []
# out_list2 = []
#
# for item,candi in list1:
#     out_list1.append(item)
#     out_list2.append(candi)
# print(out_list1)
# print(out_list2)
#
# for x in out_list1:
#     out_list2.append(x)
#
# print(out_list2)

# list1.sort()
# print(list1)
# list1.sort(key=lambda x:x[0])
# print(list1)
# list1.sort(key=lambda x:x[1])
# print(list1)


# list2 = [[5,4,8],[6,8,7],[4,7,3],[17,15,14]]
#
# for item,pin,red in list2:
#     print(item,end=" ")
#
# print()
#
# list2.sort(key=lambda x:x[2])
# print(list2)


dict1 = dict (list1)
print(type(dict1))
print(dict1)

for item,candi in dict1.items():
    print(item,candi,end=" ")

print()

for item,candi in dict1.items():
    print(candi,end=" ")

print()

line = [int,float,"Harry",5,3,3,22,21,64,23,233,23]

for item in line:
    if str(item).isnumeric() and item>6:
        print(item,end=" ")
