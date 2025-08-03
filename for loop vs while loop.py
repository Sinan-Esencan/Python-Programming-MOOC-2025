"""Please write a function named hash_square(length), which takes an integer argument. The function prints out a square of hash characters, and the argument specifies the length of the side of the square."""

#alt1: while loop-geriye sayım
def hash_square(x):
    y = x
    while y > 0:
        print("#"*x)
        y -= 1     

if __name__ == "__main__":
    hash_square(5)

#alt2: while loop-duz
def hash_square(x):
    i = 0
    while i < x:
        print("#"*x)
        i += 1     

if __name__ == "__main__":
    hash_square(5)
    
#alt3: for in range
def hash_square(x):
    for i in range(x, 0, -1):
        print(x*"#")    

if __name__ == "__main__":
    hash_square(5)

#alt4: for in range-duz
def hash_square(x):
    for i in range(x):
        print(x*"#")    

if __name__ == "__main__":
    hash_square(5)

#alt5: by using nested loops:
def hash_square(size):
    i = 0
    while i < size:
        j = size
        while  j > 0:
            print("#", end="")
            j -= 1
        print()
        i += 1    

if __name__ == "__main__":
    hash_square(5)
