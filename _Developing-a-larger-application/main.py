#bu classı test etmek icin once bagımsız calıstırdık ve asagıdaki komutları girdik:
# t = FileHandler("phonebook.txt")
# print(t.load_file())
class FileHandler: #FILE HANDLING
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self): #read işlemi icin
    #bu fonksiyonla dosyadaki Eric;02-1234567;045-4356713 satırı {'Eric': ['02-1234567', '045-4356713']} olur
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts
                names[name] = numbers
        return names

    def save_file(self, phonebook: dict): #write islemi icin
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")



#bu classı test etmek icin once bagımsız calıstırdık ve asagıdaki komutları girdik:
# phonebook = PhoneBook()
# phonebook.add_number("Eric", "02-123456")
# print(phonebook.get_numbers("Eric"))
# print(phonebook.get_numbers("Emily"))
class PhoneBook: #LOGIC
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
        # add a new dictionary entry with an empty list for the numbers if key is not available
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None

        return self.__persons[name] #list return eder

    # bu kısım mevcut sozlugu 0 ile exit'e basınca dosyaya write etmek icin 
    def all_entries(self):
        return self.__persons


# *ilk basta PhoneBook sınıfını yarattık ve bagımsız olarak test ettik. ikinci olarak PhoneBookApplication
# sınıfını yarattık ve icinde PhoneBook sınıfını referans edip beraber test ettik. üçüncü olarak FileHandler 
# sınıfını yarattık ve bagımsız olarak test ettik; sonra PhoneBookApplication sınıfına FileHandler sınıfını
# entegre ettik. son olarak da write islemi icin FileHandler sınıfına save_file() metodunu, PhoneBook sınıfına
# all_entries() metodunu, PhoneBookApplication sınıfına da exit() metodunu ekledik (dosyayı okumak icin dosyaya
# yazarkenki gibi bagımsız test yapmadık)*
class PhoneBookApplication: #UI baglayıcı rolunde
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")

    # programı baslatır baslatmaz dosyadaki isim ve numaraları sozluge yazıyoruz:
    # load_file() dosyadaki Eric;02-1234567;045-4356713 formatını {'Eric': ['02-1234567', '045-4356713']} 
    # formatında yazarken items() fonksiyonu bu verileri key-value olarak almaya yarıyor ve sonra list 
    # valuesunu loopluyoruz
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("number unknown")
            return
        for number in numbers:
            print(number)

    # a method which gets executed as the program exits
    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())

    def execute(self):
        self.help()
        while True: #loop 0 girene kadar tekrarlanıyor ve 0 girince dosyaya kaydediliyor
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            else:
                self.help()

application = PhoneBookApplication()
application.execute()
