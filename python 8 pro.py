# String Slicing
mac="Hitesh is a good boy"
#print(mac)
#print(mac[::])  Here it take 0 in first and 20 in secound (i.e total length) and increase in 1 at third
#print(len(mac))
print(mac[8])
print(mac[0:6])
print(mac[0:20])
print(mac[0:10])
#print(mac[30]) error
print(mac[0:30])
print(mac[0:15:2])
print(mac[0:15:3])
print(mac[0:])
print(mac[:6])
print(mac[2:6])
print(mac[0:20:1])
print(mac[2:15:2])
print(mac[::500])
#print(mac[-5:0]) this line not print
print(mac[-12:-2])
print(mac[-12:])
print(mac[::-1])
#print(mac[::-2])
#print(mac[-20:-4:])
print(mac[0:16:1])
#print(mac[3:16])
#book= mac[3:16:]
#print(book[::-1])

#function
print(mac.isalnum())
mac1="Hiteshisagoodboy"
print(mac1.isalnum())
mac2=mac1.isalnum()
print(type(mac2))

print(mac.isalpha())
print(mac.endswith("boy"))
print(mac.endswith("boys"))
print(mac.count("s"))
print(mac.count("o"))
print(mac.count("is"))
print(mac.capitalize())
print(mac.find("is"))
print(mac.lower())
print(mac.upper())
print(mac.replace("is","are"))
print(mac.capitalize())