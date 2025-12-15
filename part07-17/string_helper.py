def change_case(orig_string: str):
    reversed_str = ""
    for char in orig_string:
        if char.isupper():
            reversed_str += char.lower()
        else:
            reversed_str += char.upper()
    return reversed_str

def split_in_half(orig_string: str):
    str1 = ""
    str2 = ""
    first_half = len(orig_string) // 2
    for i, char in enumerate(orig_string):
        if i < first_half:
            str1 += char
        else:
            str2 += char
    return str1, str2

def remove_special_characters(orig_string: str):
    str = ""
    for char in orig_string:
        if char.islower() or char.isupper() or char.isdigit() or char.isspace():
            str += char
        else: #bu else blok gereksiz aslında
            continue
    return str


# alt - mooc.fi: son 2 fonksiyon icin daha guzel yapılmıs:
from string import ascii_letters, digits

def change_case(orig_string: str):
    new_string = ""
    for character in orig_string:
        if character.isupper():
            new_string += character.lower()
        elif character.islower():
            new_string += character.upper()
        else:
            new_string += character
    return new_string

def split_in_half(orig_string: str): #list slicing
    return orig_string[:len(orig_string) // 2], orig_string[len(orig_string) // 2:]

def remove_special_characters(orig_string: str):
    allowed = ascii_letters + digits + ' '
    # *aslında string yerine set() kullanılması daha hızlı yapar:*
    # allowed = set(ascii_letters + digits + ' ')
    new_string = ""
    for character in orig_string:
        if character in allowed:
            new_string += character
    return new_string
