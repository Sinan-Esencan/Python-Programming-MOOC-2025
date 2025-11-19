# In this exercise you will validate Finnish Personal Identity Codes (PIC).

# Please write a function named is_it_valid(pic: str), which returns True or False based on whether the PIC given as an argument is valid or not. Finnish PICs follow the format ddmmyyXyyyz, where ddmmyy contains the date of birth, X is the marker for century, yyy is the personal identifier and z is a control character.

# The program should check the validity by these three criteria:

#     The first half of the code is a valid, existing date in the format ddmmyy.
#     The century marker is either + (1800s), - (1900s) or A (2000s).
#     The control character is valid.

# The control character is calculated by taking the nine-digit number created by the date of birth and the personal identifier, dividing this by 31, and selecting the character at the index specified by the remainder from the string 0123456789ABCDEFHJKLMNPRSTUVWXY. For example, if the remainder was 12, the control character would be C.

# More examples and explanations of the uses of the PIC are available at the Digital and Population Data Services Agency.

# NB! Please make sure you do not share your own PIC, for example in the code you use for testing or through the course support channels.

# Here are some valid PICs you can use for testing:

#     230827-906F
#     120488+246L
#     310823A9877

from datetime import datetime

def is_it_valid(pic: str): #Personal Identity Codes (PIC)

    if len(pic) != 11:
        return False #fail-fast (early-exit) ile erken cıkılmalı

# rakam pass edilmemişse hata vermeyi önler
    numbers = pic[:6]+pic[7:10]
    for x in numbers:
        if x not in "0123456789":
            return False

# validation 2
    century_marker = pic[6]
    if century_marker not in "-+A":
        return False

# validation 1
    if century_marker == "-":
        year = int("19"+pic[4:6])
    elif century_marker == "+":
        year = int("18"+pic[4:6])
    elif century_marker == "A":
        year = int("20"+pic[4:6])
        
    month = int(pic[2:4])
    day = int(pic[:2])

    try:
        date_obj = datetime(year, month, day)
        # date = date_obj.strftime("%d%m%y")
#strftime (string format time), date'i string'e çevirir ancak burada gereksiz
    except ValueError:
        return False

# validation 3
    validator = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    combo = int(numbers) #combo is made of date of birth and the personal identifier
    if pic[-1] != validator[combo%31]:
        return False
    return True


if __name__ == "__main__":
    print(is_it_valid("230827-90446F")) #- is marker, and F is control character
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))


# ilk başta 3. validasyonu yanlıs anlamıstım:
    # validator = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    # total = 0
    # combo = pic[0:6]+pic[7:10]
    # for i in combo:
    #     total += int(i)
    # if pic[-1] != validator[total%31]:
    #     valid = False
