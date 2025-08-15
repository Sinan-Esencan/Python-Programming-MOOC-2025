# Please write a function named shortest, which takes a list of strings as its argument. The function returns whichever of the strings is the shortest.
# If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests). You may assume there will be no empty strings in the list.

def shortest(my_list):
    short = my_list[0]
    for i in my_list:
        if len(i) < len(short):
            short = i
    return short

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)


# alt2 - mooc.fi: 'if result == "" or' denmesi guzel bir mantık olmus
def shortest(names: list):
    result = ""
    for nimi in names:
        if result == "" or len(nimi) < len(result):
            result = nimi
    return result
