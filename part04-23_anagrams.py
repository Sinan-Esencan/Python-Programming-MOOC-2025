# Please write a function named anagrams, which takes two strings as arguments. The function returns True if the strings are anagrams of each other.
# Two words are anagrams if they contain exactly the same characters.

# Write your solution here
def anagrams(first, second):
    first = sorted(first)
    second = sorted(second)
    if first == second:
        return True
    return False

if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False

#alt2 - mooc.fi:
def anagrams(string1: str, string2: str):
    return sorted(string1) == sorted(string2)
