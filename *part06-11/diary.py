# Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt. When the program is executed, it should first read any entries already in the file.

# The program should work as follows:

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: Today I ate porridge
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: I went to the sauna in the evening
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!


while (True):
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as my_file:
            my_file.write("\n" + entry)
            print("Diary saved")
    elif function == 2:
        with open("diary.txt") as my_file:
            for line in my_file:
                print(line, end="")
            print("") #son satırı yazdıktan sonra bos satıra geçmek icin
    elif function == 0:
        print("Bye now!")
        break


# alt2 - mooc.fi: daha iyi cozum cunku her loopta dosyayı açmak zorunda kalmıyoruz
# Read the markings first
try:
    with open("diary.txt") as file:
        content = []
        for row in file:
            content.append(row.replace("\n","")) #alt: row.strip()
except FileNotFoundError:
        content = []
        print("No entries yet")

# alt: *using list comprehension:*
# try:
#     with open("diary.txt") as file:
#         content = [row.replace("\n","") for row in file]
# except FileNotFoundError:
#         content = []
#         print("No entries yet")

# Open file for appending
with open("diary.txt", "a") as file:
#*with open sonrası while True loop kullanıldıgı icin dosyaya yazdıgımız veri bellek tamponunda bekler
#ve ne zamanki 0'a basıp programdan çıkarız o zaman veri veya veriler dosyaya gerçekten yazılır. bunu onlemek
# icin flush() kullanılabilir*
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        function = input("Function: ")
        if function == "1":
            entry = input("Diary entry: ")
            file.write(entry + "\n") #diary.txt dosyasında son satır bos bırakıldıgı icin \n sorunsuz
            # file.flush() #opsiyonel: looptan 0'la cıkmadan hemen yazdırmak icin dosyaya
            content.append(entry)
            print("Diary saved")
        elif function == "2":
            print("Entries:")
            for entry in content:
                print(entry)
        elif function == "0":
            print("Bye now!")
            break
