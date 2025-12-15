from string_helper import change_case, split_in_half, remove_special_characters

if __name__ == "__main__":
    my_string = "Well hello there!"
    print(change_case(my_string))
    p1, p2 = split_in_half(my_string)
    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)
