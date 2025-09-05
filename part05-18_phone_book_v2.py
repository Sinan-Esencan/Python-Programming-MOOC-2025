# Please write an improved version of the phone book application. Each entry should now accommodate multiple phone numbers. The application should work otherwise exactly as before, 
# but this time all numbers attached to a name should be printed.

def search(persons):
    name = input("name: ")
    if name in persons:
        for number in persons[name]:
            print(number)
    else:
        print("no number")

def add(persons):
    name = input("name: ")
    number = input("number: ")
    if name not in persons:
        persons[name] = []
    persons[name].append(number)
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
