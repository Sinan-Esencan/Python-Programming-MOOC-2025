# Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.
# For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.

def longest_series_of_neighbours(my_list):
    new_list = [my_list[0]]
    serie_length = []
    for element in my_list:
        if abs(element - new_list[-1]) == 1:
            new_list.append(element)
        else:
            new_list = [element]
        serie_length.append(len(new_list))
    return max(serie_length)

if __name__ == "__main__":
    my_list = [1, 2, 5, 4, 3, 4]
    print(longest_series_of_neighbours(my_list))
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))


#V2 MOOC:
def longest_series_of_neighbours(my_list:list):
    longest=1
    result=1
    for i in range(1,len(my_list)):
        if abs(my_list[i-1]-my_list[i])==1:
            result+=1
        else:
            result=1
        longest=max(longest,result)
    return longest

#ilk hatalı denemelerim:
#1) burada problem new_list listesi sıfırlandıktan sonra onceki seri daha uzun olursa: 
# my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
def longest_series_of_neighbours(my_list):
    new_list = [my_list[0]]
    for element in my_list:
        if abs(element - new_list[-1]) == 1:
            new_list.append(element)
        else:
            new_list = [element]
    return len(new_list)
    
  
#2) burada problem listenin son serisi en uzun olursa serie_length listesine kaydedilmemesi: 
# my_list = [1, 2, 5, 4, 3, 4] 
def longest_series_of_neighbours(my_list):
    new_list = [my_list[0]]
    serie_length = []
    for element in my_list:
        if abs(element - new_list[-1]) == 1:
            new_list.append(element)
        else:
            serie_length.append(len(new_list))
            new_list = [element]
    return max(serie_length)
