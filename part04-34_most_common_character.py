# Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences
# within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.

def most_common_character(str):
    most_counted = 0
    most_counted_letter = ""
    for letter in str:
        counted = str.count(letter)
        if counted > most_counted:
            most_counted = counted
            most_counted_letter = letter
    return most_counted_letter

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))


#V2: daha sade ve iyi
def most_common_character(str):
    most_counted_letter = str[0]
    for letter in str:
        counted = str.count(letter)
        if counted > str.count(most_counted_letter):
            most_counted_letter = letter
    return most_counted_letter
