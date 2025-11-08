import string

def separate_characters(my_string: str):
    str1 = ""
    str2 = ""
    str3 = ""
    for character in my_string:
        if character in string.ascii_letters:
            # print(string.ascii_letters)
            str1 += character
        elif character in string.punctuation:
            str2 += character
        else: #digit and whitespace
            str3 += character
    my_tuple = (str1, str2, str3)
    return my_tuple

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
