#Please write a function named double_items(numbers: list), which takes a list of integers as its argument.
#The function should return a new list, which contains all values from the original list doubled. The function should not change the original list.

#using list comprehension:
def double_items(numbers: list):
    new_list = [x * 2 for x in numbers]
#numbers = [x * 2 for x in numbers] desek de main'deki numbers list degismezdi cunku yeni liste yaratılmıs olurdu
    return new_list

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)

#v2:
def double_items(numbers: list):
    new_list = []
    for item in numbers:
        new_list.append(item)
    #*alt: new_list = numbers[:]*

    for i in range(len(new_list)):
        new_list[i] = new_list[i]*2

    return new_list

#V3:
def double_items(numbers: list):
    new_list = []
    for no in numbers:
        new_list.append(no*2)
    return new_list
