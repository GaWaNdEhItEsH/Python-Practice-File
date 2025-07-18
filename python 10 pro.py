# Dictionary and its function

d1={}
print(type(d1))

d2={"Hitesh":"Biryani","Rohan":"Burger","Gaurav":"Pavwada","Hridaan":"Chocolet"}
print(d2)

print(d2["Hridaan"])
print(d2["Hitesh"])

d3={"Hitesh":"Biryani","Rohan":"Burger","Gaurav":"Pavwada","Hridaan":"Chocolet",
    "Shital": {"BK":"Idaly","LU":"Chiken","DI":"Meat"}}
print(d3["Shital"]["BK"])

d3["Praful"]="Jungfood"   #Add
print(d3)
del d3["Shital"]         #Delete
print(d3)
# d4=d3
# del d4["Gaurav"]
# print(d3)

#Function

d4=d3.copy()
del d4["Gaurav"]
print(d4)         # Gaurav delete from d4
print(d3)         # After copy Gaurav still remains

print(d3.get("Rohan"))
d3.update({"Nakul":"Beer"})
print(d3)
d3["Nakul"]="Wine"
#d3["Nakul"]="Beer"
print(d3)
print(d3.keys())
print(d3.items())