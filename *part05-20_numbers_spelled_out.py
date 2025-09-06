# Please write a function named dict_of_numbers(), which returns a new dictionary. The dictionary should have the numbers from 0 to 99 as its keys.
# The value attached to each key should be the number spelled out in words. Please have a look at the example below

def dict_of_numbers():
    small_numbers = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    numbers = {}
    for i in range(100):
        if i < 20: #alt: if i in small_numbers
            numbers[i] = small_numbers[i]
        elif 20 <= i < 100:
            ones_place = i % 10
            tens_place = i // 10
            if ones_place == 0:
                numbers[i] = tens[tens_place]
            else:
                numbers[i] = f"{tens[tens_place]}-{small_numbers[ones_place]}"
    return numbers 


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])


#V2: dictionary yerine list kullanılırsa:
def dict_of_numbers():
    numbers_dict = {}
    
    # 0-19 arası özel sayılar
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", 
            "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    # Onluk sayılar (ilk iki eleman boş - 0 ve 10 için)
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", 
            "seventy", "eighty", "ninety"]
    
    for i in range(100):
        if i < 20:
            # 0-19 arası doğrudan ones listesinden
            numbers_dict[i] = ones[i]
        else:
            # Sayıyı onlar ve birler basamağına ayır
            ten_digit = i // 10
            one_digit = i % 10
            
            if one_digit == 0:
                # Onluk sayılar (20, 30, 40, ...)
                numbers_dict[i] = tens[ten_digit]
            else:
                # Ara sayılar (21, 32, 45, ...)
                numbers_dict[i] = tens[ten_digit] + "-" + ones[one_digit]
    
    return numbers_dict
