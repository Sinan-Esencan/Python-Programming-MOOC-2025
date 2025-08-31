# Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a sudoku grid as its argument. The function should
# use the functions from the three previous exercises to determine whether the complete sudoku grid is filled in correctly. Copy the functions from the exercises above
# into your Python code file for this exercise.
# The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. If all contain each of the numbers 1 to 9 at most once, the function returns True.
# If a single one is filled in incorrectly, the function returns False.
# The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with thicker borders. These are the blocks the function should check, and they
# begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).

def column_correct(sudoku: list, column_no: int):
    repeated = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in repeated:
            return False
        elif number > 0:
            repeated.append(number)
    return True


def row_correct(sudoku: list, row_no: int):
    repeated = []
    for square in sudoku[row_no]:
        if square != 0 and square in repeated:
            return False
        elif square != 0:
            repeated.append(square)
    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    repeated = []
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no+3):
            if sudoku[i][j] > 0 and sudoku[i][j] in repeated:
                return False
            elif sudoku[i][j] > 0:
                repeated.append(sudoku[i][j]) 
    return True


def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        x = column_correct(sudoku, i)
        y = row_correct(sudoku, i)
        if x == False or y == False: #alt: if not x or not y:
            return False
    
    for r in range(3):
        for c in range(3):
            x = block_correct(sudoku, r*3, c*3)
            if x == False or y == False:
                return False
    return True

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku))
    print(sudoku_grid_correct(sudoku2))


# alt2 - mooc.fi: sadece sudoku_grid_correct fonksiyonunu ekledim:
def sudoku_grid_correct(sudoku: list):
    for row in range(0,9):
        if not row_correct(sudoku, row):
            return False

    for column in range(0,9):
        if not column_correct(sudoku, column):
            return False

    for row in range(0,9,3):
        for column in range(0,9,3):
            if not block_correct(sudoku, row, column):
                return False

    return True
