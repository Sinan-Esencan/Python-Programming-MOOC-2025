# Please write a function named list_sum which takes two lists of integers as arguments. The function returns a new list which contains the sums of the items at
# each index in the two original lists. You may assume both lists have the same number of items.

def list_sum(list1, list2):
    new_list = []
    for a in range(len(list1)):
        new_list.append(list1[a]+list2[a])
    return new_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]


#alt2 mooc: using zip function which creates new list by combining items in two or more lists:
def list_sum(list1, list2):
    new_list = []
    for item1, item2 in zip(list1, list2):
        new_list.append(item1 + item2)
    return new_list
