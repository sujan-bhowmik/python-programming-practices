# Truthly,Falsely

# #part 1
# if 1: #if true
#     print("Hello!")
#     print(bool(1))
#     print(bool("Python!"))
# else: #if false
#     print("Bye Bye")
#     print(bool(0))
#     print(bool())

# part2

# name = input("Value:")

# if name:
#     print("hello!")
#     print(bool("None"))
# else:
#     print("Bye Bye")
#     print(bool([]))
#     print(bool(None))
#     # print(bool(NULL))--Wrong type
#     # print(bool(YES)) --Wrong type
#     # print(bool(NONE)) --Wrong type
#     # print(bool(Blank)) --Wrong type


# part3

name = input("Enter name:")

if name == None:  # eta kokhonoi create kora possible naa
    print("Kichhu Nei!")
elif name != None:
    print(name)
elif name == "":
    print("Hello Enter")
else:
    print("Error")  # eta kokhonoi create kora possible naa
