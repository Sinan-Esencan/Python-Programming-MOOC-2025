# Please write a function named histogram, which takes a string as its argument. The function should print out a histogram representing the number of times each letter occurs in the string. 
# Each occurrence of a letter should be represented by a star on the specific line for that letter.

def histogram(string: str):
    letters = {}
    for i in string:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1

    for letter in letters:
        print(letter, f"{letters[letter]*'*'}") 
    
if __name__ == "__main__":
    histogram("abba")

# alt2 - mooc.fi:
def histogram(my_str: str):
    characters = {}
    for character in my_str:
        if not character in characters:
            characters[character] = 0
        characters[character] += 1

    for character, lkm in characters.items():
        stars = "*"*lkm
        print(f"{character} {stars}")
