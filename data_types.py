# # String data type

# # literal assignment
# first = "Ryland"
# last = "Lewer"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# # constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# # Concatenation
# fullname = first + " " + last
# print(fullname)

# multiline = '''
# hey how you doing

# feeling ok?

#         love ry'''

# print(multiline)

# build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))