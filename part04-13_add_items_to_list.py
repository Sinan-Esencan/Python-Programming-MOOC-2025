"""Please write a program which first asks the user for the number of items to be added. Then the program should ask for the given number
of values, one by one, and add them to a list in the order they were typed in. Finally, the list is printed out"""

items = int(input("How many items: "))
list = []
for i in range(items):
    list.append(int(input(f"Item {i+1}: ")))
print(list)

#alt2: MOOC alternatifi:
numbers = int(input("How many items: "))
list = []
while len(list) < numbers:
    number = int(input(f"Item {len(list) + 1}: "))
    list.append(number)
print(list)
