# Please write a function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments, and creates and returns a tuple based on the following criteria:
#     1) The first element in the tuple is the smallest of the arguments
#     2) The second element in the tuple is the greatest of the arguments
#     3) The third element in the tuple is the sum of the arguments

def create_tuple(x: int, y: int, z: int):
    if x < y and x < z:
        if y > z:
            numbers = (x,y,x+y+z)
        else:
            numbers = (x,z,x+y+z)
    elif y < z:
        if z > x:
            numbers = (y,z,x+y+z)
        else:
            numbers = (y,x,x+y+z)
    else:
        if x > y:
            numbers = (z,x,x+y+z)
        else:
            numbers = (z,y,x+y+z)
    return numbers

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))


# alt2 - mooc.fi: built-in fonksiyonlar ile cok daha kısa:
def create_tuple(x: int, y: int, z: int):
    """ The function returns a tuple formed from the parameters (smallest, greatest, sum) """
    smallest = min([x, y, z])
    greatest = max([x, y, z])
    sum = x + y + z # sum([x, y, z]) also works
    return (smallest, greatest, sum)
