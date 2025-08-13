# Please write a program which asks the user to choose between addition and removal. Depending on the choice, the program adds an item to or removes an item from the end of a list.
# The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.
my_list = []
i = 1
while True:
    print("The list is now", my_list)
    command = input("a(d)d, (r)emove or e(x)it:")
    if command == "d":
        my_list.append(i)
        i += 1
    elif command == "r" and my_list:
        my_list.pop()
        i -= 1
    elif command == "x":
        print("Bye!")
        break


#alt2: mooc:
my_list = []
while True:
    print(f"The list is now {my_list}")
    selection = input("a(d)d, (r)emove or e(x)it:")
    if selection == "d":
        item = len(my_list) + 1
        my_list.append(item)
    elif selection == "r" and my_list:
        my_list.pop()
    elif selection == "x":
        break
print("Bye!")
