# The exercise template contains a class definition for a Rectangle. It represents a rectangle shape.
# Please define a class named Square which inherits the Rectangle class. The sides of a square are all of equal length, which makes the square a special case of the rectangle. The new class should not contain any new attributes.
# A Square object is used as follows:
# square = Square(4)
# print(square)
# print("area:", square.area())
# Sample output
# square 4x4
# area: 16

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)
        # *asagıdaki gibi instance attribute'ları sıfırdan tanımlamak yerine superclass'taki init() cagırıldı*
        # self.width = side
        # self.height = side

    def __str__(self):
        return f"square {self.width}x{self.height}"

if __name__ == "__main__":
    square = Square(4)
    print(square)
    print("area:", square.area())
