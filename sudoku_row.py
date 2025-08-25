# Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments
# Rows are indexed from 0. The function should return True or False, depending on whether the row is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

def row_correct(sudoku: list, row_no: int):
    repeated = []
    for square in sudoku[row_no]:
        if square != 0 and square in repeated:
            return False
#square != 0 conditionı en azından bir yerde gerekiyor
        if square != 0:
            repeated.append(square)
    return True


if __name__ == "__main__":
    sudoku = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # rivi 0
    [ 2, 2, 0, 0, 5, 0, 7, 0, 0 ],   # rivi 1
    [ 0, 2, 0, 3, 0, 0, 4, 0, 4 ],   # rivi 2
    [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],   # rivi 3
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # rivi 4
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # rivi 5
    [ 0, 0, 7, 8, 0, 3, 9, 6, 6 ],   # rivi 6
    [ 3, 0, 1, 0, 0, 0, 0, 0, 3 ],   # rivi 7
    [ 3, 0, 0, 0, 2, 0, 2, 0, 1 ],   # rivi 8
    ]
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 2))
    print(row_correct(sudoku, 7))


# V2 - mooc.fi:
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
    return True
# Write your solution here
