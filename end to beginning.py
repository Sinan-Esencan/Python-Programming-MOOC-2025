str = input("Please type in a string: ")
i = len(str)-1
while i >= 0:
    print(str[i])
    i -= 1

""" V2:
input_string = input("Please type in a string: ")
index = -1
while index >= -len(input_string):
    print(input_string[index])
    index -= 1
"""
