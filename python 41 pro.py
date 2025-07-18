# *args and **kwargs

# def funarg(*args):
#     print(args)
#     print(type(args))     # list store as tupple in args
# har = ["Pinky","Chinky","Money","Honey","Banny"]
# funarg(*har)

# def funargs(*args):
#     for item in args:
#         print(item,end=" ")
# har = ["Pinky","Chinky","Money","Honey","Banny"]
# funargs(*har)

# def funargs(normal,*args):        # there is a thumb rule of sequence (normal arrgument,*args,**kwargs)
#     print(normal)
#     for item in args:
#         print(item,end=" ")
# har = ["Pinky","Chinky","Money","Honey","Banny"]
# sentence = "Hello people"
# funargs(sentence,*har)

# def funargs(normal,*args,**kwargs):
#     print(normal)
#     for item in args:
#         print(item,end=" ")
# har = ["Pinky","Chinky","Money","Honey","Banny","Chini"]
# sentence = "Hello people"
# funargs(sentence,*har)

def funargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item,end=" ")
    print()
    for key,values in kwargs.items():
        print(f"{key} is a {values}")
har = ["Pinky","Chinky","Money","Honey","Banny","Chini"]
sentence = "Hello people"
kw = {"Rohan":"Monitor","Harry":"Programmer","Hathim":"Co ordinator","Skillf":"Cook"}
funargs(sentence,*har,**kw)