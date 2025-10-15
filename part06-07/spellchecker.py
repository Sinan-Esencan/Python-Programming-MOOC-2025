# Please write a program which asks the user to type in some text. Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them. Please see the two examples below:
# Sample output

# Write text: We use ptython to make a spell checker
# We use *ptython* to make a spell checker

# Write text: This is acually a good and usefull program
# This is *acually* good and *usefull* program

# The case of the letters should be irrelevant to the functioning of your program.
# The exercise template includes the file wordlist.txt, which contains all the words the spell checker should accept as correct.

correct_words_list = []
with open("wordlist.txt") as read_file:
    for line in read_file:
        word = line.strip()
        correct_words_list.append(word)
# print(correct_words_list)

text = input("Write text: ")
parts = text.split()
# print(parts)
result = ""
for word in parts:
    if word.lower() in correct_words_list:
        result += word + " "
    else:
        result += f"*{word}* "
print(result)


# alt2 - mooc.fi: bence benimki dogru cunku split(' ') yerine split() kullanılmalı
def wordlist():
    words = []
    with open("wordlist.txt") as file:
        for row in file:
            words.append(row.strip())
    return words

words = wordlist()
sentence = input("Write text: ")

for word in sentence.split(' '):
    if word.lower() in words:
        print(word + " ", end="")
    else:
        print("*" + word + "* ", end="")
print()

# write your solution here
