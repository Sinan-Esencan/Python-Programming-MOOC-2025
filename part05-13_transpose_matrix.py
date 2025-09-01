# Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. The function should transpose the matrix. Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.
# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.
# The function should not have a return value. The matrix should be modified directly through the reference.

def transpose(matrix: list):
    for row in range(len(matrix)):
        for col in range(row, len(matrix[row])):
            temp = matrix[col][row]
            matrix[col][row] = matrix[row][col]
            matrix[row][col] = temp

if __name__ == "__main__":
    matrix = [
        [1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]
    ]
    transpose(matrix)
    print(matrix)

#V2 mooc-fi:
def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#V3 mooc-fi:
def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n): #kare matris oldugundan n denmis
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

#V4 farklı bir versiyon: referansı etkilemez
def transpose(matrix: list):
    matrix_copy = [row[:] for row in matrix]
    for row in range(len(matrix_copy)):
        for col in range(row, len(matrix_copy[row])):
            matrix_copy[col][row] = matrix[row][col]
            matrix_copy[row][col] = matrix[col][row]
    print(matrix_copy)
    print(matrix)
