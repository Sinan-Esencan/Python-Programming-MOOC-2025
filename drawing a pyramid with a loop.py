n = 10 # number of layers in the pyramid
row = "*"

while n > 0:
    print(" " * n + row) #n tane bosluk print eder
    row += "**"
    n -= 1
