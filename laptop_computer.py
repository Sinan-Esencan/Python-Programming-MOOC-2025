# The exercise template contains a class definition for a Computer, which has the attributes model and speed.
# Please define a class named LaptopComputer which inherits the class Computer. The constructor of the new class should take a third argument: weight, of type integer.
# Please also include a __str__ method in your class definition.

# Write your solution here:
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed

class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight: int):
        super().__init__(model, speed)
        self.__weight = weight
    
    def __str__(self):
        return f"{self.model}, {self.speed} MHz, {self.__weight} kg"

if __name__ == "__main__":
    laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
    print(laptop)
