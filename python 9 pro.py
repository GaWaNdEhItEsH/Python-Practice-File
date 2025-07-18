#list and list function
gro=["harpic","vimbar","deodrant","powder","soap","toothpast"]
#print(type(gro))
"""print(gro[4])
print(gro[2])
print(gro[0:4])
#print(len(gro))
print(gro[::])
print(gro[0::2])
print(gro[0:6])
print(gro[3:7:2])
print(gro[::-1])"""

number = [20,70,90,110,30,40,50]
#print(number)
print(len(number))
print(number[5])
# n1 = number
# print(n1)
# n1.sort()
# print(n1)

#list function
print(number)
number.sort()
print(number)

number.reverse()
print(number)
#print(number[9]) it gives an error
print(number[::])
print(number[2:5])
print(number[0:7:2])
print(number[::-1])
print(number)
print(number[-6:-1:2])
print(number[len(number)-6:len(number)-1:2])  #lenght of number is 7
print(number[1:6:2])
number.sort()
print(number)
print(max(number))
print(min(number))

number.append(110)    # add number at the end of the list
number.append(500)
number.append(230)
print(number)

number.insert(2,80)
print(number)
number[5]=400
print(number)

number.pop()   # delete number at the end of the list
print(number)
number.pop(1)
print(number)

number.remove(110)
print(number)

#tupple
tp=(5,6,7,8,9,10,12,15,14,6,8,9)
print(tp)
print(type(tp))
print(len(tp))
print(tp[5])
print(tp[0:7:2])
print(tp[::-1])
print(tp.count(9))

a = (1,5,3,2)
b = (5,3,4,8)
a,b=b,a
print(a,b)


tup=(1,)
print(type(tup),tup)