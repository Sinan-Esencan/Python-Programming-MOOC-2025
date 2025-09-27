# The file solutions.csv contains some solutions to mathematics problems:
# Arto;2+5;7
# Pekka;3-2;1
# Erkki;9+3;11
# Arto;8-3;4
# Pekka;5+5;10
# ...jne...

# As you can see above, on each line the format is name_of_student;problem;result. All the operations are either addition or subtraction, and each has exactly two operands.

# Please write a function named filter_solutions() which
#     Reads the contents of the file solutions.csv
#     writes those lines which have a correct result into the file correct.csv
#     writes those lines which have an incorrect result into the file incorrect.csv

# Using the example above, the file correct.csv would contain the lines
# Arto;2+5;7
# Pekka;3-2;1
# Pekka;5+5;10

# The other two would be in the file incorrect.csv.


def filter_solutions():
    true_calculations = []
    false_calculations = []
    # once dosyayı okuruz ve listleri doldururuz
    with open("solutions.csv") as my_file:
        for line in my_file:
            line = line.strip().split(";")
            if eval(line[1]) == int(line[2]):
                true_calculations.append(line)
            else:
                false_calculations.append(line)

# sonra yazma modunda bu listleri looplarız ve dosyalara yazdırırız
    with open("correct.csv", "w") as my_file:
        for calculation in true_calculations:
            print(calculation)
            output = ""
            for part in calculation:
                output += part + ";" #alt: output += f"{part};"
            output = output[0:-1] #son noktalı virgule kadar alır
            my_file.write(f"{output} \n")
# eger calculation listesi cok uzun olsaydı yukarıdaki gibi islem yapardık, kısaysa da asagıdaki gibi
    with open("incorrect.csv", "w") as my_file:
        for calculation in false_calculations:
            my_file.write(f"{calculation[0]};{calculation[1]};{calculation[2]} \n")

if __name__ == "__main__":
    filter_solutions()


# alt2 - mooc.fi: daha hızlı calısan ve daha kısa kod:
def filter_solutions():
    # Open all lines
    with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for row in source:
            pieces = row.split(";")
            calculation = pieces[1]
            result = pieces[2]
            if "+" in calculation:
                operands = calculation.split("+") #alt: a, b = calculation.split("+")
                correct = int(operands[0]) + int(operands[1]) == int(result)
                #int() ve float() otomatik olarak bastaki ve sondaki boslukları siler
            else:
                operands = calculation.split("-")
                correct = int(operands[0]) - int(operands[1]) == int(result)

            # Write to file
            if correct:
                correct_file.write(row)
#correct_file.write(row) veya incorrect_file.write(row) satırlarının sonuna '\n' eklemesine gerek olmamasının nedeni,
# row değişkeninin zaten orijinal satır sonu karakterini (\n) içeriyor olmasıdır. 
            else:
                incorrect_file.write(row)


# alt3: mooc.fi'yi kısalttım:
def filter_solutions():
    # Open all lines
    with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for row in source:
            # Split into pieces
            pieces = row.split(";")
            calculation = pieces[1]
            result = pieces[2]
            # Addition or subtraction?
            correct = eval(calculation) == int(result)
            # Write to file
            if correct:
                correct_file.write(row)
            else:
                incorrect_file.write(row)
