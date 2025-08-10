"""Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument."""

def spruce(middle):
    print("a spruce!")
    blank = middle -1
    for i in range (1, 2*middle, 2):
        print(f"{blank*" "}{i*"*"}")
        blank -= 1
    print((middle-1)*" " + 1*"*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)


#Alt2: MOOC alternatifi daha güzel:
def spruce(height):
    print("a spruce!")
    i = 1
    while i <= height:
        empty = height - i
        stars = 2 * i - 1
        print(" " * empty + "*" * stars)
        i += 1
    print(" " * (height - 1) + "*")

if __name__ == "__main__":
    spruce(3)
