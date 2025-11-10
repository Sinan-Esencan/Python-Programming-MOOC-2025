# The file lottery_numbers.csv containts winning lottery numbers in the following format:
# week 1;5,7,11,13,23,24,30
# week 2;9,13,14,24,34,35,37
# ...etc...

# Each line should contain a header week x, followed by seven integer numbers which are all between 1 and 39 inclusive.
# The file has been corrupted. Lines in the file may contain the following kinds of errors (these exact lines may not be present in the file, but errors in a similar format will be):

# The week number is incorrect:
# week zzc;1,5,13,22,24,25,26
# One or more numbers are not correct:
# week 22;1,**,5,6,13,2b,34
# Too few numbers:
# week 13;4,6,17,19,24,33
# The numbers are too small or large:
# week 39;5,9,15,35,39,41,105
# The same number appears twice:
# week 41;5,12,3,35,12,14,36

# Please write a function named filter_incorrect(), which creates a file called correct_numbers.csv. The file should contain only those lines from the original file which are in the correct format.

def filter_incorrect():
    with open("lottery_numbers.csv") as wrong_lotteries_file, open("correct_numbers.csv", "w") as right_lotteries_file:
        for line in wrong_lotteries_file:
            new_line = line.strip().split(";")
            # print(new_line)
            try:
                week = new_line[0].split()
                week_number = int(week[1])
                if not (0 <= week_number <= 53):
                    continue
            except ValueError: #int() icin
                continue
            except IndexError: #week[1] yoksa
                continue

            lottery_numbers = new_line[1].split(",")
            if len(lottery_numbers) != 7:
                continue
            if len(lottery_numbers) != len(set(lottery_numbers)): #eşsiz değilse
                continue
            for number in lottery_numbers:
                # print(lottery_numbers)
                try: 
                    if not (1 <= int(number) <= 39):
                        break
                    if lottery_numbers.index(number) == 6:
                        #bkz. V2: bu kodun yazılmadıgı daha iyi alt
                        right_lotteries_file.write(line)
                except ValueError:
                    break

if __name__ == "__main__":
    filter_incorrect()


# V2: daha duzgun:
def filter_incorrect():
    with open("lottery_numbers.csv") as wrong_lotteries_file, open("correct_numbers.csv", "w") as right_lotteries_file:
        for line in wrong_lotteries_file:
            new_line = line.strip().split(";")
            try:
                week = new_line[0].split()
                week_number = int(week[1])
                if not (0 <= week_number <= 53):
                    continue
            except ValueError: #int() icin
                continue
            except IndexError: #week[1] yoksa
                continue

            lottery_numbers = new_line[1].split(",")
            if len(lottery_numbers) != 7:
                continue
            if len(lottery_numbers) != len(set(lottery_numbers)): #eşsiz değilse
                continue
            valid = True
            for number in lottery_numbers:
                try: 
                    if not (1 <= int(number) <= 39):
                        valid = False
                        break
                except ValueError:
                    valid = False
                    break

            # SADECE tüm kontroller geçtiyse yaz
            if valid:
                right_lotteries_file.write(line)


# V3 - Mooc.fi:
def filter_incorrect():
    with open("lottery_numbers.csv") as input_file, open("correct_numbers.csv", "w") as result_file:
        for row in input_file:
            parts = row.strip().split(";")
            if len(parts) != 2:
                continue
            week = parts[0].split(" ")
            error = False
            if len(week) != 2 or week[0] != "week":
                error = True
            try:
                mika = int(week[1])
            except:
                error = True
            
            number_list = parts[1].split(",")
            if len(number_list) != 7:
                error = True
            
            listed = [] #eşsizlik icin
            for item in number_list:
                try:
                    number = int(item)
                    if number < 1 or number > 39 or number in listed:
                        error = True
                    listed.append(number)
                except:
                    error = True

            if not error:
                result_file.write(row)
