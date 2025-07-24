width = int(input("Width: "))
height = int(input("Height: "))
h = 0
w = 0
string = ""

while h < height:
    while w < width:
        string += "#"
        w+=1
    print(string)
    h+=1


#V2: practical:
width = int(input("Width: "))
height = int(input("Height: "))

n = 0
while n < height:
    print("#" * width)
    n += 1
