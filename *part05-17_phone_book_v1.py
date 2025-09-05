# Please write a phone book application. Each name can be attached to a single number only. If a new entry with the same name is added, the number attached to the old entry is replaced with the new number.

phone_book = {}
while (True):
    command = int(input("command (1 search, 2 add, 3 quit):"))
    if command == 3:
        print("quitting...")
        break
    elif command == 2:
        name = input("name: ")
        number = input("number: ") #int() kullanılmamalı
        phone_book[name] = number
        print("ok!")
    elif command == 1:
        name = input("name: ")
        if name in phone_book:
            print(phone_book[name])
        else:
            print("no number")


#V2 - mooc.fi:
def search(persons):
    name = input("name: ")
    if name in persons:
        print(persons[name])
    else:
        print("no number")

def add(persons):
    name = input("name: ")
    number = input("number: ")
    persons[name] = number
    print("ok!")

def main():
    persons = {}
    while True:
        cmd = input("command (1 search, 2 add, 3 quit): ")
        if cmd == "1":
            search(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            break
    print("quitting...")

main()
# Write your solution here
