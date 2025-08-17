# Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items 
# on the original list reversed. Also the order of items should be reversed on the new list.

def everything_reversed(my_list):
    new_list = []
    for words in my_list:
        new_list.insert(0, words[::-1])
    return new_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)


#alt2 - mooc: once kelimeleri sonra da liste elemanlarını reverse etmis:
def everything_reversed(my_list: list):
    new_list = []
    for my_string in my_list:
        new_list.append(my_string[::-1])
    return new_list[::-1]
