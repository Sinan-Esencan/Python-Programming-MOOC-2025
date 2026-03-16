# part1: Decreasing the value of the counter:
# Please complete the method decrease defined in the template, so that it decreases the value stored in the counter by one. See the example above for expected behaviour

# part2: The counter must not have a negative value
# Please add functionality to your decrease method, so that the value of the counter will never reach negative values. If the value of the counter is 0, it will not be further decreased.

# part3: Setting the value to zero:
# Please add a method set_to_zero which sets the value of the counter to 0

# part4: Resetting the counter:
# Please add a method reset_original_value() which resets the counter to its initial state

# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.original = initial_value
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    # Write the rest of the methods here!
    def decrease(self):
        if self.value != 0: #alt: self.value > 0 veya self.value >= 1
            self.value -= 1

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.original

if __name__ == "__main__":
    # 1
    counter = DecreasingCounter(10)
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    
    # # 2
    # counter = DecreasingCounter(2)
    # counter.print_value()
    # counter.decrease()
    # counter.print_value()
    # counter.decrease()
    # counter.print_value()
    # counter.decrease()
    # counter.print_value()
    
    # # 3
    # counter = DecreasingCounter(100)
    # counter.print_value()
    # counter.set_to_zero()
    # counter.print_value()

    # # 4
    # counter = DecreasingCounter(55)
    # counter.decrease()
    # counter.decrease()
    # counter.decrease()
    # counter.decrease()
    # counter.print_value()
    # counter.reset_original_value()
    # counter.print_value()
