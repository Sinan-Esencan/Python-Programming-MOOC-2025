#Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be the same as the original but with all vowels removed.

def no_vowels(str):
    new_str = ""
    vowels = "aeiou"
    for letter in str.lower(): #lower() sayesinde buyuk harfe de duyarlı
        if letter not in vowels:
            new_str += letter
    return new_str

if __name__ == "__main__":
    my_string = "this Is an example"
    print(no_vowels(my_string))
