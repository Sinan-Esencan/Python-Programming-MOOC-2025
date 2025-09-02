# This is the very last sudoku task. This time we will create a slightly different version of the function for adding new numbers to the grid.
# The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid,
# two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should
# return a copy of the original grid with the new digit added in the correct location. The function should not change the original grid received as a parameter.
# The print_sudoku function from the previous exercise could be useful for testing, and it is used in the example below:

def print_sudoku(sudoku: list):
    r = 0
    for row in sudoku:
        c = 0
        for character in row:
            c += 1
            if character == 0:
                character = "_"
            m = f"{character} "
            if c%3 == 0 and c < 7:
                m += " "
            print(m, end="")
        print()
        r += 1
        if r%3 == 0 and r < 7:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
#sudoku 2 boyutlu oldugundan sığ kopya (shallow copy) yerine derin kopya (deep copy) yapmalıyız
    sudoku_copy = [row[:] for row in sudoku]  # row[:] ile her satırın ayrıca kopyasını al
#bu bir list comprehension ifadesidir    
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)


#V2 - mooc.fi:
def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_list = []
    for row in sudoku:
        new_list.append(row[:])
    new_list[row_no][column_no] = number
    return new_list

#V3:    
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_list = []
    for row in sudoku:
        new_row = []  # Her satır için yeni bir liste oluştur
        for square in row:
            new_row.append(square)  # Her kareyi yeni satıra ekle
        new_list.append(new_row)  # Yeni satırı ana listeye ekle
    
    new_list[row_no][column_no] = number
    return new_list
