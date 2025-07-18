# Join function in python

lis =["John","cena","Randy","orton","sheamus","khali","jinder mahal"]

# for index,item in enumerate(lis):
#     index+=1
#     print(index,".",item)

for item in lis:
    print(item,"and",end=" ")
print("other wwe superstar.")

a = " and ".join(lis)
print(a,"and other wwe superstar.")

a = ",".join(lis)
print(a,"and other wwe superstar.")
