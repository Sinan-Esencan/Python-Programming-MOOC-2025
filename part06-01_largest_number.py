# Please write a function named largest, which reads the file and returns the largest number in the file.
# Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.

def largest():
    with open("numbers.txt") as new_file:
        start = True #bu kısım onemli!
        largest_number = 0
        # alt: starts with negative infinity: largest_number = float('-inf')
        for line in new_file:
            number = int(line.replace("\n", ""))
            if start or largest_number < number:
                largest_number = number
                start = False
        return largest_number

if __name__ == "__main__":
    print(largest())


# alt: daha guzel bence:
def largest():
    with open("numbers.txt") as new_file:
        largest_number = float('-inf') #starts with negative infinity: 
        for line in new_file:
            number = int(line.strip()) #Converts to integer and removes whitespace
            if largest_number < number:
                largest_number = number
        return largest_number
