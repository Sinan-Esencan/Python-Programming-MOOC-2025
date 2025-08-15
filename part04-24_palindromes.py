# Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome.
# Palindromes are words which are spelled exactly the same backwards and forwards.

def palindromes(word):
    reverse = ""
    for i in word:
        reverse = i + reverse
    return word == reverse

while True:
    word = input("Please type in a palindrome: ")
    pal = palindromes(word)
    if pal == True:
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")


#V2 mooc: palindromes fonksiyonu farklı bicimde uygulanmıs:
    def palindromes(word: str):
        for i in range(len(word)//2):
            if word[i] != word[len(word)-i-1]:
                return False
        return True
