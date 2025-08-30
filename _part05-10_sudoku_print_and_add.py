# In this exercise we will complete two more functions for the sudoku project from the previous section: print_sudoku and add_number.
# The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. The function should
# print out the grid in the format specified in the examples below.
# The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid,
# two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. 
# The function should add the digit to the specified location in the grid.

def print_sudoku(sudoku: list):
    row_count = 0
    for row in sudoku:
        column_count = 0
        for number in row:
            column_count += 1
            if column_count % 3 == 0:
                if number == 0:
                    print("_  ", end="")
                else:
                    print(f"{number}  ", end="")
            else:
                if number == 0:
                    print("_ ", end="")
                else:
                    print(f"{number} ", end="")
        row_count += 1
        if row_count % 3 == 0:    
            print("\n")
        else:
            print()


def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number


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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)


# V2 mooc.fi:
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
            
def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number
