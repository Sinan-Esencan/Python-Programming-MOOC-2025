"""Please write a program which asks the user to input a string. The program then prints out different messages if the string contains any of the vowels a, e or o.
You may assume the input will be in lowercase entirely. Have a look at the examples below."""

string = input("Please type in a string: ")
to_search = "aeo"
i = 0

while i < len(to_search):
    if to_search[i] in string:
        print(f"{to_search[i]} found")
    else:
        print(f"{to_search[i]} not found")
    i += 1
