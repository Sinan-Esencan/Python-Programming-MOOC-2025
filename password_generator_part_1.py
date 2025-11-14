# Please write a function which creates passwords of a desired length, consisting of lowercase characters a to z.

# An example of how the function should work:

# for i in range(10):
#     print(generate_password(8))

# Sample output:
# lttehepy
# olsxttjl
# cbjncrzo
# dwxqjdgu
# gpfdcecs
# jabyvgar
# xnbbonbl
# ktmsjyww
# ejhprmel
# rjkoacib

from random import randint
import string

def generate_password(length):
    password = ""
    for i in range(length):
        rand_int = randint(0,25)
        password += string.ascii_letters[rand_int]
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))


# V2 - mooc.fi
from random import choice
from string import ascii_lowercase

def generate_password(length: int):
    passwd = ""
    for i in range(length):
        passwd += choice(ascii_lowercase)
    return passwd