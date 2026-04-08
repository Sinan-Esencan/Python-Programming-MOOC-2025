# Please write a function named distinct_numbers, which takes a list of integers as its argument. The function returns a new list 
# containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.

def distinct_numbers(list_of_numbers:list):
    distinct_list = []
    for num in list_of_numbers:
        if num in distinct_list:
            continue
        distinct_list.append(num)            
    distinct_list.sort()
    return distinct_list

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]

# alt - mooc.fi:
def distinct_numbers(my_list: list):
    results = []
    for item in my_list:
        if item not in results:
            results.append(item)
 
    results.sort()
    return results
