#Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest

#V1: benim:
string = input("Please type in a string: ")
i = 1
while i <= len(string):
    print(string[len(string)-i:len(string)])
    i+=1


#V2: mooc:
string = input("Please type in a string: ")
start = len(string) - 1
while start >= 0:
    print(string[start:])
    start -= 1
