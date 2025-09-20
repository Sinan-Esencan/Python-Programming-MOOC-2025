# The file matrix.txt contains a matrix in the format specified in the example below:

# 1,0,2,8,2,1,3,2,5,2,2,2
# 9,2,4,5,2,4,2,4,1,10,4,2
# ...etc...

# Please write two functions, named matrix_sum and matrix_max. Both go through the matrix in the file, and then return the sum of the elements or the element
# with the greatest value, as the names of the functions imply. Please also write the function row_sums, which returns a list containing the sum of each row in
# the matrix. For example, calling row_sums when the matrix in the file is defined as

# 1,2,3
# 2,3,4

# The function should return the list [6, 9].
# Hint: you can also include other helper functions in your program. It is very worthwhile to spend a moment considering which functionalities are shared by the
# three functions you are asked to write. Notice that the three functions named above do not take any arguments, but any helper functions you write may take arguments.
# The file you are working with is always named matrix.txt.

def iterator():
    with open("matrix.txt") as new_file:
        new_list = [] #list of list
        for line in new_file:
            line = line.replace("\n", "") #alt: line.strip()
            parts = line.split(",") #list of strings
            int_list = [int(x) for x in parts] #int'e çevirir sublistleri
            new_list.append(int_list)
        return new_list

def my_sum():
    new_list = iterator()
    sum_list = []
    for row in new_list:
        sum_list.append(sum(row))
    return sum_list    

def matrix_sum():
    return sum(my_sum())

def matrix_max():
    new_list = iterator()
    start = True
    max_num = 0
    for row in new_list:
        if start or max(row) > max_num:
            max_num = max(row)
            start = False
    return max_num

def row_sums():
    return my_sum()

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())


# alt1 - mooc.fi: benden daha iyi çözümmüş:
def read_matrix():
    with open("matrix.txt") as file:
        m = [] #list of lists (multidimensional list/2d array)
        for row in file:
            mrow = []
            items = row.split(",")
            for item in items:
                mrow.append(int(item)) #int demek strip() gorevi de goruyor
            m.append(mrow)
    return m

def combine(matrix: list):
    mlist = [] #sublistler bu boş liste concatenate ediliyor
    for row in matrix:
        mlist += row
    return mlist

def matrix_sum():
    mlist = combine(read_matrix())
    return sum(mlist)

def matrix_max():
    mlist = combine(read_matrix())
    return max(mlist)

def row_sums():
    matrix = read_matrix()
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())


# alt2 - qwen'in benim cozumume onerdigi refactoring:
def iterator():
    with open("matrix.txt") as new_file:
        new_list = []
        for line in new_file:
            parts = line.strip().split(",")
            int_list = [int(x) for x in parts]
            new_list.append(int_list)
        return new_list

def my_sum():
    new_list = iterator()
    return [sum(row) for row in new_list]

def matrix_sum():
    return sum(my_sum())

def matrix_max():
    new_list = iterator()
    max_num = None
    for row in new_list:
        row_max = max(row)
        if max_num is None or row_max > max_num:
            max_num = row_max
    return max_num

def row_sums():
    return my_sum()
