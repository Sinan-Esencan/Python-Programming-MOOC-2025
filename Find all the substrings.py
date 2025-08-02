"""Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user.
You may assume the input string is at least three characters long."""

word = input("Please type in a word")
char = input("Please type in a character")

while True:

    if len(word) == 2:
        break
    
    if word[0] == char:
        if len(word) >= 3:
            print(word[0:3])

    word = word[1:]


#alt2:
word = input("Please type in a word")
char = input("Please type in a character")
index = 0

while index < len(word):
    if word[index] == char:
        if len(word[index:]) >= 3:
            print(word[index:index+3])
    index += 1
    

#alt3: mooc:
word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = 0

while index + 3 <= len(word):
    if word[index] == character:
        print(word[index:index+3])
    index += 1

#alt4: mooc'nin for loop versiyonu:
word = input("Please type in a word: ")
character = input("Please type in a character: ")

for index in range(len(word) - 2):
    if word[index] == character:
        print(word[index:index+3])
