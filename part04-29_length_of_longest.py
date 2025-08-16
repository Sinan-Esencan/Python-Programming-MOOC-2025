#Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns the length of the longest string

def length_of_longest(my_list):
    longest = 0
    for i in my_list:
        if len(i) > longest:
            longest = len(i)
    return longest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)


#V2: eger indeksi return etseydik:
def length_of_longest(my_list):
    longest = ""
    for i in my_list:
        if len(i) > len(longest):
            longest = i
    return longest

#V3: hem indeksi hem de kelimeyi return etmek:
def length_of_longest(my_list):
    longest = 0
    longest_word = ""
    for i in my_list:
        if len(i) > len(longest_word):
            longest = len(i)
            longest_word = i
    return [longest, longest_word]
