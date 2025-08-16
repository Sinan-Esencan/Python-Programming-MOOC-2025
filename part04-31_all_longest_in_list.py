# Please write a function named all_the_longest, which takes a list of strings as its argument. The function should return a new list containing the longest
# string in the original list. If more than one are equally long, the function should return all of the longest strings
def all_the_longest(my_list):
    longest = ""
    new_list = []
    for word in my_list:
        if len(word) > len(longest):
            longest = word
            new_list = [word] #listeyi sıfırlar
        elif len(word) == len(longest):
            new_list.append(word)
    return new_list

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard", "jackely"]
    result = all_the_longest(my_list)
    print(result)


#alt2 - mooc.fi: daha sade ve guzel:
def all_the_longest(names: list):
    result = []
    for name in names:
        if result == [] or len(name) > len(result[0]): #result == [] demesek hata alırız liste bosken!
            result = [name]
        elif len(name) == len(result[0]):
            result.append(name)
    return result
