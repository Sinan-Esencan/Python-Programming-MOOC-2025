# Please write an improved version of your password generator. The function now takes three arguments:

#     If the second argument is True, the generated password should also contain one or more numbers.
#     If the third argument is True, the generated password should also contain one or more of these special characters: !?=+-()#.

# Despite these two additional arguments, the password should always contain at least one lowercase alphabet. You may assume the function will only be called with combinations of arguments that are possible to formulate into passwords following these rules. That is, the arguments will not specify e.g. a password of length 2 which contains both a number and a special characters, for then there would not be space for the mandatory lowercase letter.
# An example of how the function should work:

# for i in range(10):
#     print(generate_strong_password(8, True, True))

# Sample output
# 2?0n+u31
# u=m4nl94
# n#=i6r#(
# da9?zvm?
# 7h)!)g?!
# a=59x2n5
# (jr6n3b5
# 9n(4i+2!
# 32+qba#=
# n?b0a7ey

from random import choice, shuffle
from string import ascii_lowercase, digits

def generate_strong_password(length: int, number: bool, special_character: bool):
    symbols = "!?=+-()#"
# a) zorunlu karakterleri listeye koyar:
    pass_list = [choice(ascii_lowercase)] #shuffle edecegimiz icin list kullandık
    if number == True:
        pass_list.append(choice(digits))
    if special_character == True:
        pass_list.append(choice(symbols))
# b) karakter havuzunu doldurur
    char_pool = ascii_lowercase # genel karakter havuzu
    if number == True:
        char_pool += digits
    if special_character == True:
        char_pool += symbols
    # bu kod fazla uzatıyor:
    # if number == True and special_character == False:
    #     char_pool += digits
    # elif number == False and special_character == True:
    #     char_pool += symbols
    # elif number == True and special_character == True:
    #     char_pool += digits + symbols
# c) sifrede kalan boslukları havuzdan doldurur:
    for i in range(length - len(pass_list)): #alt:while len(pass_list) < length:
        pass_list.append(choice(char_pool))  
# d) tum sifreyi karıstırır
    shuffle(pass_list)
    return "".join(pass_list)
    
if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))


# V2: tavsiye edilmiyor conditional karısık oldugundan:
def generate_strong_password(length: int, number: bool, special_character: bool):
    symbols = "!?=+-()#"

    pass_list = [choice(ascii_lowercase)]
    if number == True:
        pass_list.append(choice(digits))
    if special_character == True:
        pass_list.append(choice(symbols))

    letter_number = ascii_lowercase + digits
    letter_symbol = ascii_lowercase + symbols
    all_chars = letter_number + symbols
    
    if number == False and special_character == False:
        for i in range(length - 1):
            pass_list.append(choice(ascii_lowercase))    
    elif number == True and special_character == False:
        for i in range(length - 2):
            pass_list.append(choice(letter_number))
    elif number == False and special_character == True:
        for i in range(length - 2):
            pass_list.append(choice(letter_symbol))
    elif number == True and special_character == True:
        for i in range(length - 3):
            pass_list.append(choice(all_chars))
    
    shuffle(pass_list)
    return "".join(pass_list)


# V3: *mooc.fi cozumunu yapay zeka tavsiye etmiyor cunku add_character() icindeki string concatenation'dan dolayı verimlilik dusuk. shuffle
# olmadıgından ve karakterler sadece basa veya sona eklendiginden dolayı sifreleme zayıf. okunabilirlik zayıftır cunku ana mantık while döngüsü
# ve helper fonksiyon arasında bölünmüştür*
from random import choice, randint
from string import ascii_lowercase, digits
def generate_strong_password(length: int, numbers: bool, special_characters: bool):
    special_chars = "!?=+-()#"
    passwd = choice(ascii_lowercase)
    choice_set = ascii_lowercase
    if numbers:
        passwd = add_character(passwd, digits)
        choice_set += digits
    if special_characters:
        passwd = add_character(passwd, special_chars)
        choice_set += special_chars
    while (len(passwd) < length):
        passwd = add_character(passwd, choice_set)
    return passwd
def add_character(passwd: str, characters):
    character = choice(characters)
    if randint(1,2) == 1:
        return character + passwd
    else:
        return passwd + character
