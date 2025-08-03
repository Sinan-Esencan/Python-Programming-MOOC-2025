"""Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length
of the side of the board. See the examples below for details:"""

# Write your solution here
def chessboard(num):
    for i in range(num):
        for j in range(num):
            if (i+j)%2 == 0:
                print("1", end="")
            else:
                print("0", end="")
        print()

# Testing the function
if __name__ == "__main__":
    chessboard(3)

#alt2:
def chessboard(n):
    for i in range(n):
        row = ""
        for j in range(n):
            if (i + j) % 2 == 0:
                row += "1"
            else:
                row += "0"
        print(row)

if __name__ == "__main__":
    chessboard(3)
    

#alt3: mooc'den ilginc bir alternatif:
def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1

if __name__ == "__main__":
    chessboard(3)
