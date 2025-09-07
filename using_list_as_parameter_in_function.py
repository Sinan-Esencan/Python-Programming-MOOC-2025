def augment_all(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(item + 10)    
    my_list[:] = new_list
   #  yukarıdaki kod asagıdakiler gibi degisirse ne print edilecegini bil:
   #  my_list = []
   #  my_list = new_list[:]
   #  my_list = new_list
   #  new_list = my_list
   #  new_list = my_list[:]
    my_list.append(2)
    print("my_list inside function", my_list)
    print("new_list inside function", new_list)

numbers = [1, 2, 3]
print("in the beginning:", numbers)
augment_all(numbers)
print("after the function is executed:", numbers)
