#Please write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line

#V1: benimki:
sentence = input("Please type in a sentence: ")
arr = sentence.split()

i = 0
while i < len(arr):
    print(arr[i][0])
    i += 1
"""while loop yerine for loop kullansak daha bile iyi:
for word in arr:
    print(word[0])"""

#V2: mooc:
sentence = input("Please type in a sentence: ")
# Add a space at the start, to make handling sentence easier
sentence = " " + sentence
# Searching for indexes which are preceded by spaces
index = 1
while index < len(sentence):
    if sentence[index-1] == " " and sentence[index] != " ":
        print(sentence[index])
    index += 1
