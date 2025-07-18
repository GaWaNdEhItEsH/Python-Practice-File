s_s = set()
#s_s = set([4,8,6,7,2])
#print(type(s_s))
s_s.add(1)
print(s_s)
s_s.add(10)
print(s_s)

i=0
while(i<45):
      print(i,end=" ")
      i=i+1

print()

print(s_s)

i=0
while(i<45):
     i=i+1
     s_s.add(i-1)

print(s_s)

# s1= s_s.union({6,8,7,3})
# print(s1)
# print(s_s)
#
# s1.add(10)
# print(s1)
#
# s2=s_s.intersection(s1)
# print(s2)
#
# s3=set({8,6})
# print(s_s.isdisjoint(s3))
#
# s_s.remove(10)
# print(s_s)